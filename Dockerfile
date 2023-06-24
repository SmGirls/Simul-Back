FROM python:3.10.11-slim

WORKDIR /usr/src/app
COPY ./share/Data ./share/Data
COPY ./share/static ./share/static
COPY templates ./templates
COPY app.py .
COPY Dockerfile .
COPY requirements.txt .

# RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt
CMD python app.py
