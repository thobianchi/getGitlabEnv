# -*- coding: utf-8 -*-

from pathlib import Path

import gitlabctl.config as config

__author__ = "Thomas Bianchi"
__copyright__ = "Thomas Bianchi"
__license__ = "mit"


def test_save_config(tmp_path):
    CONTENT = """[gitTools]
url = https://ahahah.com
token = kkkkkk

"""
    config_file = Path.joinpath(tmp_path, "gitlabctl.ini")
    config_dict = {"name": "gitTools", "url": "https://ahahah.com", "token": "kkkkkk"}
    config.save(config_file, config_dict)
    assert config_file.read_text() == CONTENT
