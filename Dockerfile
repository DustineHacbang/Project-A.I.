# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.11

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
RUN apt update -y
RUN apt-get install -y postgresql-client-common postgresql-client libpq-dev python3 python3-pip git


# create root directory for our project in the container


# Set the working directory to /project_x


# Copy the current directory contents into the container at /project_x
RUN mkdir /project_x 

COPY . /project_x/
WORKDIR /project_x
# install dependencies  
RUN pip install setuptools
RUN pip install -r requirements.txt
RUN pip install --upgrade pip --user
# Install any needed packages specified in requirements.txt

# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver 