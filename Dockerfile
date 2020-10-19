FROM ubuntu:xenial
RUN apt-get update && \
    apt-get install -y python-pip python-dev
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY backend /app/
COPY main.py /app/main.py
ENTRYPOINT ["python"]
CMD ["main.py"]
