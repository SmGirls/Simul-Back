FROM nginx

WORKDIR /usr/src/app

COPY test.py .
COPY requirements.txt .

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

RUN python3 ./test.py

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]