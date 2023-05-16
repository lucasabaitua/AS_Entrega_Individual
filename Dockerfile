FROM python:latest

RUN apt-get update
RUN apt-get -y install python
RUN pip install couchdb

COPY app.py .

CMD ["python", "./app.py"]
