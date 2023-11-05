# Get the base image
FROM python:3.11-bullseye

# Apt update
RUN apt update

# Install git
RUN apt update && apt install -y git

# Install geckodriver dependencies
# RUN apt install libgtk-3-0 libdbus-glib-1-2 xvfb libasound2 -y

# Install pipenv
RUN pip install -U pipenv

# Make a temporary directory for the pipenv
RUN mkdir /tmp/pipenv

# Set the working directory
WORKDIR /tmp/pipenv

# Install pipenv requirements
COPY Pipfile Pipfile.lock /tmp/pipenv/
RUN pipenv install

# Remove the temporary directory
RUN rm -rf /tmp/pipenv

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1