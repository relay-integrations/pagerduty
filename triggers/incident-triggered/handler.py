from relay_sdk import Interface, WebhookServer
from quart import Quart, request, jsonify, make_response

import logging
import json

relay = Interface()
app = Quart('incident-triggered')

logging.getLogger().setLevel(logging.INFO)


@app.route('/', methods=['POST'])
async def handler():
    if request.headers.get('X-Webhook-Id') is None:
        return {'message': 'not a valid PagerDuty event'}, 400, {}

    payload = await request.get_json(force=True)
    logging.info("Received the following webhook payload: \n%s", json.dumps(payload, indent=4))

    for message in payload.get('messages', []):
        if message['event'] != 'incident.trigger':
            continue

        incident = message['incident']

        relay.events.emit({
            'id': incident['id'],
            'incidentNumber': incident['incident_number'],
            'title': incident['title'],
            'urgency': incident['urgency'],
            'triggeredAt': incident['created_at'],
            'details': message['log_entries'][0]['channel']['details'],
            'assignments': [{
                'assignedAt': assignment['at'],
                'assigneeID': assignment['assignee']['id'],
                'assigneeName': assignment['assignee']['summary'],
                'assigneeAPIURL': assignment['assignee']['self'],
                'assigneeAppURL': assignment['assignee']['html_url'],
            } for assignment in incident['assignments']],
            'apiURL': incident['self'],
            'appURL': incident['html_url'],
            'service': incident['service']['id'],
            'serviceName': incident['service']['name'],
            'serviceDescription': incident['service']['description'],
            'serviceAPIURL': incident['service']['self'],
            'serviceAppURL': incident['service']['html_url'],
        }, key=message['id'])

    return {'message': 'success'}, 202, {}


if __name__ == '__main__':
    WebhookServer(app).serve_forever()
