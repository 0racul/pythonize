

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
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit()
        self.return_to()

    def creation_init(self):
        # init group creation
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def open(self):
        # open group page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
