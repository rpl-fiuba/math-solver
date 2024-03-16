FROM python:3.9.18-alpine
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD [ "gunicorn", "--env", "DJANGO_SETTINGS_MODULE=mathlearning.settings", "mathlearning.wsgi", "--workers=1", "--bind=0.0.0.0:5000" ]