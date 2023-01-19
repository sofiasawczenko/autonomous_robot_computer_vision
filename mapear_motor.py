import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
MOTOR = 12 
GPIO.setup(MOTOR, GPIO.OUT) 

GPIO.output(MOTOR, True)
input("Aperte enter para parar o motor.")
GPIO.output(MOTOR, False)

GPIO.cleanup()
