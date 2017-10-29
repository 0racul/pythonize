from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app


    def contact_creation(self, contact):
        wd = self.app.wd
        self.new_contact_init()
        self.fill_contact_fields(contact)
        self.select_group()
        self.submit()

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        self.input_firstname(contact.firstname)
        self.input_middlename(contact.middlename)
        self.input_lastname(contact.lastname)
        self.input_nickname(contact.nickname)
        self.input_title(contact.title)
        self.input_company(contact.company)
        self.input_address(contact.address)
        self.input_hometele(contact.hometele)
        self.input_mobiletele(contact.mobiletele)
        self.input_worktele(contact.worktele)
        self.input_fax(contact.fax)
        self.input_email(contact.email)
        self.input_email2(contact.email2)
        self.input_email3(contact.email3)
        self.input_homepage(contact.homepage)
        self.input_dates()
        self.input_address2(contact.address2)
        self.input_phone2(contact.phone2)
        self.input_notes(contact.notes)

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def input_notes(self, note_field):
        wd = self.app.wd
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(note_field)

    def input_phone2(self, homesecondaryaddress):
        wd = self.app.wd
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(homesecondaryaddress)

    def input_address2(self, address2):
        wd = self.app.wd
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address2)

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

    def input_homepage(self, self_homepage):
        wd = self.app.wd
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(self_homepage)

    def input_email3(self, email3):
        wd = self.app.wd
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email3)

    def input_email2(self, email2):
        wd = self.app.wd
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email2)

    def input_email(self, email):
        wd = self.app.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)

    def input_fax(self, faxtele):
        wd = self.app.wd
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(faxtele)

    def input_worktele(self, worktele):
        wd = self.app.wd
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(worktele)

    def input_mobiletele(self, mobiletele):
        wd = self.app.wd
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobiletele)

    def input_hometele(self, hometele):
        wd = self.app.wd
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(hometele)

    def input_address(self, address):
        wd = self.app.wd
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)

    def input_company(self, company):
        wd = self.app.wd
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)

    def input_title(self, title):
        wd = self.app.wd
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)

    def input_nickname(self, nickname):
        wd = self.app.wd
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)

    def input_lastname(self, lastname):
        wd = self.app.wd
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)

    def input_middlename(self, middlename):
        wd = self.app.wd
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)

    def input_firstname(self, firstname):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)

    def new_contact_init(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def init_edit_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[3]/td[8]/a/img").click()

    def submit_updating(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

