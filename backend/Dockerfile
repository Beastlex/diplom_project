FROM python:3.9.9-slim

# Working dir
WORKDIR /app

# set environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install dependencies
COPY requiements.txt .
RUN pip install -r requiements.txt

# copy project
COPY ./stat_backend/* .
EXPOSE 5000
CMD ["uwsgi", "--ini", "/app/wsgi.ini"]
