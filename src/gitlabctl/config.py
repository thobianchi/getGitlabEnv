# -*- coding: utf-8 -*-

import configparser
import logging
from pathlib import Path

__author__ = "Thomas Bianchi"
__copyright__ = "Thomas Bianchi"
__license__ = "mit"

CONFIG_PATH = str(Path.home())
CONFIG_NAME = "gitlabctl.ini"

config = configparser.ConfigParser()
_logger = logging.getLogger(__name__)


def save(filepath, config_dict):
    config[config_dict["name"]] = {
        "url": config_dict["url"],
        "token": config_dict["token"]
    }
    with open(filepath, 'w') as configfile:
        config.write(configfile)


def read(filepath, section_name):
    config.read(filepath)
    config_dict = {"name": section_name, "url": config[section_name]["url"],
                   "token": config[section_name]["token"]}
    _logger.debug("config_dict: {}".format(config_dict))
    return config_dict
