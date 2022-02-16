FROM ubuntu:latest

EXPOSE 8080

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install requests
RUN pip3 install singer-python==5.12.2
RUN pip3 install numpy
RUN pip3 install python-dotenv
RUN pip3 install setuptools
WORKDIR /usr/app/src
COPY jazzhr_tap ./
COPY app.py ./
RUN pip3 install -e .
RUN pip3 install target-stitch
RUN pip3 install flask
CMD python3 app.py