FROM centos:7.9.2009

RUN yum update -y && \
    yum install -y python3

RUN pip3 install pytest==7.0.0
RUN pip3 install --user xmltodict
RUN pip3 install --user Flask==2.0.3

RUN mkdir /iss_system
WORKDIR /iss_system

COPY iss_system_app.py /iss_system
COPY XMLsightingData_citiesUSA10.xml /iss_system
COPY ISS.OEM_J2K_EPH.xml /iss_system
COPY pytest-iss-app.py /iss_system

ENTRYPOINT ["python3"]
CMD ["iss_system_app.py"]
