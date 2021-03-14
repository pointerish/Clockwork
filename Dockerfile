FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && apk add linux-headers \
  && pip install -r /requirements.txt \
  && apk del build-deps

RUN mkdir /app
COPY ./app /app
WORKDIR /app
COPY ./scripts /scripts
RUN chmod +x /scripts/*
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]