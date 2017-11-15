from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
class Application:

    def __init__(self, browser="firefox"):
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "opera":
            self.wd = webdriver.Opera()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("HeIIoH9ITHbIU 6Pay3eP %s" % browser)

        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False