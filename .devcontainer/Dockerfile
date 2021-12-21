FROM python:3.8-slim

WORKDIR /home/
RUN apt update &&\
    apt install -y make curl zip groff

# aws cliインストール
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" &&\
    unzip awscliv2.zip &&\
    ./aws/install

WORKDIR /home/root