from dotenv import load_dotenv
import os


load_dotenv()


class Env:
    def __init__(self):
        self.host = os.getenv("HOST")
        self.port = os.getenv("PORT")
        self.sio_api = os.getenv("SIO_API")


env = Env()
