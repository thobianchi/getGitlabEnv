# -*- coding: utf-8 -*-

import configparser
import logging
from pathlib import Path

__author__ = "Thomas Bianchi"
__copyright__ = "Thomas Bianchi"
__license__ = "mit"

CONFIG_PATH = Path.home()
CONFIG_NAME = "gitlabctl.ini"

_logger = logging.getLogger(__name__)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls). \
                __call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    def __init__(self, filepath=Path.joinpath(CONFIG_PATH, CONFIG_NAME)):
        self.filepath = filepath
        self.config = configparser.ConfigParser()
        self._read(filepath)

    def _read(self, filepath):
        self.config.read(filepath)
        return self.config

    def save(self):
        with open(self.filepath, 'w') as configfile:
            self.config.write(configfile)

    def set_current_context(self, context):
        self.config['DEFAULT'] = {'current-context': context}

    def _get_current_context(self):
        return self.config.get('DEFAULT', 'current-context', fallback=None)

    def get_config(self):
        ctx = self._get_current_context()
        if ctx:
            return {
                    'context': ctx,
                    'url': self.config.get(ctx, 'url'),
                    'token': self.config.get(ctx, 'token')
                    }
        return None

    def set_context(self, context, url, token):
        self.config[context] = {
                                'url': url,
                                'token': token
                                }
