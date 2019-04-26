# Use an official debian sid as a parent image
FROM debian:sid
# add PSU repository
RUN echo "deb http://ftp.sg.debian.org/debian/ sid " \
 "main contrib non-free" > /etc/apt/sources.list
# Update and Upgrade system then install python3
RUN apt update && apt upgrade -y
RUN apt install -y python3 python3-dev python3-pip nodejs npm

RUN npm install -g yarn vue @vue/cli

# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org flask
RUN pip3 install --trusted-host pypi.python.org -r server/requirements.txt
RUN cd server; python3 setup.py install

RUN cd /app/client; yarn install
