FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN apt-get update -y
RUN apt-get install tk -y

COPY . .

CMD ["python", "app.py"]