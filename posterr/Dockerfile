FROM python:3.10-buster

RUN apt-get install libpq-dev

COPY src posterr/src/
COPY requirements.txt posterr/requirements.txt

WORKDIR posterr/
RUN pip install -r requirements.txt

EXPOSE 8888

#CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "python:src.wsgi", "src:app"]
CMD ["python3", "-m", "src"]