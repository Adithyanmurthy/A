FROM python:3.11-slim
WORKDIR /app
COPY a.py .
RUN pip install flask
CMD ["python", "a.py"]