import configparser
import os
import yaml
import requests


class Configuration(object):

    def __init__(self, env):
        self.users = None
        cwd = os.path.dirname(__file__)
        filename = cwd + '/config-auth.yaml'

        data = {}
        with open(filename) as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            data = yaml.load(file, Loader=yaml.FullLoader)

        self.base_uri = data[env]['base_uri']
        self.db_host = data[env]['db_host']
