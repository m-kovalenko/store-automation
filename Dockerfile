FROM python:3.9.5-slim


WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt --no-deps

COPY src /app/src

RUN chmod +x /app/src/main.py

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0"]
