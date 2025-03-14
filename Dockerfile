FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY .env requirements.txt ./
RUN pip3 install -r requirements.txt

COPY ./src ./src

EXPOSE 8000
