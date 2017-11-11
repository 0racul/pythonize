from model.contact import Contact
from random import randrange



def test_del_first_contact(app):
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
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

