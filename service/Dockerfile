FROM python:3.12-alpine

WORKDIR /service

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY .. .

EXPOSE 8000

ENTRYPOINT ["python", "main.py"]