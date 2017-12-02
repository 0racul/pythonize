from model.contact import Contact
import random
import time



def test_del_some_contact(app, db):
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
                                              phone2="123",
                                              notes = "123")))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

