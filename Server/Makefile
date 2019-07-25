all: gen-proto

install:
	pip install -r requirements.txt

docker-build:
	docker build -t lilly-server .

docker-run: docker-build
	docker run --name lilly-server-p 50051:50051 -itd lilly-server

docker-stop:
	docker stop lilly-server

docker-rm: docker-stop
	docker rm lilly-server

gen-proto:
	python -m grpc_tools.protoc -I./proto/ --python_out=. --grpc_python_out=. src/grpc/pb/message.proto
	python -m grpc_tools.protoc -I./proto/ --python_out=. --grpc_python_out=. src/grpc/pb/file.proto