# get official base image of python from docker hub
FROM python:3.11

# set up environment
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set up working directory
WORKDIR /code

# install dependencies
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y libpcre3 libpcre3-dev
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY Words_counter /code