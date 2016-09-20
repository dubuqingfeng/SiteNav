FROM centos:7
MAINTAINER Dubu Qingfeng <1135326346@qq.com>

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install python-pip; yum clean all
RUN yum -y group install "Development Tools"
RUN yum -y install python-virtualenv; yum clean all

ADD . /src

RUN cd /src; pip install -r requirements.txt

ENV USERNAME admin
ENV PASSWORD c33ba20b52f8aa5a8699deee49b54218

ENV MONGODB_USER user
ENV MONGODB_PASS mypass
ENV MONGODB_PORT_27017_TCP_ADDR 192.168.100.100
ENV MONGODB_PORT_27017_TCP_PORT 27017

EXPOSE 80

CMD ["python", "/src/app.py"]