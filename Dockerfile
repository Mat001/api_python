FROM ubuntu:latest
MAINTAINER Matjaz Pirnovar
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . .
WORKDIR /
RUN pip3 install -r requirements.txt
CMD ["python3", "-W", "ignore", "-m", "unittest", "discover"]