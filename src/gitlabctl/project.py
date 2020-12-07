# -*- coding: utf-8 -*-

__author__ = "Thomas Bianchi"
__copyright__ = "Thomas Bianchi"
__license__ = "mit"


def get_env(client, id):
    client.get_project_env(id)
