NAME=lilly-telegram
BOTTOKEN=$(BOT_TOKEN)

all: gen-proto

install:
	pip install -r requirements.txt

docker-build:
	docker build -t $(NAME) .

docker-run: docker-build
	docker run --name $(NAME) -e BOT_TOKEN=$(BOTTOKEN)  -itd $(NAME)

docker-stop:
	docker stop $(NAME)

docker-rm: docker-stop
	docker rm $(NAME)

gen-proto:
	python -m grpc_tools.protoc -I./proto/ --python_out=. --grpc_python_out=. src/grpc/pb/message.proto
	python -m grpc_tools.protoc -I./proto/ --python_out=. --grpc_python_out=. src/grpc/pb/file.proto
