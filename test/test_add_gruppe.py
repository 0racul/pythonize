# -*- coding: utf-8 -*-
from model.group import Group



def test_add_gruppe(app):
    old_groups = app.group.get_group_list()
    app.group.create_group(Group("adasd", "fhggfh", "ewrwer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_gruppe(app):
    old_groups = app.group.get_group_list()
    app.group.create_group(Group("", "", ""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
