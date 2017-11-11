import re



def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.hometele == clear(contact_from_edit_page.hometele)
    assert contact_from_home_page.worktele == clear(contact_from_edit_page.worktele)
    assert contact_from_home_page.mobiletele == clear(contact_from_edit_page.mobiletele)
    assert contact_from_home_page.phone2 == clear(contact_from_edit_page.phone2)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.hometele == contact_from_edit_page.hometele
    assert contact_from_view_page.worktele == contact_from_edit_page.worktele
    assert contact_from_view_page.mobiletele == contact_from_edit_page.mobiletele
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def test_all_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_phones()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)




def clear(s):
    return re.sub(" [ ()-]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda  x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.hometele, contact.worktele, contact.mobiletele, contact.phone2]))))