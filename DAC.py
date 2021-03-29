import RPi.GPIO as GPIO
import time

D = [26,19,13,6,5,11,9,10]
d = D[::-1]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(GPIO.OUT)
GPIO.setup(D,GPIO.OUT)


GPIO.output(D, 0)



def decToBinList(decNumber):
    a = []
    for i in range(8):
        a.append(decNumber%2)
        decNumber//=2
    return a[::-1]

def num2dac(value):
    value = decToBinList(value)
    for j in range(8):
        GPIO.output(D[j],value[j])
    time.sleep(0.02)

print("Введите число повторений")
repetitionsNumber = int(input())
try:
    if repetitionsNumber<0:
        1/0
    for i in range(repetitionsNumber):
        for e in range(256):
            num2dac(e)
        for e in range(255,-1,-1):
            num2dac(e)
except ZeroDivisionError:
    print("Только число от 0 до 255")
except ValueError:
    print("Только число от 0 до 255")
finally:    
    GPIO.cleanup()