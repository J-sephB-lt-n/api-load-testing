# gunicorn-concurrency-optimisation
Exploring optimal settings for concurrent requests using Python + Gunicorn + Flask

```bash
# start local gunicorn server in background
gunicorn \
--bind :5000 \
--workers 1 \
--threads 8 \
--timeout 10 \
--access-logfile "-" \
--log-level info \
flask_app:app &

locust

# stop gunicorn server #
GUNICORN_PID=$(pgrep -f "gunicorn .* flask_app:app")
kill -15 $GUNICORN_PID
```