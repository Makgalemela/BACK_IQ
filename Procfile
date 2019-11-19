web: gunicorn Channels.wsgi --log-file -
worker: python manage.py celery worker -B -l info
web2: daphne  Channels.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker2: python manage.py runworker --only-channels=http.* --only-channels=websocket.*
release: python manage.py migrate --noinput
