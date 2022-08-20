FROM python:3.10.0
COPY . /app
RUN ls -l
WORKDIR /app
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install -r requirements.txt
WORKDIR /app/
RUN /opt/venv/bin/python manage.py collectstatic  --noinput
CMD /opt/venv/bin/gunicorn django_shopping_api.wsgi:application --bind "0.0.0.0:8080"
EXPOSE 8080