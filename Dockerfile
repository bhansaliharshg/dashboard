FROM python:3.11
EXPOSE 4200
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
CMD ["python3","manage.py", "runserver","127.0.0.1:4200"]