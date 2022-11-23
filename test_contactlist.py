import unittest
from contacts import Contact
class ContactTest(unittest.TestCase):
    def setUp(self):
        self.contacts = Contact()
    def test_lookup_by_firstname(self):
        self.contacts.add("Sofia", "0700433078")
        number = self.contacts.lookup("Sofia")
        self.assertEqual("0700433078", number)
    def test_lookup_by_lastname(self):
        self.contacts.add("Fallah", "0700433078")
        number = self.contacts.lookup("Fallah")
        self.assertEqual("0700433078", number)
    def test_missing_name_raises_error(self):
        with self.assertRaises(KeyError):
            self.contacts.lookup("missing")
    def test_empty_contacts_is_consistent(self):
        self.assertTrue(self.contacts.is_consistent())

    def test_is_consistent_with_address(self):
        self.contacts.add("Sofia", "Nybohovsbacken 99")
        self.assertTrue(self.contacts.is_consistent())
    def test_is_consistent_with_email(self):
        self.contacts.add("Sofia", "sofia.fallah@iths.se")
        self.assertTrue(self.contacts.is_consistent())