from nebula_sdk import Interface, WebhookServer
from quart import Quart, request, jsonify, make_response

import logging

relay = Interface()
app = Quart('incident-triggered')

logging.getLogger().setLevel(logging.INFO)


@app.route('/', methods=['POST'])
async def handler():
    if request.headers.get('X-Webhook-Id') is None:
        return {'message': 'not a valid PagerDuty event'}, 400, {}

    payload = await request.get_json(force=True)
    for message in payload.get('messages', []):
        if message['event'] != 'incident.trigger':
            continue

        incident = message['incident']

        relay.events.emit({
            'id': incident['id'],
            'incident_number': incident['incident_number'],
            'title': incident['title'],
            'urgency': incident['urgency'],
            'triggered_at': incident['created_at'],
            'assignments': [{
                'assigned_at': assignment['at'],
                'assignee_id': assignment['assignee']['id'],
                'assignee_name': assignment['assignee']['summary'],
                'assignee_api_url': assignment['assignee']['self'],
                'assignee_app_url': assignment['assignee']['html_url'],
            } for assignment in incident['assignments']],
            'api_url': incident['self'],
            'app_url': incident['html_url'],
            'service_id': incident['service']['id'],
            'service_name': incident['service']['name'],
            'service_description': incident['service']['description'],
            'service_api_url': incident['service']['self'],
            'service_app_url': incident['service']['html_url'],
        })

    return {'message': 'success'}, 202, {}


if __name__ == '__main__':
    WebhookServer(app).serve_forever()
