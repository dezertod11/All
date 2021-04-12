import RPi.GPIO as GPIO
import time

D = [26,19,13,6,5,11,9,10]
d = D[::-1]


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(GPIO.OUT)
GPIO.setup(D+[17],GPIO.OUT)

GPIO.output(17, 1)

GPIO.setup(4,GPIO.IN)

def decToBinList(decNumber):
    a = []
    for i in range(8):
        a.append(decNumber%2)
        decNumber//=2
    return a[::-1]

def num2dac(value):
    value = decToBinList(value)
    GPIO.output(D,value)

#def dac_data(data):
#    for i in range(0, bit_depth):
#        GPIO.output(D[i], data[i])

def adc_procedure():
    for j in range(0, 2**8):
        num2dac(j)
        time.sleep(0.001)
        if GPIO.input(4) == 0:
            print(j,"-", round(j*3.26/255*100)/100,"В")
            break
        
    return j

try:
    num2dac(128)
    if GPIO.input(17) == 1:
            print(100000)
    while True:
        adc_procedure()

except ZeroDivisionError:
    print("Только число от 0 до 255")
except ValueError:
    print("Только число от 0 до 255")
finally:    
    GPIO.cleanup()