# -*- coding: utf-8 -*-
from model.group import Group



def test_add_gruppe(app):
    app.group.create_group(Group("adasd", "fhggfh", "ewrwer"))

def test_add_empty_gruppe(app):
    app.group.create_group(Group("", "", ""))

