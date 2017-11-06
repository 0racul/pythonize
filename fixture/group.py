from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app


    def return_to(self):
        # return to group page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def submit(self):
        # submit
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def fill_fields(self, group):
        # fill group form
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open()
        #select 1st group
        wd.find_element_by_name("selected[]").click()
        #submit del
        wd.find_element_by_name("delete").click()
        #self.return_to()
        self.return_home()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.fill_fields(group)
        wd.find_element_by_name("update").click()
        self.return_home()

    def return_home(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def creation_init(self):
        # init group creation
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def open(self):
        # open group page
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
           wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.app.wd
        self.open()
        self.creation_init()
        self.fill_fields(group)
        self.submit()
        self.return_to()

    def count(self):
        wd = self.app.wd
        self.open()
        return len(wd.find_elements_by_name("selected[]"))