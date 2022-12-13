class Login:
    def add(self, name, email):
        self.emails[name] = email
    pass
    def __init__(self):
        self.emails = {}
    def lookup(self, name):
        return self.emails[name]
    def is_consistent(self):
        for name1, email1 in self.emails.items():
            for name2, email2 in self.emails.items():
                if email1 == name2:
                    continue
                if email1.startswith(email2):
                    return False
        return True