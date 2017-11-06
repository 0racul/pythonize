class Contact:

    def __init__(self,firstname = None,
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
                        homesecondaryaddress = None,
                        notes = None):
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
        self.fax = faxtele
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = secondaryaddress
        self.phone2 = homesecondaryaddress
        self.notes = notes