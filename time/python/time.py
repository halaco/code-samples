import time
from datetime import timezone, datetime
from dateutil import parser, tz

utc = time.time()
date_time1 = datetime.now(timezone.utc)
date_time2 = datetime.fromtimestamp(utc, timezone.utc)
date_time3 = datetime.fromtimestamp(utc).astimezone()

print(utc)
print(date_time1)
print(date_time1.tzinfo)

print(date_time2)
print(date_time2.tzinfo)
print(date_time2.ctime())

print(date_time3)
print(date_time3.tzinfo)
print(date_time3.ctime())

print(date_time2.timestamp())
print(date_time3.timestamp())

# Get Local Time Zone
local_timezone = datetime.now().astimezone().tzinfo

print(local_timezone)
print(local_timezone.tzname(None))

local_timezone = tz.tzlocal()

print(local_timezone)
print(local_timezone.tzname(None))

print(datetime.now().astimezone(local_timezone))

date_time4 = datetime.now().astimezone()
print(date_time4)

print(str(date_time3.astimezone()))
print(date_time3.astimezone().ctime())

print(date_time1.isoformat())
print(date_time3.isoformat())

print(parser.isoparse("2021-06-06T15:09:44.624295+00:00"))
print(parser.isoparse("2021-06-06T15:09:44.624295Z"))
