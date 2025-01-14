
FROM python:3.9-slim

ENV APP_HOME /app
ENV GOOGLE_APPLICATION_CREDENTIALS="${APP_HOME}/firebase_credentials.json"
ENV PORT 8000

WORKDIR $APP_HOME

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE $PORT

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
