from model.group import Group


def test_del_first_gruppe(app):
    if app.group.count() == 0:
        app.group.create_group(Group("test_group"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert len(old_groups) == len(new_groups)

