# -*- coding: utf-8 -*-

from pathlib import Path

import pytest

from gitlabctl.config import Config

__author__ = "Thomas Bianchi"
__copyright__ = "Thomas Bianchi"
__license__ = "mit"

CONTENT = """[DEFAULT]
current-context = gitTools

[gitTools]
url = https://ahahah.com
token = kkkkkk

"""

CONTENT2 = """[gitTools]
url = https://ahahah.com
token = kkkkkk
"""

CONTENT3 = """[DEFAULT]
current-context = gitTools
[gitTools]
url = https://ahahah.com
token = kkkkkk
[another]
url = https://ssss.com
token = sss
"""


def write_config_example(tmp_path, content):
    config_file = Path.joinpath(tmp_path, "gitlabctl.ini")
    with open(config_file, "w") as f:
        f.write(content)
    return config_file


test_read_config_expections = [
    pytest.param(CONTENT, {
             'url': 'https://ahahah.com',
             'context': 'gitTools',
             'token': 'kkkkkk'
             }, id='single-section'),
    pytest.param(CONTENT3, {
             'url': 'https://ahahah.com',
             'context': 'gitTools',
             'token': 'kkkkkk'
             }, id='multiple-sections'),
    pytest.param(CONTENT2, None, id='no-current'),
]


@pytest.mark.parametrize("a,expected", test_read_config_expections)
def test_read_config(tmp_path, a, expected):
    config_file = write_config_example(tmp_path, a)
    cfg = Config(filepath=config_file)
    # Config is a singleton, reinitialize for testing porpuses
    cfg.__init__(filepath=config_file)
    info = cfg.get_config()
    print("info:", info)
    assert info == expected


def test_set_context(tmp_path):
    cfg = Config(filepath=Path.joinpath(tmp_path, "gitlabctl.ini"))
    cfg.__init__(filepath=Path.joinpath(tmp_path, "gitlabctl.ini"))
    cfg.set_context('testSet', 'https://lll', 'eeeee')
    assert 'testSet' in cfg.config.sections()
    assert cfg.config['testSet']['url'] == 'https://lll'
    assert cfg.config['testSet']['token'] == 'eeeee'


def test_set_current_context(tmp_path):
    cfg = Config(filepath=Path.joinpath(tmp_path, "gitlabctl.ini"))
    cfg.__init__(filepath=Path.joinpath(tmp_path, "gitlabctl.ini"))
    cfg.set_current_context('currcontextA')
    assert cfg._get_current_context() == 'currcontextA'
    assert cfg.config['DEFAULT']['current-context'] == 'currcontextA'


def test_not_existing(tmp_path):
    cfg = Config(filepath=Path.joinpath(tmp_path, "NonEsiste"))
    cfg.__init__(filepath=Path.joinpath(tmp_path, "NonEsiste"))
    assert not cfg.get_config()


def test_save(tmp_path):
    test_file = Path.joinpath(tmp_path, "gitlabctl.ini")
    cfg = Config(filepath=test_file)
    cfg.__init__(filepath=test_file)
    cfg.config.read_string(CONTENT)
    cfg.save()
    with open(test_file) as f:
        assert f.read() == CONTENT
