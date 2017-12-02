from model.group import Group






def test_group_list(app, db):
    u_i = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    d_b = map(clean, db.get_group_list())
    assert sorted(u_i, key=Group.id_or_max) == sorted(d_b, key=Group.id_or_max)