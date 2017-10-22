# -*- coding: utf-8 -*-
from group import Group
import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def add_gruppe(app):
    app.login("admin", "secret")
    app.open_group_page()
    app.group_creation_init()
    app.fill_group_fields(Group("y", "bh", "bh"))
    app.logout()

def add_empty_gruppe(app):
    app.login("admin", "secret")
    app.open_group_page()
    app.group_creation_init()
    app.fill_group_fields(Group("", "", ""))
    app.logout()

