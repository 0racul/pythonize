# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login("admin","secret")
    app.contact.contact_creation(Contact(firstname = "123",
                                         middlename = "123",
                                         lastname = "123",
                                         nickname = "123",
                                         title = "123",
                                         company = "123",
                                         address = "123",
                                         hometele = "123",
                                         mobiletele = "123",
                                         worktele = "123",
                                         faxtele = "123",
                                         email = "123",
                                         email2 = "123",
                                         email3 = "123",
                                         homepage = "123",
                                         secondaryaddress = "123",
                                         homesecondaryaddress = "123",
                                         notes = "123"))
    app.session.logout()
