######
# Image for compile uwsgi
# ####
FROM python:3.9.9-bullseye AS compile-image

RUN apt-get install -y gcc

WORKDIR /app

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip3 install -r requirements.txt

######
# Image for runtime
# ####
FROM python:3.9.9-alpine

# Working dir
RUN mkdir /app

# Create a user to run the service
RUN addgroup -S uwsgi
RUN adduser -H -D -S uwsgi
USER uwsgi

# copy from compile-image dependencies
COPY --chown=uwsgi:uwsgi --from=compile-image /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

# copy project
COPY --chown=uwsgi:uwsgi ./stat_backend/* /app/
WORKDIR /app
EXPOSE 5000
CMD ["uwsgi", "--ini", "/app/wsgi.ini"]
