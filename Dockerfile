FROM python:3.11-alpine
RUN apk add --no-cache py3-pip gcc python3-dev musl-dev mariadb-dev

WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]