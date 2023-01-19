from controller import httpController
import RPi.GPIO as GPIO
import time


ledPins = {'red': 17, 'yellow': 27, 'green': 22,}

def turnOffAllLeds():
    global ledPins
    print('', end='')

    GPIO.setmode(GPIO.BCM)

    for pin in ledPins.keys():
        GPIO.setup(ledPins[pin], GPIO.OUT)
        GPIO.cleanup(ledPins[pin])

def turnOnLed(pin):
    global ledPins
    print(pin, 'PIN Turn On!')

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPins[pin], GPIO.OUT)
    GPIO.output(ledPins[pin], True)


currentLed = ''
httpController = httpController.HttpController()

while True:
    response = httpController.get('https://tails1101.cafe24.com/test/getled.php',
        None
    )

    if response is not None:
        if response['success']:
            if response['name'] != currentLed:
                turnOffAllLeds()
                turnOnLed(response['name'])
                currentLed = response['name']
        else:
            print('통신 중 오류가 발생하였습니다.')
    else:
        print('통신 중 오류가 발생하였습니다.')
    
    time.sleep(3)
