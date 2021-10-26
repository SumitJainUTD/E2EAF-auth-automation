import configparser

import requests


class Configuration(object):
    def __init__(self, env):
        self.users = None
        config = configparser.ConfigParser(allow_no_value=True)
        config.read('../E2EAF_auth_automation/resources/config-auth.cfg')

        section = 'QA'
        if env == 'qa':
            section = 'QA'
        elif env == 'staging':
            section = 'STAGING'

        self.base_uri = config.get(section=section, option='base_uri')
        self.db_host = config.get(section=section, option='db_host')
