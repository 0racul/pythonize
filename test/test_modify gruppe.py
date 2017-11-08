# -*- coding: utf-8 -*-
from model.group import Group





def test_modify_gruppe(app):
    app.group.open()
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create_group(Group("test_group"))
    app.group.modify_first_group(Group("[eqgbplfl;buehlf", "[eqgbplfl;buehlf", "[eqgbplfl;buehlf"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

