openai-image-api
================
openai-image-api is a Web API written in Python that uses the OpenAI to generate images for text-based prompts.

Running Locally
------------
Navigate to the openai-image-api directory.
```
cd openai-image-api
```

Install dependencies with pip
```
pip install -r requirements.txt
```

Set the 'OPENAI_API_KEY' environment variable:
```
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Run the application with python
```
python app.py
```

API
-----
GET /create?prompt=<Your Prompt>
```
curl --location 'http://127.0.0.1:5000/create?prompt=Cats'
```

Response
```
image/png
```

Docker
------

We also provide a Docker image to make it easier to run *openai-image-api*
```
docker build . -t openai-image-api -f docker/Dockerfile
```

Then run the image
```
docker run --rm -p 5000:5000 --env OPENAI_API_KEY=<YOUR_OPENAI_API_KEY> openai-image-api
```
