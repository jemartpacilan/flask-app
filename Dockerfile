FROM python:3.7.2-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add libpq

RUN apk --no-cache add --virtual .build-deps \
  g++ gcc libgcc libstdc++ linux-headers make \
  libffi libffi-dev postgresql-dev musl-dev python3-dev

RUN pip install pipenv

RUN adduser -D irithm

WORKDIR /home/irithm

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system

RUN apk del .build-deps

COPY app app
COPY migrations migrations
COPY config.py manage.py docker-entrypoint.sh ./
RUN chmod +x ./docker-entrypoint.sh

ENV FLASK_APP irithm.py

RUN chown -R irithm:irithm ./
USER irithm

ENTRYPOINT ["./docker-entrypoint.sh"]