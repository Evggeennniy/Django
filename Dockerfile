FROM python:3.10

WORKDIR /app/build

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "app/manage.py", "runserver", "0.0.0.0:8000"]
