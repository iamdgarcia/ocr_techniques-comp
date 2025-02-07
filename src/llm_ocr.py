import base64
import requests
from dotenv import load_dotenv
import os
load_dotenv()

# Set up your API key for OpenAI
api_key = os.environ.get("OPENAI_KEY")

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "./assets/receta_farmacia.png"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is the doctor prescribing? Return only the text handwritten"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}
import time
start_time = time.time()
response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
print(f"Total time: {time.time()-start_time} s ")
print(response.json()['choices'][0]['message']['content'])
