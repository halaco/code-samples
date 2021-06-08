import unittest
import time
from datetime import timezone, datetime, timedelta, tzinfo
from dateutil import parser, tz

class HtimiLaCommonTest(unittest.TestCase):

    def test_get_utc_time(self):
        utc_float = time.time()

        self.assertTrue(type(utc_float) is float)


    def test_get_utc_datetime(self):
        date_time = datetime.now(timezone.utc)

        self.assertTrue(type(date_time) is datetime)
        self.assertIsNotNone(date_time.tzinfo)
        self.assertTrue(type(date_time.tzinfo) is timezone)
        self.assertEqual("UTC", str(date_time.tzinfo))
        self.assertEqual(timedelta(0), date_time.tzinfo.utcoffset(None))


    def test_convert_to_utc_datetime(self):
        date_time = datetime.fromtimestamp(1623041958.1010292, timezone.utc)

        self.assertIsNotNone(date_time.tzinfo)
        self.assertTrue(type(date_time.tzinfo) is timezone)
        self.assertEqual("UTC", str(date_time.tzinfo))        
        self.assertEqual(2021, date_time.year)
        self.assertEqual(6, date_time.month)
        self.assertEqual(7, date_time.day)
        self.assertEqual(4, date_time.hour)
        self.assertEqual(59, date_time.minute)
        self.assertEqual(18, date_time.second)
        self.assertEqual(101029, date_time.microsecond)


    def test_convert_to_timestamp(self):
        date_time = datetime(2021, 6, 7, 4, 59, 18, 101029, tzinfo=timezone.utc)

        self.assertEqual(1623041958.101029, date_time.timestamp())


    def test_dateutil_tzlocal(self):
        local_timezone = tz.tzlocal()

        self.assertTrue(issubclass(type(local_timezone), tzinfo))
    

    def test_isoformat(self): 
        date_time = datetime(2021, 6, 7, 4, 59, 18, 101029, tzinfo=timezone.utc)
        self.assertEqual("2021-06-07T04:59:18.101029+00:00", date_time.isoformat())


    def test_isoparse(self): 
        date_time = parser.isoparse("2021-06-07T04:59:18.101029+00:00")
        self.assertEqual(1623041958.101029, date_time.timestamp())

        date_time = parser.isoparse("2021-06-07T04:59:18.101029Z")
        self.assertEqual(1623041958.101029, date_time.timestamp())


    def test_monotonic_time(self):
        start_float = time.monotonic()

        time.sleep(0.1)

        end_float = time.monotonic()

        self.assertAlmostEqual((end_float - start_float), 0.1, places=2)


if __name__ == '__main__':
    unittest.main()
