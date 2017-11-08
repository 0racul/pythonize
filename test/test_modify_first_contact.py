# -*- coding: utf-8 -*-
from model.contact import Contact



def test_modify_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.contact_creation((Contact(firstname = "123",
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

    app.contact.init_edit_first_contact()
    app.contact.fill_contact_fields(Contact(firstname = "666",
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
                                     notes = "666"))
    app.contact.submit_updating()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
