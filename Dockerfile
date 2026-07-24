FROM python:3.10
WORKDIR /student-info-app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]


