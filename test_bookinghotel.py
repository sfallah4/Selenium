import unittest
from booking import Booking

class BookingTest(unittest.TestCase):

    def setUp(self):
        self.booking = Booking()

    def test_lookup_by_date(self):
        self.booking.add("2022-11-20", "2 guests", "1 room")
        date = self.date.lookup("2 guests", "1 room")
        self.assertEqual("2022-11-20", date)
