# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + (" " * 10)
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
           Contact(firstname=firstname,
                   middlename=middlename,
                   lastname=lastname,
                   nickname=nickname,
                   title=title,
                   company=company,
                   address=address,
                   hometele=hometele,
                   worktele=worktele,
                   faxtele=faxtele,
                   email=email,
                   email2=email2,
                   email3=email3,
                   homepage=homepage,
                   secondaryaddress=secondaryaddress,
                   phone2=phone2,
                   notes=notes)
    for firstname in ["", random_string("firstname", 10)]
    for middlename in ["", random_string("middlename", 10)]
    for lastname in ["", random_string("lastname", 10)]
    for nickname in ["", random_string("nickname", 10)]
    for title in ["", random_string("title", 10)]
    for company in ["", random_string("company", 10)]
    for address in ["", random_string("address", 10)]
    for hometele in ["", random_string("hometele", 10)]
    for mobiletele in ["", random_string("mobiletele", 10)]
    for worktele in ["", random_string("worktele", 10)]
    for faxtele in ["", random_string("faxtele", 10)]
    for email in ["", random_string("email", 10)]
    for email2 in ["", random_string("email2", 10)]
    for email3 in ["", random_string("email3", 10)]
    for homepage in ["", random_string("homepage", 10)]
    for secondaryaddress in ["", random_string("secondaryaddress", 10)]
    for phone2 in ["", random_string("phone2", 10)]
    for notes in ["", random_string("notes", 10)]]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.contact_creation(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



