import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class Env:
    endpoint: str


def load_env(path: str = ".env"):
    load_dotenv(path)
    return Env(
        endpoint=os.getenv("ENDPOINT"),
    )
