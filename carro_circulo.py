import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
RF = 12 #Right - Forward
RB = 32 #Right - Backward
LF = 33 #Left  - Forward
LB = 35 #Left  - Backward
GPIO.setup(RF, GPIO.OUT) 
GPIO.setup(RB, GPIO.OUT)
GPIO.setup(LF, GPIO.OUT)
GPIO.setup(LB, GPIO.OUT)
motor_RF = GPIO.PWM(RF, 100)
motor_RB = GPIO.PWM(RB, 100)
motor_LF = GPIO.PWM(LF, 100)
motor_LB = GPIO.PWM(LB, 100)
motor_RF.start(0)
motor_RB.start(0)
motor_LF.start(0)
motor_LB.start(0)

for i in range(0,100):
    motor_RF.ChangeDutyCycle(i)
    motor_LF.ChangeDutyCycle(i)
    time.sleep(0.005)

time.sleep(2)

for i in range(0,100):
    motor_RF.ChangeDutyCycle(100-i)
    motor_LF.ChangeDutyCycle(100-i)
    time.sleep(0.005)

input("Aperte enter para parar o carrinho.")

motor_RF.stop()
motor_RB.stop()
motor_LF.stop()
motor_LB.stop()
GPIO.cleanup()