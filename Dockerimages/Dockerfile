FROM ubuntu:latest

ENV NAME jovyan

RUN apt update
RUN apt install python3 -y
RUN pip install boto3

WORKDIR /home/$NAME

COPY downloadscript.py ./

CMD [ "python3", "./downloadscript.py"]

