# Pull base image
FROM python:3.8.11-buster

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

# Set remote work directory 
WORKDIR /devops

# Install dependencies
COPY requirements.txt /devops/
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# Copy contents to remote instance 
COPY . /devops/

# Run Script
CMD ["python", "show_version.py"]

