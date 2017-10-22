from selenium.webdriver.firefox.webdriver import WebDriver
class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def logout(self):
        # logout
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys("\\9")
        wd.find_element_by_css_selector("html").click()

    def return_to_group(self):
        # return to group page
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def submit(self):
        # submit
        wd = self.wd
        wd.find_element_by_name("submit").click()

    def fill_group_fields(self, group):
        # fill group form
        wd = self.wd
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
        self.return_to_group()

    def group_creation_init(self):
        # init group creation
        wd = self.wd
        wd.find_element_by_name("new").click()

    def open_group_page(self):
        # open group page
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_homepage()
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()