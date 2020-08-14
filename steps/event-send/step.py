#!/usr/bin/env python

from pdpyras import APISession, EventsAPISession
from relay_sdk import Interface, Dynamic as D

relay = Interface()

token = relay.get(D.connection.accessToken)
session = EventsAPISession(token)

eventType = relay.get(D.type)
summary   = relay.get(D.summary)
source    = relay.get(D.source)
severity  = relay.get(D.severity)
dedupKey  = relay.get(D.dedup_key)

# All calls require type
# Trigger calls require summary/source/severity
# Trigger calls may take dedup_key
# Acknowledge and Resove calls require dedup_key
if eventType == None:
    sys.exit("A type is required for sending events, but none was set")
elif eventType == "trigger":
    if summary == None:
       sys.exit("A summary is required for event type trigger, but none was set")
    if source == None:
       sys.exit("A source is required for event type trigger, but none was set")
    if severity == None:
       sys.exit("A severity is required for event type trigger, but none was set")
    kwargs = dict(
        summary = summary,
        source = source,
        severity = severity,
        dedup_key = dedupKey,
    )
    response = session.trigger(**{k: v for k, v in kwargs.items() if v is not None})
elif eventType == "acknowledge":
    if dedupKey == None:
       sys.exit("A dedup_key is required for event type acknowledge, but none was set")
    response = session.acknowledge(dedupKey)
elif eventType == "resolve":
    if dedupKey == None:
       sys.exit("A dedup_key is required for event type resolve, but none was set")
    response = session.resolve(dedupKey)

relay.outputs.set("dedup_key", "This will be the value of the dedup_key recieved from PagerDuty")

print(response)
