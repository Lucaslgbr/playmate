FROM python:3.10
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

RUN chown root -R /code

RUN pip install --upgrade pip

COPY ./requirements ./requirements

RUN pip install --default-timeout=100 -r requirements/prod.txt -r requirements/prod.txt 

COPY . .
