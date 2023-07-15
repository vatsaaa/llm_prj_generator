FROM centos:latest

LABEL MAINTAINER="Ankur Vatsa"
LABEL GitHub="https://github.com/vatsaaa"
LABEL version="1.0"
LABEL description="A Docker container to serve Python API for {{cookiecutter.project_slug}}"

WORKDIR /app
COPY . /app

RUN cd /etc/yum.repos.d/ && sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* && sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
RUN yum upgrade -y && yum && yum install python3.9 -y && pip3 install --upgrade pip && yum install firefox -y && pip3 install -r requirements.txt

CMD ["python3", "app.py", "-h"]
