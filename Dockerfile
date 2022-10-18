# syntax=docker/dockerfile:1

FROM python:3.8.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /app_grupo7

WORKDIR /app_grupo7

COPY requirements.txt /app_grupo7/

RUN pip install -r requirements.txt

COPY . /app_grupo7/

RUN mkdir -p /app_grupo7/data

RUN python viajandoando/manage.py migrate

RUN python viajandoando/manage.py update_index --remove

CMD ["python","viajandoando/manage.py","runserver", "0.0.0.0:8000"]