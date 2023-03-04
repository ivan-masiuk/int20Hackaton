FROM python:3.9

WORKDIR /code

COPY ./server/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./server /code


ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver", "0.0.0.0:8001"]
