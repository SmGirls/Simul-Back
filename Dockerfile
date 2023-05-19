# build stage
FROM python:3.8.11-slim as builder
WORKDIR /usr/src/app
COPY . .
ARG index
ENV START_ROW=${index}
RUN pip3 install -r requirements.txt
# RUN python3 ./visualize.py
CMD [ "python3", "./visualize.py" ]

# production stage
FROM nginx:1.21.3-alpine
COPY --from=builder /usr/src/app /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# build stage
# FROM python:3.8.11-slim as builder
# ARG row
# ENV START_ROW=$row

# WORKDIR /usr/src/app
# COPY . .
# RUN pip3 install -r requirements.txt
# RUN python3 ./Data/data_slicing.py
# RUN python3 ./visualize.py

# production stage
# FROM nginx:1.21.3-alpine
# COPY --from=builder /usr/src/app /usr/share/nginx/html/
# COPY index.html /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]