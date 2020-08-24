#!/usr/bin/env python

from sys import exit
from copy import deepcopy
from relay_sdk import Interface, Dynamic as D
from pdpyras import PDSession, EventsAPISession, raise_on_error, PDClientError, try_decoding
from datetime import datetime


class ChangeEventsAPISession(PDSession):

    """
    Session class for submitting change events to the PagerDuty v2 Change Events API.

    Provides methods for submitting change events to the Change Events API.

    Inherits from :class:`PDSession`.
    """

    permitted_methods = ('POST',)

    url = "https://events.pagerduty.com"

    @property
    def auth_header(self):
        return {'X-Routing-Key': self.api_key}

    def prepare_headers(self, method):
        """Add user agent and content type headers for Events API requests."""
        headers = deepcopy(self.headers)
        headers.update({
            'Content-Type': 'application/json',
            'User-Agent': self.user_agent,
        })
        return headers

    def send_change_event(self, **properties):
        """
        Send a change event to the v2 Change Events API.

        # TODO This url may not be correct
        See: https://v2.developer.pagerduty.com/docs/send-a-change-event-events-api-v2

        :param **properties:
            Properties to set, i.e. ``payload`` and ``links``
        :returns:
            The response ID
        """
        event = deepcopy(properties)
        event['dedup_key'] = 'try-something-else'
        response = self.post('/v2/change/enqueue', json=event)
        #raise_on_error(response)
        # TODO This is a modified raise_on_error that returns the API error
        # message. The modification should be propagated back upstream.
        r = deepcopy(response)
        if not r.ok:
            raise PDClientError(
                "%s %s: API responded with non-success status "
                "(%d): %s" % (
                    r.request.method.upper(),
                    r.request.url.replace('https://api.pagerduty.com', ''),
                    r.status_code,
                    r.content
                ), response=r
            )
        response_body = try_decoding(response)
        return response_body.get("id", None)

    def submit(self, summary, source, custom_details=None, links=None):
        """
        Submit an incident change

        :param summary:
            Summary / brief description of the change.
        :param source:
            A human-readable name identifying the source of the change.
        :param custom_details:
            The ``payload.custom_details`` property of the payload. Will
            override the property set in the ``payload`` parameter if given.
        :param links:
            Set the ``links`` property of the event.
        :type summary: str
        :type source: str
        :type custom_details: dict
        :type links: list
        :rtype: str
        """
        local_var = locals()['custom_details']
        if not (local_var is None or type(local_var) is dict):
            raise ValueError("custom_details must be a dict")
        event = {'payload': {
            'summary': summary,
            'source': source,
            'timestamp': datetime.now().isoformat(),
        }}
        if type(custom_details) is dict:
            details = event.setdefault('payload', {}).get('custom_details', {})
            details.update(custom_details)
            event['payload']['custom_details'] = details
        if links:
            event['links'] = links
        return self.send_change_event(**event)


relay = Interface()

token = relay.get(D.connection.accessToken)
session = ChangeEventsAPISession(token)

summary = relay.get(D.summary)
source = relay.get(D.source)
if summary is None:
    exit("A summary is required, but none was set")

response = session.submit(summary, source)

relay.outputs.set("id", response)

print(response)
