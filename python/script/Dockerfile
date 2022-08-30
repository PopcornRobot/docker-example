FROM python:3.10.6-slim-buster

# set work directory
WORKDIR /app

# set environment variables, does not have to be in Dockerfile, can be set within container
ENV TEST_VARIABLE 'this is a test environment variable'

# copy content into container
COPY . .

# run command
CMD python sample.py