import base64
import requests
import json

# from app.eatmongo.config.settings import settings
from app.src.analyse.schemas.analyse import AnalyseDocument


class AnalyseService:
    analyseModel = AnalyseDocument

    def picture_analyse(self, base64Obj):
        api_key = "PUT_KEY_HERE"

        prompt = "What is the main object in the picture? What is the material(mainly material)? Is it metal? Which type of rubbish(metal, plastic, paper, glass)?  please return me a json by the format of {'success': bool, 'object': string, 'material': string, 'isMetal': bool, 'type':{'metal': bool, 'plastic': bool, 'paper': bool, 'glass': bool} 'detail': string}, each just need one word except detail, every word is needed to be lowercase"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt,
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64Obj}"},
                        },
                    ],
                }
            ],
            "max_tokens": 300,
            "temperature": 0,
        }

        # Make the API request and print out the response
        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload,
            )
            data = response.json()
            content = data["choices"][0]["message"]["content"]
            json_str = content.replace("```json\n", "").replace("\n```", "")
            json_data = json.loads(json_str)
            print(json_data)

            # if json_data["material"] == "glass" or "plastic":
            #     plasticUrl = "https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/rockcms/2022-07/220728-coke-bottles-mjf-0712-f4d231.jpg"
            #     glassUrl = "https://img.uline.com/is/image/uline/S-24698?$Mobile_Zoom$"

            #     response = requests.get(
            #         plasticUrl if json_data["material"] == "plastic" else glassUrl
            #     )
            #     image_content = response.content
            #     base64PlasticOrGlassPicture = base64.b64encode(image_content).decode(
            #         "utf-8"
            #     )
            #     payload = {
            #         "model": "gpt-4-vision-preview",
            #         "messages": [
            #             {
            #                 "role": "user",
            #                 "content": [
            #                     {
            #                         "type": "text",
            #                         "text": f"This picture has been detected as {json_data['material']}, please compare the pictures and answer What is the main object in the picture? What is the material(mainly material)? Is it metal? Is recyclable? Which type of rubbish(Recyclables, hazardous waste, food waste, other waste)?",
            #                     },
            #                     {
            #                         "type": "image_url",
            #                         "image_url": {
            #                             "url": f"data:image/jpeg;base64,{base64Obj}"
            #                         },
            #                     },
            #                     {
            #                         "type": "image_url",
            #                         "image_url": {
            #                             "url": f"data:image/jpeg;base64,{base64PlasticOrGlassPicture}"
            #                         },
            #                     },
            #                     {
            #                         "type": "text",
            #                         "text": "return me a json by the format of {'success': bool, 'object': string, 'material': string, 'isMetal': bool, 'type':{'recyclable': bool, 'hazardous': bool, 'food': bool, 'other': bool} 'detail': string}, each just need one word except detail, every word is needed to be lowercase",
            #                     },
            #                 ],
            #             }
            #         ],
            #         "max_tokens": 300,
            #         "temperature": 0,
            #     }
            #     response = requests.post(
            #         "https://api.openai.com/v1/chat/completions",
            #         headers=headers,
            #         json=payload,
            #     )
            # data = response.json()
            # content = data["choices"][0]["message"]["content"]
            # json_str = content.replace("```json\n", "").replace("\n```", "")
            # json_data = json.loads(json_str)
            # print(json_data)

        except Exception as e:
            json_data = {"success": False, "error": str(e), "content": json_str}

        return json_data


analyseService = AnalyseService()
