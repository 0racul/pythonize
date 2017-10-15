# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_gruppe(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_add_gruppe(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, "admin", "secret")
        self.open_group_page(wd)
        self.group_creation_init(wd)
        self.fill_group_fields(wd, Group("y", "bh", "bh"))
        self.submit(wd)
        self.return_to_group(wd)
        self.logout(wd)

    def test_add_empty_gruppe(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, "admin", "secret")
        self.open_group_page(wd)
        self.group_creation_init(wd)
        self.fill_group_fields(wd, Group("", "", ""))
        self.submit(wd)
        self.return_to_group(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys("\\9")
        wd.find_element_by_css_selector("html").click()

    def return_to_group(self, wd):
        # return to group page
        wd.find_element_by_link_text("group page").click()

    def submit(self, wd):
        # submit
        wd.find_element_by_name("submit").click()

    def fill_group_fields(self, wd, group):
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def group_creation_init(self, wd):
        # init group creation
        wd.find_element_by_name("new").click()

    def open_group_page(self, wd):
        # open group page
        wd.find_element_by_name("searchstring").click()
        wd.find_element_by_name("searchstring").send_keys("\\9")
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
