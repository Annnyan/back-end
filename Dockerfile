FROM python:3.10.8

ENV FLASK_APP=app

ENV FLAK_DEBUG=$FLAK_DEBUG

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY . /opt

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT