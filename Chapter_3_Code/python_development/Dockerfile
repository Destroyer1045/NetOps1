# Pull base image
FROM python:3.8.11-buster

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

# Set remote work directory 
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# Copy contents to remote instance 
COPY . /code/

# Run Script
CMD ["python", "main.py"]
