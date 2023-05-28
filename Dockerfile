FROM python:3.9
ADD . /app
WORKDIR /app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
