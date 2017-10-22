# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_gruppe(app):
    app.session.login("admin", "secret")
    app.open_group_page()
    app.group_creation_init()
    app.fill_group_fields(Group("y", "bh", "bh"))
    app.session.logout()

def test_add_empty_gruppe(app):
    app.session.login("admin", "secret")
    app.open_group_page()
    app.group_creation_init()
    app.fill_group_fields(Group("", "", ""))
    app.session.logout()

