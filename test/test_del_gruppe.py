from model.group import Group


def test_del_first_gruppe(app):
    app.group.delete_first_group()

