# Get the base image
FROM python:3.11-bullseye

# Apt update
RUN apt update

# Install pipenv
RUN pip install -U pipenv

# Make a directory for the app
RUN mkdir /app

# Set the working directory
WORKDIR /app

# Install pipenv requirements
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set the entrypoint
ENTRYPOINT ["/entrypoint_backend.sh"]

# Copy all files
COPY . /app/

# Make the entrypoint scripts executable
RUN chmod +x /app/entrypoint_backend.sh
RUN chmod +x /app/entrypoint_celery_worker.sh
RUN chmod +x /app/entrypoint_celery_beat.sh

