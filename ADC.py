import RPi.GPIO as GPIO
import time

D = [26,19,13,6,5,11,9,10]
d = D[::-1]


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(GPIO.OUT)
GPIO.setup(D+[17],GPIO.OUT)


GPIO.output(17, 1)

def decToBinList(decNumber):
    a = []
    for i in range(8):
        a.append(decNumber%2)
        decNumber//=2
    return a[::-1]

def num2dac(value):
    value = decToBinList(value)

    GPIO.output(D,value)
    time.sleep(0.02)

#def dac_data(data):
#    for i in range(0, lenbit_depth):
#        GPIO.output(D[i], data[i])

#def adc_procedure():
#    for j in range(0, 2**bit_depth):
#        dac_data(bin_convert(j))
#        time.sleep(0.1)

try:
    while True:
        e = int(input())
        if e<0:
            1/0
        elif e == -1:
            exit()
        num2dac(e)
        print("напряжение V =",round(e*3.26/255*100)/100, "В")
except ZeroDivisionError:
    print("Только число от 0 до 255")
except ValueError:
    print("Только число от 0 до 255")
finally:    
    GPIO.cleanup()