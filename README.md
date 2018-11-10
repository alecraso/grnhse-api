# grnhse-api
[![pypi](https://img.shields.io/pypi/v/grnhse-api.svg)](https://pypi.org/project/grnhse-api/)
[![versions](https://img.shields.io/pypi/pyversions/grnhse-api.svg)](https://pypi.org/project/grnhse-api/)

A python wrapper for the [Greenhouse](https://developers.greenhouse.io/) APIs.

For now, only the [Harvest API](https://developers.greenhouse.io/harvest.html) is supported.

# Installation
```
$ pip install grnhse-api
```

# Basic Usage
```python
from grnhse import Harvest

api_key = 'ABCDE12345'
hvst = Harvest(api_key)
# <Harvest API v1>

depts = hvst.departments
depts
# <Departments Endpoint>

depts.get()
# [{'id': 1234,
#   'name': 'Administration',
#   'parent_id': None,
#   'child_ids': [],
#   'external_id': None},
#  {'id': 2345,
#   'name': 'Operations',
#   'parent_id': None,
#   'child_ids': [],
#   'external_id': None},
#  {'id': 3456,
#   'name': 'Engineering',
#   'parent_id': None,
#   'child_ids': [],
#   'external_id': None},
#   ...]

depts.get(1234)
# {'id': 1234,
#  'name': 'Administration',
#  'parent_id': None,
#  'child_ids': [],
#  'external_id': None}

admin = depts(1234)
admin
# <Departments Endpoint (id=1234)>

admin.get()
# {'id': 1234,
#  'name': 'Administration',
#  'parent_id': None,
#  'child_ids': [],
#  'external_id': None}

hvst.departments(1234).get()
# {'id': 1234,
#  'name': 'Administration',
#  'parent_id': None,
#  'child_ids': [],
#  'external_id': None}
```

# Pagination
```python
from grnhse import Harvest

api_key = 'ABCDE12345'
hvst = Harvest(api_key)

apps = hvst.applications
apps
# <Applications Endpoint>

all_apps = apps.get()
len(all_apps)
# 100
apps.records_remaining
# True
while apps.records_remaining:
    all_apps.extend(apps.get_next())
len(all_apps)
# 437

# Using list comprehension
all_apps = [app for page in apps for app in page]
len(all_apps)
# 437
```
