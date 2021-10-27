import configparser
import os
import yaml
import requests


class Configuration(object):

    def __init__(self, filename=None, stream=None, data=None, parent_path=None):
        """
        init for the Configuration class

        :param filename:
        :param stream:
        :param data:
        :param parent_path:
        """
        if filename is not None:
            self.data = yaml.load(open(filename, encoding="utf-8"))
        elif stream is not None:
            self.data = yaml.load(stream)
        else:
            self.data = data
        if parent_path is None:
            self._parent_path = Configuration.NAMESPACE_ROOT
        else:
            self._parent_path = parent_path

    def __init__(self, env):
        self.users = None
        config = configparser.ConfigParser(allow_no_value=True)
        cwd = os.path.dirname(__file__)
        filename = cwd + '/config-auth.yaml'

        data = {}
        with open(filename) as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            data = yaml.load(file, Loader=yaml.FullLoader)

        self.base_uri = data[env]['base_uri']
        self.db_host = data[env]['db_host']
