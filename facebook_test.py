class Login:
    def add(self, name, email):
        self.emails[name] = email
    pass

    def __init__(self):
        self.emails = {}

    def lookup(self, name):
        return self.emails[name]

