# -*- coding: utf-8 -*-

from pathlib import Path

import gitlabctl.config as config

__author__ = "Thomas Bianchi"
__copyright__ = "Thomas Bianchi"
__license__ = "mit"

CONTENT = """[gitTools]
url = https://ahahah.com
token = kkkkkk

"""


def test_save_config(tmp_path):
    config_file = Path.joinpath(tmp_path, "gitlabctl.ini")
    config_dict = {"name": "gitTools", "url": "https://ahahah.com", "token": "kkkkkk"}
    config.save(config_file, config_dict)
    assert config_file.read_text() == CONTENT


def test_read_config(tmp_path):
    config_file = Path.joinpath(tmp_path, "gitlabctl.ini")
    with open(config_file, "w") as f:
        f.write(CONTENT)
    config_dict = config.read(config_file, "gitTools")
    assert config_dict["url"] == "https://ahahah.com"
    assert config_dict["token"] == "kkkkkk"
