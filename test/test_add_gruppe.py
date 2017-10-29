# -*- coding: utf-8 -*-
from model.group import Group



def test_add_gruppe(app):
    app.session.login("admin", "secret")
    app.group.open()
    app.group.creation_init()
    app.group.fill_fields(Group("y", "bh", "bh"))
    app.session.logout()

def test_add_empty_gruppe(app):
    app.session.login("admin", "secret")
    app.group.open()
    app.group.creation_init()
    app.group.fill_fields(Group("", "", ""))
    app.session.logout()

