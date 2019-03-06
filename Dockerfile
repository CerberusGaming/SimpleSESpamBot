FROM python:3.7

ENV API_KEY "cerberusgamingiscool=="
ENV API_URL "http://127.0.0.1:8080."
ENV MESSAGE_DELAY 300
ENV MESSAGE "Some Idiot "

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py ./

CMD ["python", "./server.py"]