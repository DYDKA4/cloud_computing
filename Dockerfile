FROM python:3.8
RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
COPY ./requirements.txt /app/requirements.txt

WORKDIR app

RUN pip install -r requirements.txt

COPY .venv /app/.venv
COPY main.py /app/main.py
EXPOSE 5000