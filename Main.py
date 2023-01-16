from controller import httpController
#import RPi.GPIO as GPIO
import time


ledPins = {'red': 18, 'yellow': 19, 'green': 20,}

def turnOffAllLeds():
    print('', end='')

    """
    GPIO.setmode(GPIO.BOARD)

    for pin in ledPins.keys():
        GPIO.setup(ledPins[pin], GPIO.OUT)
        GPIO.cleanup(ledPins[pin])
    """

def turnOnLed(pin):
    print(pin, '번 PIN Turn On!')

    """
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)
    """


currentLed = ''
httpController = httpController.HttpController()

while True:
    response = ''  # http get

    response = httpController.get('https://tails1101.cafe24.com/test/getled.php',
        None
    )

    if response is not None:
        if response['success']:
            if response['name'] != currentLed:
                turnOffAllLeds()
                turnOnLed(ledPins[response['name']])
                currentLed = response['name']
        else:
            print('통신 중 오류가 발생하였습니다.')
    else:
        print('통신 중 오류가 발생하였습니다.')
    
    time.sleep(3)
