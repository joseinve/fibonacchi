FROM python:3.11.4-alpine

WORKDIR /app

COPY *.py .

ENTRYPOINT ["python"]
CMD ["main.py"]
