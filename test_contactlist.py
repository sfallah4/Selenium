import unittest
from booking import Booking
class BookingTest(unittest.TestCase):
    def setUp(self):
        self.booking = Booking()
    def tearDown(self):
        pass
    def test_lookup_by_firstname(self):
        self.booking.add("Sofia", "0700433078")
        number = self.booking.lookup("Sofia")
        self.assertEqual("0700433078", number)
    def test_lookup_by_lastname(self):
        self.booking.add("Fallah", "0700433078")
        number = self.booking.lookup("Fallah")
        self.assertEqual("0700433078", number)
    def test_missing_name_raises_error(self):
        with self.assertRaises(KeyError):
            self.booking.lookup("missing")
    def test_empty_booking_is_consistent(self):
        self.assertTrue(self.booking.is_consistent())
    def test_is_consistent_with_different_entries(self):
        self.booking.add("Sofia", "0700433078")
        self.booking.add("Elena", "0720433078")
        self.assertTrue(self.booking.is_consistent())
    def test_inconsistent_with_duplicate_entries(self):
        self.booking.add("Sofia", "0700433078")
        self.booking.add("Eva", "0700433078")
        self.assertFalse(self.booking.is_consistent())
    def test_inconsistent_with_duplicate_prefix(self):
        self.booking.add("Sofia", "0700433078")
        self.booking.add("Eva", "07004")
        self.assertFalse(self.booking.is_consistent())

import calendar
from datetime import datetime

dt = datetime.now()
print('Datetime is:', dt)

c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2022, 11)
print (str)
