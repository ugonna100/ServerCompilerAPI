# Starting dockerfile
FROM ubuntu

RUN apt-get update
RUN apt-get install gcc -y
RUN apt-get install openjdk-8-jdk -y
RUN apt-get install g++ -y
RUN apt-get install python3 -y
RUN apt-get install python3-flask -y

EXPOSE 5000

COPY main.py main.py
COPY code.java code.java

ENV NAME World

CMD ["python3", "main.py"]