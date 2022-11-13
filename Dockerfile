FROM python:3.10

WORKDIR /app/build

ENV PYTHONPATH /app/build/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

#CMD ["python3", "app/manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "settings.wsgi", "--threads", "4", \
    "--workers", "9", "--log-level", "bedug", "--max-requests", \
    "1", "--timeout", "10", "--bind=0.0.0.0:8000"]