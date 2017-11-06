# -*- coding: utf-8 -*-
from model.group import Group



def test_add_gruppe(app):
    app.group.open()
    app.group.creation_init()
    app.group.fill_fields(Group("y", "bh", "bh"))
    app.group.submit()
    app.group.return_to()

def test_add_empty_gruppe(app):
    app.group.open()
    app.group.creation_init()
    app.group.fill_fields(Group("", "", ""))
    app.group.submit()
    app.group.return_to()

