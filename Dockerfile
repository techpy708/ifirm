FROM python:3.11-slim-bullseye

WORKDIR /app

# Fix sources.list to use HTTPS before any apt-get update
RUN sed -i 's|http://deb.debian.org|https://deb.debian.org|g' /etc/apt/sources.list

# Now install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    netcat \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Optional if you use static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD /bin/sh -c "\
  echo 'Waiting for PostgreSQL at' \$POSTGRES_HOST; \
  until nc -z -v -w30 \$POSTGRES_HOST \$POSTGRES_PORT; do \
    echo 'Waiting for database connection...'; \
    sleep 3; \
  done; \
  echo 'Database is up'; \
  python manage.py makemigrations && \
  python manage.py migrate && \
  echo 'Creating superuser if not exists...' && \
  python manage.py shell -c \"from django.contrib.auth import get_user_model; User = get_user_model(); username = '$DJANGO_SUPERUSER_USERNAME'; password = '$DJANGO_SUPERUSER_PASSWORD'; email = '$DJANGO_SUPERUSER_EMAIL'; User.objects.filter(username=username).exists() or User.objects.create_superuser(username, email, password)\" && \
  python manage.py runserver 0.0.0.0:8000"