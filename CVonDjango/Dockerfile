FROM python:3-onbuild
WORKDIR /app
COPY . .

RUN python manage.py collectstatic

CMD ["python3", "manage.py"]