# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.contact_creation(contact)
    new_contacts = db.get_contact_list()
    contact[id] = app.contact.get_last_contact_id()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)







