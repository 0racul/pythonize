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

