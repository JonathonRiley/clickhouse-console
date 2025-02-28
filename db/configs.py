import os
import shelve
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Config:
    host: str= "localhost"
    port: int = 8123
    username: str = "default"
    password: str = ""

class DBConfig:
    def __init__(self):
        self.db_path = os.path.join(Path(__file__).parent.resolve(), "db_configs")
        self.db = shelve.open(self.db_path, writeback=True)

    def add(self, name:str, host:str=None, port:int=None, username:str=None, password:str=None):
        if port is None and username is None and password is None:
            config = Config()
        elif all([host, port, username, password]):
            config = Config(host, port, username, password)
        else:
            raise ValueError("Incomplete database configuration data provided.")
        self.db[name] = config
        self.db.sync()

    def update(self, name:str, config:Config):
        self.db[name] = config
        self.db.sync()

    def remove(self, name:str):
        del self.db[name]
        self.db.sync()

    def get_config(self, name:str) -> Config:
        config = self.db.get(name)
        if config is None:
            raise ValueError(f"No configuration found for {name}.")
        return config
