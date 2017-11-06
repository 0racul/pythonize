# -*- coding: utf-8 -*-
from model.group import Group





def test_modify_gruppe(app):
    app.group.open()
    if app.group.count() == 0:
        app.group.create_group(Group("test_group"))
    app.group.modify_first_group(Group("[eqgbplfl;buehlf", "[eqgbplfl;buehlf", "[eqgbplfl;buehlf"))
