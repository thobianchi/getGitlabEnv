# -*- coding: utf-8 -*-

__author__ = "Thomas Bianchi"
__copyright__ = "Thomas Bianchi"
__license__ = "mit"


def get_all_parents_ids(client, id):
    """
    returns a list of ids of all parents groups from project id
    """
    project = client.get_project_by_id(id)
    parent_id = project.namespace.get('id')
    ids = [parent_id]
    while True:
        group = client.get_group_by_id(parent_id)
        if not group.parent_id:
            break
        parent_id = group.parent_id
        ids.append(parent_id)
    return ids


def get_env(client, id):
    # client.get_project_env(id)
    ids = get_all_parents_ids(client, id)
    print("ids", ids)
