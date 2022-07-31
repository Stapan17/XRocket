FROM python:3.8

WORKDIR /code

COPY . /code/

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "--workers", "3", "project.wsgi:application"]
