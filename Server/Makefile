all: gen-proto

install:
    pip install -r requirements.txt

gen-proto:
    python -m grpc_tools.protoc -I./proto/ --python_out=. --grpc_python_out=. src/grpc/pb/message.proto
    python -m grpc_tools.protoc -I./proto/ --python_out=. --grpc_python_out=. src/grpc/pb/file.proto