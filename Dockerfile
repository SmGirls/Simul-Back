FROM python:3.10.11-slim

WORKDIR /usr/src/app
COPY ./share/static ./share/static

COPY Dockerfile .
COPY requirements.txt .

COPY app.py .

# RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt
EXPOSE 7000
CMD python app.py
