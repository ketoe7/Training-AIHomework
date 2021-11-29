FROM python:3.9-alpine

LABEL version="1.0" \
      maintener="Mikołaj Wierzbicki"

RUN apk update
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]