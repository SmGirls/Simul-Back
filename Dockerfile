# build stage
FROM python:3.8.11-slim as builder
WORKDIR /usr/src/app
COPY requirements.txt .
COPY test.py .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 ./test.py
COPY . .

# production stage
FROM nginx:1.21.3-alpine
COPY --from=builder /usr/src/app/test0.png /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]