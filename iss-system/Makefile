NAME ?= costaki33

all: build run push

build:
	docker build -t ${NAME}/iss-data-pull:1.0 .

run:
	docker run --name "iss-data-pull" -d -p 5031:5000 ${NAME}/iss-data-pull:1.0

pull:
	docker pull ${NAME}/iss-data-pull:1.0

clean:
	docker ps -a | grep ${NAME}
