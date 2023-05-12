# build stage

FROM python:3.8.11-slim as builder
WORKDIR /usr/src/app
COPY . .
ENV START_ROW=21
RUN pip3 install -r requirements.txt
RUN python3 ./Data/create_data.py
RUN python3 ./visualize.py

# production stage
FROM nginx:1.21.3-alpine
COPY --from=builder /usr/src/app /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]