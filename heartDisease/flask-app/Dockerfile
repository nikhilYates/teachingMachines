FROM python:3.11.7-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV NAME Heart

CMD ["python3", "heart-disease-web.py"]
