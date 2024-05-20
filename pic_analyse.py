from app.src.analyse.analyse_service import analyseService
from app.src.motor.motor import motor_actions, motor_debug
from picamera2 import Picamera2
from app.src.camera.cam import cam_debug, capture_and_encode_image
from app.src.ir.ir import irSensor
import time
import os
import json


def pic_analyse(picam):
    os.system("gpio readall")
    response = {}
    while True:
        try:

            isObj = irSensor()
            if isObj:
                print("detected")
                base64pic = capture_and_encode_image(picam)
                if not base64pic:
                    response = {
                        "success": False,
                        "message": "Failed to capture and encode image",
                    }
                    print(response)

                response = analyseService.picture_analyse(base64pic)
                isSuccess = response["success"]
                if isSuccess == True:
                    print(response)
                    isMetal = response["isMetal"]
                    GarbageType = response["type"]
                    motor_actions(isSuccess, isMetal, GarbageType)  # motor action

                elif isSuccess == False:
                    response = {"success": False, "message": "Failed to process image"}
                    print(response)

            with open("result.json", "w") as f:
                json.dump(response, f)

        except Exception as e:
            response = {"success": False, "detail": str(e)}
            print(response)
            with open("result.json", "w") as f:
                json.dump(response, f)

        time.sleep(1)


def main():
    
    print("----- Self Debugging ----- \n\n")

    print("----- Motor Debugging -----")
    motor_debug()

    print("----- Self Debug Finish -----")
    picam = Picamera2(0)
    picam.start()
    pic_analyse(picam)


if __name__ == "__main__":
    main()
