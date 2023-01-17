FROM python:3.9.16-slim

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

CMD ["uvicorn","main:app","--reload"]
