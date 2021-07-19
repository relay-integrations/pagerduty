#!/usr/bin/env python

from sys import exit
from relay_sdk import Interface, Dynamic as D
from pdpyras import ChangeEventsAPISession

relay = Interface()

token = relay.get(D.connection.accessToken)
session = ChangeEventsAPISession(token)

summary = relay.get(D.summary)
source = relay.get(D.source)
if summary is None:
    exit("A summary is required, but none was set")

response = session.submit(summary, source)

relay.outputs.set("id", response)

print("Summary '{}' was submitted; received the following response: {}".format(summary, response))
