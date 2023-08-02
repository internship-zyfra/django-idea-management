FROM python:3.11-bookworm

RUN apt install -y libpq-dev

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt /temp/requirements.txt

RUN pip install --upgrade pip; pip install  -r /temp/requirements.txt

RUN adduser --disabled-password idea-user
USER idea-user

COPY idea_management /idea_management
WORKDIR /idea_management

EXPOSE 8000