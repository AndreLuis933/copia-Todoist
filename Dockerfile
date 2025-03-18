FROM python:3-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src ./src

EXPOSE 8000

CMD ["python", "src/main.py"]