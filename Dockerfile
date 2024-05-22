FROM python:3.12.3-alpine

WORKDIR '/app'

RUN pip3 install flask
COPY . .

CMD tail -f /dev/null
