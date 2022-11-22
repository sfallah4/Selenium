import unittest
from contacts import Contact
class ContactTest(unittest.TestCase):
    def setUp(self):
        self.contacts = Contact()
    def test_lookup_by_firstname(self):
        self.contacts.add("Sofia", "0700433078")
        number = self.contacts.lookup("Sofia")
        self.assertEqual("0700433078", number)