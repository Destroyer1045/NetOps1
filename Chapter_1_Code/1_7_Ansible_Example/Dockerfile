# Pull base image
# FROM "quay.io/ansible/ansible-runner:stable-2.10-latest"
FROM "python:3.8.11-buster"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# fatal: [iosv-1]: FAILED! => {"msg": "paramiko: The authenticity of host 'x' can't be established."}
ENV ANSIBLE_HOST_KEY_CHECKING 0

# Set remote work directory 
WORKDIR /devops

# Install dependencies
COPY requirements.txt /devops/
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# Copy contents to remote instance 
COPY . /devops/

# Run Script
CMD ["ansible-playbook", "-i", "hosts", "backup_config_playbook.yml"]

