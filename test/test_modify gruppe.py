# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange





def test_modify_gruppe(app, db):
    app.group.open()
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))

    if app.group.count() == 0:
        app.group.create_group(Group("test_group"))

    group = Group("[eqgbplfl;buehlf", "[eqgbplfl;buehlf", "[eqgbplfl;buehlf")
    group.id = old_groups[index].id

    app.group.modify_group_by_id(group.id, group)

    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()


    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
