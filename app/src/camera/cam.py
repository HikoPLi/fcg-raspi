from picamera2 import Picamera2, Preview
from time import sleep
import base64
import os


def capture_and_encode_image(picam):
    try:
        picturePath = "cam.jpg"
        picam.capture_file(picturePath)

        with open(picturePath, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

        # os.remove(picturePath)

        return encoded_image

    except Exception as e:
        print("error:", e)
        return False


def cam_debug():
    try:
        picam = Picamera2(0)
        picam.start()

    except Exception as e:
        print(f"----- DEBUG: False, CAM ERROR: {str(e)} -----\n\n")
