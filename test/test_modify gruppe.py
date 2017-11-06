# -*- coding: utf-8 -*-
from model.group import Group





def test_modify_gruppe(app):
    app.group.open()
    app.group.modify_first_group(Group("[eqgbplfl;buehlf", "[eqgbplfl;buehlf", "[eqgbplfl;buehlf"))
