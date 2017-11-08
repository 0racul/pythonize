# -*- coding: utf-8 -*-
from model.contact import Contact



def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.contact_creation((Contact(   firstname = "123",
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
                                                 notes = "123")))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(               firstname = "666",
                                     middlename = "666",
                                     lastname = "666",
                                     nickname = "666",
                                     title = "666",
                                     company = "666",
                                     address = "666",
                                     hometele = "666",
                                     mobiletele = "666",
                                     worktele = "666",
                                     faxtele = "666",
                                     email = "666",
                                     email2 = "666",
                                     email3 = "666",
                                     homepage = "666",
                                     secondaryaddress = "666",
                                     homesecondaryaddress = "666",
                                     notes = "666")
    contact.id = old_contacts[0].id
    app.contact.update_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

