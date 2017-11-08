from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    contact_cache = None


    def contact_creation(self, contact):
        wd = self.app.wd
        self.new_contact_init()
        self.fill_contact_fields(contact)
        self.select_group()
        self.submit()
        self.return_home()
        self.contact_cache = None

    def return_home(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        self.change_fields_value("firstname", contact.firstname)
        self.change_fields_value("middlename", contact.middlename)
        self.change_fields_value("lastname", contact.lastname)
        self.change_fields_value("nickname", contact.nickname)
        self.change_fields_value("title", contact.title)
        self.change_fields_value("company", contact.company)
        self.change_fields_value("address", contact.address)
        self.change_fields_value("home", contact.hometele)
        self.change_fields_value("mobile", contact.mobiletele)
        self.change_fields_value("work", contact.worktele)
        self.change_fields_value("fax", contact.fax)
        self.change_fields_value("email", contact.email)
        self.change_fields_value("email2", contact.email2)
        self.change_fields_value("email3", contact.email3)
        self.change_fields_value("homepage", contact.homepage)
        self.input_dates()
        self.change_fields_value("address2", contact.address2)
        self.change_fields_value("phone2", contact.phone2)
        self.change_fields_value("notes", contact.notes)

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def input_dates(self):
        wd = self.app.wd
        self.input_birth_day()
        self.input_birth_month()
        self.input_birth_year("2010")
        self.input_anniversary_day()
        self.input_anniversary_month()
        self.input_anniversary_year("3010")

    def select_group(self):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[10]").click()

    def input_anniversary_year(self, anniv_year):
        wd = self.app.wd
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(anniv_year)

    def input_anniversary_month(self):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[6]").click()

    def input_anniversary_day(self):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[5]").click()

    def input_birth_year(self, birth_year):
        wd = self.app.wd
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(birth_year)

    def input_birth_month(self):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[7]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[7]").click()

    def input_birth_day(self):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").click()

    def change_fields_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def new_contact_init(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def init_edit_contact_by_index(self, index):
            wd = self.app.wd
            site_index = index + 2
            wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(site_index) + "]/td[8]/a/img").click()

    def submit_updating(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.return_home()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_home()
            self.contact_cache = []
            x = 2
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                lastname = element.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(x) + "]/td[2]").text
                firstname = element.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(x) + "]/td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
                x = x+1
        return list(self.contact_cache)

    def update_first_contact(self, contact):
        wd = self.app.wd
        self.update_contact_by_index(0, contact)

    def update_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.init_edit_contact_by_index(index)
        self.fill_contact_fields(contact)
        self.submit_updating()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None




