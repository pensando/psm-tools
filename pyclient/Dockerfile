from ubuntu:20.04

RUN apt update
RUN apt install -y git python3 make python3-distutils curl
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
RUN rm get-pip.py
# RUN git clone https://github.com/pensando/psm-tools.git
ADD ./requirements.txt /pyclient/requirements.txt
WORKDIR pyclient
RUN pip install -r requirements.txt

ENV DEBIAN_FRONTEND=noninteractive
RUN apt install -y default-jdk maven
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PYTHONPATH=/pyclient

COPY bin/openapi-generator-cli.jar /opt/openapi-generator-cli.jar

CMD ["echo", "Hello World!"]
