import RPi.GPIO as GPIO
import time

D = [24,25,8,7,12,16,20,21]
d = D[::-1]


GPIO.setmode(GPIO.BCM)
GPIO.setup([24,25,8,7,12,16,20,21],GPIO.OUT)

def lightUp(Number, period):
    GPIO.output(D[Number], 1)
    time.sleep(period)

def blink( blinkCount, blinkPeriod):
    for i in range(blinkCount):
        GPIO.output(D, 1)
        time.sleep(blinkPeriod)
        GPIO.output(D, 0)
        time.sleep(blinkPeriod)

def runningLight(count, period):
    for j in range(count):
        for i in range(8):
            GPIO.output(D[i],1)
            GPIO.output(D[i-1],0)
            time.sleep(period)
            
def runningDark(count, period):
    GPIO.output(D,1)
    for j in range(count):
        for i in range(8):
            GPIO.output(D[i],0)
            GPIO.output(D[i-1],1)
            time.sleep(period)

def decToBinList(decNumber):
    a = []
    for i in range(8):
        a.append(decNumber%2)
        decNumber//=2
    return a[::-1]

def lightNumber(number):
    n = decToBinList(number)
    for j in range(8):
        GPIO.output(d[j],n[j])
    time.sleep(1)

def runningPattern(pattern, direction):
    lightNumber(pattern)
    if direction >= 0:
        for i in range(direction):
            tmp = 0
            if (pattern & 128) == 128:
                tmp = 1
                pattern -= 128  
            pattern = (pattern<<1)
            pattern+=tmp
            lightNumber(pattern)
    else:       
        for i in range(abs(direction)):
            tmp = 0
            if (pattern & 1) == 1:
                tmp = 128
                pattern -= 1
            pattern = (pattern>>1)
            pattern+=tmp
            lightNumber(pattern)


def govnyashka():
    for i in range(256):
        n = bin_convert(i)
        for j in range(8):
            GPIO.output(d[j],n[j])
        time.sleep(0.1)
def shim():
    i = 10**(-2)
    while i > 10**(-4)/2:
        blink(100, i)
        i -= 10**(-2)
    print(1)
    while i < 10**(-2):
        blink(1000, i)
        i += 10**(-4)
    print(1)
shim()
#lightUp(1, 1)
#blink(1, 30000000000, 0.000000000001)
#runningLight(3, 0.5)
#runningDark(3, 0.5)
#print(decToBinList(3))
#lightNumber(5)
#runningPattern(130, -15)



GPIO.output(D,0)



