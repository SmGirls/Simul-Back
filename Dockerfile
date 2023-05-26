FROM python:3.10.11-slim

WORKDIR /usr/src/app

COPY . .

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

# EXPOSE 80

RUN chmod +x ./entrypoint.sh

CMD ["./entrypoint.sh"]