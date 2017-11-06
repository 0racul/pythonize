# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
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

