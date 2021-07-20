# incident-event-received

This trigger fires when a PagerDuty incident is triggered or resolved.

## Setup Instructions

- Navigate to Apps > Extensions > "New Extension"
- Select "Generic V2 Webhook" for the Extension Type
- Name your extension (e.g. "relay")
- Select the service
- Copy the webhook URL from your Relay workflow
- Paste it into the "URL:" field in PagerDuty
- Click "Save"
