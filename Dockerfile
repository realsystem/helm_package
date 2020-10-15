FROM ubuntu:xenial
RUN apt-get update && \
    apt-get install -y python-pip python-dev
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY backend/storage.py /app/app.py
ENTRYPOINT ["python"]
CMD ["app.py"]
