import requests
import json
import time


def text_to_speech(text='Привет Настя!'):
    headers = {"Authorization": f"Bearer {('your api Edenai')}"} #https://www.edenai.co/
    url = "https://api.edenai.run/v2/audio/text_to_speech"

    # payload = {"providers": 'lovoai',
    #            "language": "ru-RU",
    #            "option": "FEMALE",f
    #            'lovoai': 'ru-RU_Natalia Sychyov',
    #            'text': f'{text}',
    #            }
    payload = {"providers": 'lovoai',
               "language": "ru-RU",
               "option": "MALE",
               'lovoai': 'ru-RU_Alexei Syomin',
               'text': f'{text}',
               }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    unx_time = int(time.time())
    with open(f'{unx_time}.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    audio_url = result.get('lovoai').get('audio_resource_url')
    r = requests.get(audio_url)
    with open(f'{unx_time}.wav', 'wb') as file:
        file.write(r.content)
def main():
    text_to_speech(text= 'в тебя многие не верили , но ты не сдавался, зная что ты остановишься только тогда когда достигнешь цели!')


if __name__ =='__main__':
    main()
