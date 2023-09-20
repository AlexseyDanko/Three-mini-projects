import openai
from api import api_key # better to use OS
import json
from base64 import b64decode

prompt = input('The prompt: only fantasy')
openai.api_key = api_key

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size='1024x1024',
    response_format='b64_json'
)
with open('base.json', 'w') as file:
    json.dump(response, file, indent=4, ensure_ascii=False)

image_base = b64decode(response['data'][0]['b64_json'])
file_name = '_'.join(prompt.split(' '))
with open(f'{file_name}.png', 'wb') as file:
    file.write(image_base)
