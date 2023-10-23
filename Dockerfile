FROM python:3.10.13-alpine
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python3"]
CMD ["./main.py"]