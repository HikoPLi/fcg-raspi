from gpiozero import AngularServo
import time
import pigpio

# motor GPIO BCM port
pinMotorA = 10
pinMotorB = 9
pinMotorC = 11
pinMotorD = 5
pinMotorE = 6

# pigpio's initialization
pi = pigpio.pi()

def motor_action(servo_pin, delay_time, start_angle, end_angle):
    time.sleep(delay_time)
    print(f"----- servo GPIO: {servo_pin} start -----")
    pi.set_servo_pulsewidth(servo_pin, start_angle)
    time.sleep(1)
    print(f"----- servo GPIO: {servo_pin} angle {end_angle} -----")
    pi.set_servo_pulsewidth(servo_pin, end_angle)
    time.sleep(2)
    print(f"----- servo GPIO: {servo_pin} close -----")
    pi.set_servo_pulsewidth(servo_pin, 0)

def motor_actions(isDetected: bool, isMetal: bool, garbageType):
    try:
        if isDetected:
            print(f"----- IS_DETECTED: {isDetected}, IS_METAL: {isMetal} -----\\n\\n")
            print("motorA")
            motor_action(pinMotorA, 0, 500, 2500)
            if garbageType["metal"]:
                print("motorB, recyclable")
                motor_action(pinMotorB, 1.8, 500, 2500)
            elif garbageType["plastic"]:
                print("motorC, hazardous")
                motor_action(pinMotorC, 4.29, 500, 2500)
            elif garbageType["paper"]:
                print("motorD, food")
                motor_action(pinMotorD, 6.54, 500, 2500)
            elif garbageType["glass"]:
                print("motorE, other")
                motor_action(pinMotorE, 7.89, 500, 2500)
        else:
            print(f"----- IS_DETECTED: {isDetected} -----\\n\\n")
    except Exception as e:
        print(f"----- IS_DETECTED: False, MOTOR ERROR: {str(e)} -----\\n\\n")

def motor_debug():
    try:
        print("motorA")
        motor_action(pinMotorA, 0, 500, 2500)
        print("motorB")
        motor_action(pinMotorB, 0, 500, 2500)
        print("motorC")
        motor_action(pinMotorC, 0, 500, 2500)
        print("motorD")
        motor_action(pinMotorD, 0, 500, 2500)
        print("motorE")
        motor_action(pinMotorE, 0, 500, 2500)
    except Exception as e:
        print(f"----- DEBUG: False, MOTOR ERROR: {str(e)} -----\\n\\n")
