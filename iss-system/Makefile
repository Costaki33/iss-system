NAME ?= costaki33

all: build run push

build:
	docker build -t ${NAME}/iss-data-query:1.1 .

run:
	docker run --name "iss-query-data" -d -p 5038:5000 ${NAME}/iss-data-query:1.1

pull:
	docker pull ${NAME}/iss-data-query:1.1

clean:
	docker ps -a | grep ${NAME}
