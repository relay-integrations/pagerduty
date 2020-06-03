# pagerduty-trigger-incident-triggered

This [PagerDuty](https://pagerduty.com) trigger fires when a new incident is created. 

## Data Emitted 

| Name | Child data | Data type | Description | 
|------|------------|-----------|-------------|
| `id` | | string | id of the incident | 
| `incidentNumber` | | string | incident number | 
| `title`  | | string | incident title | 
| `urgency` | string | | incident urgency | 
| `triggeredAt` || datetime | time incident was triggered | 
| `assignments` | | mapping | mapping of incident assignments |
| | `assignedAt` | datetime | time incident was assigned | 
| | `assigneeID` | string | assignee id |
| | `assigneeName` | string | assignee name |
| | `assigneeAPIRUL` | url | assignee API URL |
| | `assigneeAppURL` | url | assignee app URL |
| `apiURL` || url | api URL | 
| `appURL` || url | app URL | 
| `service` || string | impacted service id |
| `serviceName` || string | impacted service name | 
| `serviceDescription` || string | impacted service description | 
| `serviceAPIURL` || url | impacted service API URL | 
| `serviceAppURL` || url | impacted service APP URL | 

## Example Trigger

```
parameters:
  id:
    default: ""
  title:
    default: ""
  urgency:
    default: ""
  serviceName:
    default: ""
  
triggers:
- name: pagerduty-incident
  source:
    type: webhook
    image: relaysh/pagerduty-trigger-incident-triggered:latest
  binding:
    parameters:
      id: !Data id
      title: !Data title
      urgency: !Data urgency
      serviceName: !Data serviceName
```

## Example Raw Data 

```
{
  "messages": [
    {
      "event": "incident.trigger",
      "log_entries": [
        {
          "id": "RP5DGEVXHFLN5CGGS0M7WLK5YQ",
          "type": "trigger_log_entry",
          "summary": "Triggered through the website",
          "self": "https://api.pagerduty.com/log_entries/RP5DGEVXHFLN5CGGS0M7WLK5YQ",
          "html_url": "https://relaysh.pagerduty.com/incidents/P0I34Z2/log_entries/RP5DGEVXHFLN5CGGS0M7WLK5YQ",
          "created_at": "2020-06-01T16:31:37Z",
          "agent": {
            "id": "P8F6MGW",
            "type": "user_reference",
            "summary": "Kenaz Kwa",
            "self": "https://api.pagerduty.com/users/P8F6MGW",
            "html_url": "https://relaysh.pagerduty.com/users/P8F6MGW"
          },
          "channel": {
            "type": "web_trigger",
            "summary": "test9",
            "subject": "test9",
            "details": null,
            "details_omitted": false,
            "body_omitted": false
          },
          "service": {
            "id": "PRVET6Y",
            "type": "service_reference",
            "summary": "task",
            "self": "https://api.pagerduty.com/services/PRVET6Y",
            "html_url": "https://relaysh.pagerduty.com/services/PRVET6Y"
          },
          "incident": {
            "id": "P0I34Z2",
            "type": "incident_reference",
            "summary": "[#15] test9",
            "self": "https://api.pagerduty.com/incidents/P0I34Z2",
            "html_url": "https://relaysh.pagerduty.com/incidents/P0I34Z2"
          },
          "teams": [],
          "contexts": [],
          "event_details": {
            "description": "test9"
          }
        }
      ],
      "webhook": {
        "endpoint_url": "https://webhook.site/ef7456dd-f6d3-4c13-8822-a2882a3eb7df",
        "name": "webhook.site",
        "description": null,
        "webhook_object": {
          "id": "PRVET6Y",
          "type": "service_reference",
          "summary": "task",
          "self": "https://api.pagerduty.com/services/PRVET6Y",
          "html_url": "https://relaysh.pagerduty.com/services/PRVET6Y"
        },
        "config": {
          "referer": "https://relaysh.pagerduty.com/extensions"
        },
        "outbound_integration": {
          "id": "PJFWPEP",
          "type": "outbound_integration_reference",
          "summary": "Generic V2 Webhook",
          "self": "https://api.pagerduty.com/outbound_integrations/PJFWPEP",
          "html_url": null
        },
        "accounts_addon": null,
        "id": "PI7BGWT",
        "type": "webhook",
        "summary": "webhook.site",
        "self": "https://api.pagerduty.com/webhooks/PI7BGWT",
        "html_url": null
      },
      "incident": {
        "incident_number": 15,
        "title": "test9",
        "description": "test9",
        "created_at": "2020-06-01T16:31:37Z",
        "status": "triggered",
        "incident_key": "6ae1421129e345618abea06568408335",
        "service": {
          "id": "PRVET6Y",
          "name": "task",
          "description": "Your first service - describe what this service is monitoring and any information that will help responders.\n\nFor example: What is the SLA of this service? Where are the runbooks for this service stored? What tier level is this service?",
          "created_at": "2020-05-27T15:53:00Z",
          "updated_at": "2020-05-27T15:53:00Z",
          "status": "critical",
          "teams": [],
          "alert_creation": "create_alerts_and_incidents",
          "addons": [],
          "scheduled_actions": [],
          "support_hours": null,
          "last_incident_timestamp": "2020-06-01T16:31:37Z",
          "escalation_policy": {
            "id": "PD4CGS5",
            "type": "escalation_policy_reference",
            "summary": "Default",
            "self": "https://api.pagerduty.com/escalation_policies/PD4CGS5",
            "html_url": "https://relaysh.pagerduty.com/escalation_policies/PD4CGS5"
          },
          "incident_urgency_rule": {
            "type": "constant",
            "urgency": "high"
          },
          "acknowledgement_timeout": null,
          "auto_resolve_timeout": null,
          "alert_grouping": null,
          "alert_grouping_timeout": null,
          "integrations": [
            {
              "id": "P0AAJ0X",
              "type": "event_transformer_api_inbound_integration_reference",
              "summary": "Amazon CloudWatch",
              "self": "https://api.pagerduty.com/services/PRVET6Y/integrations/P0AAJ0X",
              "html_url": "https://relaysh.pagerduty.com/services/PRVET6Y/integrations/P0AAJ0X"
            }
          ],
          "metadata": {},
          "response_play": null,
          "type": "service",
          "summary": "task",
          "self": "https://api.pagerduty.com/services/PRVET6Y",
          "html_url": "https://relaysh.pagerduty.com/services/PRVET6Y"
        },
        "assignments": [
          {
            "at": "2020-06-01T16:31:37Z",
            "assignee": {
              "id": "P8F6MGW",
              "type": "user_reference",
              "summary": "Kenaz Kwa",
              "self": "https://api.pagerduty.com/users/P8F6MGW",
              "html_url": "https://relaysh.pagerduty.com/users/P8F6MGW"
            }
          }
        ],
        "assigned_via": "escalation_policy",
        "last_status_change_at": "2020-06-01T16:31:37Z",
        "first_trigger_log_entry": {
          "id": "RP5DGEVXHFLN5CGGS0M7WLK5YQ",
          "type": "trigger_log_entry_reference",
          "summary": "Triggered through the website",
          "self": "https://api.pagerduty.com/log_entries/RP5DGEVXHFLN5CGGS0M7WLK5YQ",
          "html_url": "https://relaysh.pagerduty.com/incidents/P0I34Z2/log_entries/RP5DGEVXHFLN5CGGS0M7WLK5YQ"
        },
        "alert_counts": {
          "all": 0,
          "triggered": 0,
          "resolved": 0
        },
        "is_mergeable": true,
        "escalation_policy": {
          "id": "PD4CGS5",
          "type": "escalation_policy_reference",
          "summary": "Default",
          "self": "https://api.pagerduty.com/escalation_policies/PD4CGS5",
          "html_url": "https://relaysh.pagerduty.com/escalation_policies/PD4CGS5"
        },
        "teams": [],
        "impacted_services": [
          {
            "id": "PRVET6Y",
            "type": "service_reference",
            "summary": "task",
            "self": "https://api.pagerduty.com/services/PRVET6Y",
            "html_url": "https://relaysh.pagerduty.com/services/PRVET6Y"
          }
        ],
        "pending_actions": [],
        "acknowledgements": [],
        "basic_alert_grouping": null,
        "alert_grouping": null,
        "last_status_change_by": {
          "id": "PRVET6Y",
          "type": "service_reference",
          "summary": "task",
          "self": "https://api.pagerduty.com/services/PRVET6Y",
          "html_url": "https://relaysh.pagerduty.com/services/PRVET6Y"
        },
        "metadata": {},
        "external_references": [],
        "incidents_responders": [],
        "responder_requests": [],
        "subscriber_requests": [],
        "urgency": "high",
        "id": "P0I34Z2",
        "type": "incident",
        "summary": "[#15] test9",
        "self": "https://api.pagerduty.com/incidents/P0I34Z2",
        "html_url": "https://relaysh.pagerduty.com/incidents/P0I34Z2",
        "alerts": []
      },
      "id": "5db5f532-a425-11ea-9e1f-0242c0a82a0a",
      "created_on": "2020-06-01T16:31:38Z",
      "account_features": {
        "response_automation": true
      },
      "account_id": "PIXQBYJ"
    }
  ]
}
```