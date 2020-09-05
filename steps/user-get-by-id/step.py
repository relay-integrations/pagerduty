#!/usr/bin/env python

from sys import exit
from pdpyras import APISession
from relay_sdk import Interface, Dynamic as D

relay = Interface()

token = relay.get(D.connection.accessToken)
session = APISession(token)

userid = relay.get(D.user_id)
if userid is None:
    exit("A userID is required, but none was set")

admin_key = relay.get(D.connection.accessToken)
session = APISession(admin_key)

# https://2.python-requests.org/en/master/api/#requests.Session.request
# eg https://api.pagerduty.com/users/PHNH11G
response = session.request("get", "https://api.pagerduty.com/users/" + userid)

relay.outputs.set("response", response.text)

print(response.text)
