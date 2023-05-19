FROM nginx

WORKDIR /usr/src/app

COPY . .

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

# RUN python3 ./Data/data_slicing.py
# RUN python3 ./visualize.py

CMD ["python3", "./Data/data_slicing.py"]
CMD ["python3","./visualize.py"]

COPY index.html /usr/share/nginx/html

EXPOSE 80

CMD ["sh", "-c", "mv result.png /usr/share/nginx/html && nginx -g 'daemon off;'"]
