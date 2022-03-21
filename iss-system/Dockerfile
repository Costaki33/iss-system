FROM python:3.9

RUN mkdir /iss-system
WORKDIR /iss-system
COPY requirements.txt /iss-system/requirements.txt
RUN pip3 install -r /iss-system/requirements.txt 
COPY . /iss-system

ENTRYPOINT ["python"]
CMD ["iss-system-app.py"]
