FROM python:3.11

WORKDIR /usr/src/application/

COPY ./requirements.txt /usr/src/application/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r  /usr/src/application/requirements.txt

COPY ./app /usr/src/application/app



