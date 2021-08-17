from time import sleep
import RPi.GPIO as GPIO
import socketio

isClicked1 = False
isClicked2 = False
pin1 = 18
pin2 = 23

sio = socketio.Client()
sio.connect('http://ipadress:3000')

# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    #break
    if GPIO.input(pin1) == GPIO.HIGH and isClicked1 == False:
        try:
            isClicked1 = True
            sio.emit('breakPressed', 'balls')
            print('break')
            sleep(0.2)
        except Exception as e:
            print(f'I Messed up lmao: {e}')
            break
    elif GPIO.input(pin1) == GPIO.LOW and isClicked1 == True:
        try:
            isClicked1 = False
            sio.emit('notBreak', 'nuts')
            print('let go')
            sleep(0.2)
        except Exception as e:
            print(f'I Messed up lmao: {e}')
            break
    #place
    
    if GPIO.input(pin2) == GPIO.HIGH and isClicked2 == False:
        try:
            isClicked2 = True
            sio.emit('placePressed', 'piss')
            print('place')
            sleep(0.2)
        except Exception as e:
            print(f'I Messed up lmao: {e}')
            break
    elif GPIO.input(pin2) == GPIO.LOW and isClicked2 == True:
        try:
            isClicked2 = False
            sio.emit('notPlace', 'cum')
            print('let go')
            sleep(0.2)
        except Exception as e:
            print(f'I Messed up lmao: {e}')
            break
    # else:
    #     print(GPIO.input(pin2))