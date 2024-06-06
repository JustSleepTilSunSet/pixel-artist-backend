FROM python:3.8-slim

WORKDIR '/app'

RUN pip3 install flask
COPY . .

CMD tail -f /dev/null
