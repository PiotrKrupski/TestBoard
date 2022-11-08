from configparser import ConfigParser
import os


class ConfigManager:

    def __init__(self):

        self.config = ConfigParser()

    @property
    def config_filename(self, config_filename="config"):
        return f"{config_filename}.ini"

    @property
    def config_filepath(self):
        return f"{os.path.abspath(os.getcwd())}{os.path.sep}{self.config_filename}.ini"

    @property
    def config_presence(self):
        return os.path.isfile(self.config_filepath)

    def create_config(self, config_name="DEFAULT", **kwargs):
        if self.config_presence:
            raise FileExistsError(f"\n{self.config_filepath} already exists\n Update ini file instead")
        else:
            self.config[config_name] = {}
            for key, value in kwargs.items():
                self.config[config_name].update({key: value})

    def save_config(self):
        if self.config_presence:
            raise FileExistsError(f"\n{self.config_filepath} already exists\n Update ini file instead")
        else:
            with open(self.config_filepath, "w") as f:
                self.config.write(f)

    def update_config(self):
        pass


if __name__ == "__main__":
    config = ConfigManager()
    config.create_config(username="Piotr", password="admin")
    config.save_config()
