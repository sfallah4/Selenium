import unittest

from phonebook import PhoneBook

class PhoneBookTest(unittest.TestCase):
    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("Sofia", "0700433078")
        number = phonebook.lookup("Sofia")
        self.assertEqual("0700433078", number)

