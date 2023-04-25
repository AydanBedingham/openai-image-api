from flask import Flask, request, send_file
import json
import openai
import os
import logging
import structlog
from io import BytesIO
import requests

log = structlog.getLogger(__name__)

IMAGE_SIZE = "256x256" # 512x512, 1024x1024

structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY == None:
    raise Exception("OPENAI_API_KEY environment variable is missing!")

log.debug("Found OPENAI_API_KEY: {}".format(OPENAI_API_KEY))

openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size=IMAGE_SIZE
    )
    return response['data'][0]['url']

def download_image(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.content
    else:
        raise Exception("Failed to retrieve file")

@app.route('/create', methods=['GET']) 
def prompt():
    prompt = request.args.get('prompt')
    if not prompt: 
        return 'Missing Prompt query string parameter!', 400 
    
    log.debug("Received Prompt: {}".format(prompt))

    url = generate_image(prompt)
    content_bytes = download_image(url)

    log.debug("Generated Response: {}".format(content_bytes))
    
    buffer = BytesIO()
    buffer.write(content_bytes)
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0')