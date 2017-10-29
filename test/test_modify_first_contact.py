# -*- coding: utf-8 -*-
from model.contact import Contact



def test_modify_first_contact(app):
    app.session.login("admin","secret")
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
