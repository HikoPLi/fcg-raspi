from gpiozero import AngularServo
import time


# motor GPIO BCM port
pinMotorA = 10
pinMotorB = 9
pinMotorC = 11
pinMotorD = 5
pinMotorE = 6


def motor_action90(servo_pin):

    print(f"----- servo GPIO: {servo_pin} start -----")
    servo = AngularServo(servo_pin, min_angle=-90, max_angle=90)

    print(f"----- servo GPIO: {servo_pin} angle -90 -----")
    servo.angle = -90
    
    time.sleep(1)
    servo.close()
    servo = AngularServo(servo_pin, min_angle=-90, max_angle=90)
    print(f"----- servo GPIO: {servo_pin} angle 90 -----")
    servo.angle = 80

    time.sleep(2)
    print(f"----- servo GPIO: {servo_pin} close -----")
    servo.close()

def motor_action45(motorNo, servo_pin):

    if motorNo == "b":
        time.sleep(1.6)
    if motorNo == "c":
        time.sleep(3.5)
    if motorNo == "d":
        time.sleep(5)
    if motorNo == "e":
        time.sleep(7)

    print(f"----- servo GPIO: {servo_pin} start -----")
    servo = AngularServo(servo_pin, min_angle=-90, max_angle=90)
    


    print(f"----- servo GPIO: {servo_pin} angle -40 -----")
    servo.angle = -40
    
    time.sleep(2)
    servo.close()
    servo = AngularServo(servo_pin, min_angle=-90, max_angle=90)
    print(f"----- servo GPIO: {servo_pin} angle 90 -----")
    servo.angle = 90

    time.sleep(2)
    print(f"----- servo GPIO: {servo_pin} close -----")
    servo.close()


def motor_actions(isDetected: bool, isMetal: bool, garbageType):
    try:
        if isDetected:
            print(f"----- IS_DETECTED: {isDetected}, IS_METAL: {isMetal} -----\n\n")
            print("motorA")
            print(f"----- servo GPIO: {pinMotorA} start -----")
            servo = AngularServo(pinMotorA, min_angle=-90, max_angle=90)
            print(f"----- servo GPIO: {pinMotorA} angle -90 -----")
            servo.angle = -90

            time.sleep(1)

            if garbageType["metal"]:
                print("motorB, recyclable")
                motor_action45("b",pinMotorB)
                time.sleep(1)
                print(f"----- servo GPIO: {pinMotorA} angle 90 -----")
                servo.angle = 90
            elif garbageType["plastic"]:
                print("motorC, hazardous")
                motor_action45("c",pinMotorC)
                time.sleep(1)
                print(f"----- servo GPIO: {pinMotorA} angle 90 -----")
                servo.angle = 90
            elif garbageType["paper"]:
                print("motorD, food")
                motor_action45("d",pinMotorD)
                time.sleep(1)
                print(f"----- servo GPIO: {pinMotorA} angle 90 -----")
                servo.angle = 90
            elif garbageType["glass"]:
                print("motorE, other")
                motor_action45("e",pinMotorE)

                time.sleep(1)
                print(f"----- servo GPIO: {pinMotorA} angle 90 -----")
                servo.angle = 90
            print(f"----- servo GPIO: {pinMotorA} angle 90 -----")
            # servo.angle = 90

            time.sleep(2)
            print(f"----- servo GPIO: {pinMotorA} close -----")
            servo.close()

        else:

            print(f"----- IS_DETECTED: {isDetected} -----\n\n")

    except Exception as e:

        print(f"----- IS_DETECTED: False, MOTOR ERROR: {str(e)} -----\n\n")


def motor_debug():

    try:
        print("motorA")
        motor_action90(pinMotorA)
        print("motorB")
        motor_action90(pinMotorB)
        time.sleep(0.5)
        print("motorC")
        motor_action90(pinMotorC)
        time.sleep(0.5)
        print("motorD")
        motor_action90(pinMotorD)
        time.sleep(0.5)
        print("motorE")
        motor_action90(pinMotorE)

    except Exception as e:
        print(f"----- DEBUG: False, MOTOR ERROR: {str(e)} -----\n\n")
