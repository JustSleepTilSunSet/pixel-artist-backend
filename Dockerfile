FROM python:3.8-slim

WORKDIR '/app'

RUN pip3 install flask
COPY . .

RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0", "--port=10001"]
EXPOSE 10001
