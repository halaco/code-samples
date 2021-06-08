# Time API Samples

## Priciples
* Use UTC in code. SHOULD NOT have a local time in code.
* When handling a local time, the data MUST be combined with the timezone.

## python

### Data type

* `float`: A float value from the epic. fetched by `time.time()`
* `datetime.datetime`: fetched by `datetime.now(timezone.utc)`

SHOULD NOT use "naive" `datetime` object. If "naive" `datetime` is used, it MUST be a UTC time.  

### Import
```python
import time
from datetime import timezone, datetime
```

### Get UTC Time

```python
utc_float = time.time()
utc_datetime = datetime.now(timezone.utc)
local_datetime = datetime.now().astimezone()
```
Convert a float to a datetime.

```python
utc_datetime = datetime.fromtimestamp(utc_float, timezone.utc)
local_datetime = datetime.fromtimestamp(utc_float).astimezone()
```

Convert a datetime to a utc float.

```python
utc_float = date_time.timestamp()
```

Convert a utc datetime to a local datetime.

```python
local_datetime = utc_datetime.astimezone()
```

Convert a local datetime to a utc datetime.

```python
utc_datetime = local_datetime.astimezone(timezone.utc)
```

### Print as local time

```python
print(utc_datetime.astimezone())
```

### ISO8601

#### Formating

```
iso8601 = utc_datetime.isoformat()
```

#### Parseing with the datetuil
Use the dateutil ISO8601 parser

Install
```
pip install python-dateutil
```
or
```
pip install python-dateutil=2.8.1
```

```python
from dateutil import parser

datetime = parser.isoparse("2021-06-06T15:09:44.624295+00:00"))
```

### Time zone

Get a local time zone object
```python
LOCAL_TIMEZONE = datetime.now().astimezone().tzinfo
LOCAL_TIMEZONE = dateutil.tz.tzlocal()
```
datetime.now().astimezone().tzinfo != dateutil.tz.tzlocal()


### Monotonic Time APIs

```
sec = time.monotonic() # returns float
ns = time.monotonic_ns() # returns int (>=3.7)
```
