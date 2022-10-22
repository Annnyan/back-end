FROM python:3.10.8

ENV FLASK_APP=application

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY application /opt/application

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT