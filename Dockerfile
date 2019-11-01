FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV TZ Europe/Kiev

COPY ./app /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
