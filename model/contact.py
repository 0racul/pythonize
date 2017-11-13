from sys import maxsize
class Contact:

    def __init__(self, firstname = None,
                 middlename = None,
                 lastname = None, nickname = None,
                 title = None, company = None,
                 address = None, hometele = None,
                 mobiletele = None,
                 worktele = None,
                 faxtele = None,
                 email = None,
                 email2 = None,
                 email3 = None,
                 homepage = None,
                 secondaryaddress = None,
                 phone2 = None,
                 notes = None,
                 id = None,
                 all_phones_from_homepage = None,
                 all_emails_from_homepage = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.hometele = hometele
        self.mobiletele = mobiletele
        self.worktele = worktele
        self.faxtele = faxtele
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.secondaryaddress = secondaryaddress
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage


    def __repr__(self):
      return "%s:%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.address, self.all_phones_from_homepage, self.all_emails_from_homepage)

    def __eq__(self, other):
      return ((self.id is None or other.id is None or self.id == other.id)
              and self.lastname == other.lastname
              and self.firstname == other.firstname
              and self.middlename == other.middlename
              and self.nickname == other.nickname
              and self.title == other.title
              and self.company == other.company
              and self.hometele == other.hometele
              and self.worktele == other.worktele
              and self.faxtele == other.faxtele
              and self.email == other.email
              and self.email2 == other.email2
              and self.email3 == other.email3
              and self.homepage == other.homepage
              and self.secondaryaddress == other.secondaryaddress
              and self.phone2 == other.phone2
              and self.notes == other.notes
              and self.address == other.address
              and self.mobiletele == other.mobiletele
              and self.all_phones_from_homepage == other.all_phones_from_homepage
              and self.all_emails_from_homepage == other.all_emails_from_homepage)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

