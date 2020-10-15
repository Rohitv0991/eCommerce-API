FROM python:3.8-slim-buster
WORKDIR /app
ADD . /app

RUN set -xe
RUN apt-get update
RUN apt-get install -y python-pip

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

EXPOSE 5000
# docker build -t flaskapp .

ENTRYPOINT ["python"]
CMD ["app.py"]