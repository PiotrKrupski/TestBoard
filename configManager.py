from configparser import ConfigParser
import os

class ConfigManager:

    def __init__(self):
        self.config = ConfigParser()

    def create_default(self):
        self.config["DEFAULT"] = {
            "firstUsage": "",
            "username": "",
            "password": ""}

    # def append_config

    def update_config(self):
        with open(f"{os.path.abspath(os.getcwd())}{os.path.sep}config.ini", "w") as f:
            self.config.write(f)



if __name__ == "__main__":
    config = ConfigManager()
    config.create_default()
    config.update_config()
