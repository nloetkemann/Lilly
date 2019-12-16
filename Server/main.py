import os

from src.grpc.server import Server

if __name__ == '__main__':
    if os.getenv("WIT_TOKEN") and os.getenv("WEATHER_TOKEN") and os.getenv("WOLFRAM_TOKEN"):
        print("Starte Server")
        server = Server()
        server.start()
    else:
        print("Es fehlen die Token")
        print("Flieht ihr Narren")
