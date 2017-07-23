# Starting dockerfile
FROM ubuntu

RUN apt-get update
RUN apt-get install gcc -y
RUN apt-get install openjdk-8-jdk -y
RUN apt-get install g++ -y
RUN apt-get install python3 -y

EXPOSE 5000

COPY main.py main.py
COPY get-pip.py get-pip.py

RUN python3 get-pip.py
RUN pip3 install flask
RUN pip3 install flask-cors

ENV NAME World

CMD ["python3", "main.py"]