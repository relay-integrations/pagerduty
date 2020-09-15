#!/usr/bin/env python

from sys import exit
from urllib.parse import quote

from pdpyras import APISession
from relay_sdk import Interface, Dynamic as D

relay = Interface()

token = relay.get(D.connection.accessToken)
session = APISession(token)

user_id = relay.get(D.userID)
if user_id is None:
    exit("A userID is required, but none was set")

admin_key = relay.get(D.connection.accessToken)
session = APISession(admin_key)

# https://2.python-requests.org/en/master/api/#requests.Session.request
# eg https://api.pagerduty.com/users/PHNH11G
response = session.request("get", "https://api.pagerduty.com/users/" + quote(user_id))
response.raise_for_status()

data = response.json()

for output, prop in {
    'name': 'name',
    'email': 'email',
    'description': 'description',
    'timeZone': 'time_zone',
    'apiURL': 'self',
    'appURL': 'html_url',
}.items():
    if prop in data['user']:
        relay.outputs.set(output, data['user'][prop])

print('Found PagerDuty user {0} <{1}>'.format(data['user']['name'], data['user']['email']))
