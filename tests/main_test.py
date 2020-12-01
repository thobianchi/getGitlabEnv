# -*- coding: utf-8 -*-

import logging

import pytest

from gitlabctl.main import parse_args

__author__ = "Thomas Bianchi"
__copyright__ = "Thomas Bianchi"
__license__ = "mit"


testdata_logging = [
    (["-v"], logging.INFO),
    (["-vv"], logging.DEBUG),
    (["--very-verbose"], logging.DEBUG),
    (["-v", "-vv"], logging.DEBUG),
]


@pytest.mark.parametrize("a,expected", testdata_logging)
def test_parsing_loglevel(a, expected):
    args = a
    args = parse_args(args)
    assert args.loglevel == expected
