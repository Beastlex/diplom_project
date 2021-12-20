######
# Image for compile uwsgi
# ####
FROM python:3.9.9-slim-bullseye AS compile-image

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install system dependencies
RUN apt-get update && \
      apt-get install -y --no-install-recommends gcc
RUN pip install --upgrade pip
# todo lint and maybe

COPY stat_backend/ /app/

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

######
# Image for runtime
# ####
FROM python:3.9.9-slim-bullseye

# Working dir
RUN mkdir /app

# Create a user to run the service
RUN addgroup --system app && adduser --system --group app

# copy from compile-image dependencies
COPY --chown=app:app --from=compile-image /app/wheels /app/wheels
COPY --chown=app:app --from=compile-image /app/requirements.txt /app/
RUN pip install --no-cache /app/wheels/*

# copy project
COPY --chown=app:app ./stat_backend/ /app/
RUN chown -R app:app /app
WORKDIR /app
EXPOSE 5000
USER app
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:create_app()"]
