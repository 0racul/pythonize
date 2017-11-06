from model.group import Group


def test_del_first_gruppe(app):
    if app.group.count() == 0:
        app.group.create_group(Group("test_group"))
    app.group.delete_first_group()

