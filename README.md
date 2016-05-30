# jsonLookup
Searching in MySQL JSON field in Django

# Challenge

MySQL has introduced JSON fields in MySQL Server 5.7, Currently it works well with [jsonfield](https://github.com/bradjasper/django-jsonfield) for Data Saving and retrieval. The problem that Searching can only be done through LIKE operator which isn't convinent for all function.

# Objective

Creating a new custom lookup operator "has" for Django that will support JSON Search in MySQL.

# Installation

### Install the Package
```sh
$ pip install jsonLookup
```

### Register to JSONFields

```python
from jsonLookup import hasLookup,jcontainsLookup
JSONField.register_lookup(hasLookup)
JSONField.register_lookup(jcontainsLookup)
```

### Write your JSON queries

```python
# Create test objects
User.objects.create(name="Ahmed",properties={"city":"Giza","Address":{"district":"Ahram","Code":11263}})
User.objects.create(name="Mohamed",properties={"city":"Cairo","Address":{"district":"Helipolis","Code":11351}})
# Run first query
q = User.objects.filter(properties__has="$.city=Giza")
print q[0].name
"Ahmed"
# Run Second query
q= User.objects.filter(properties__has="$.Address.Code=11351")
print q[0].name
"Mohamed"
```



