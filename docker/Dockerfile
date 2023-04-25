FROM python:3.9

COPY ./docker/docker-requirements.txt /docker-requirements.txt
RUN pip install -r /docker-requirements.txt

COPY ./openai-image-api /openai-image-api
RUN pip install -r /openai-image-api/requirements.txt

WORKDIR /openai-image-api
EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "--log-level=info", \
     "app:app", "--workers=2", "--threads=2"]
