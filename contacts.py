
class Contact:
    def add(self, name, number):
        self.numbers[name] = number
    pass
    def __init__(self):
        self.numbers = {}
    def lookup(self, name):
        return self.numbers[name]