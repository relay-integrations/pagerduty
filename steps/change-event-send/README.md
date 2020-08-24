# change-event-send

This step can be used to send change events to [PagerDuty](http://pagerduty.com/). Change events are the means by which incidents are [triggered](https://support.pagerduty.com/docs/incidents), acknowledged, or resolved.

## Specification

This step expects the following fields in the `spec` section of a workflow step definition that uses it:

| Setting      | Data type        | Description                                 | Default | Required |
|--------------|------------------|---------------------------------------------|---------|----------|
| `connection` | Relay connection | A pagerduty connection containing the token | None    | Yes      |
| `summary`    | String           | The [summary](#tbd) of the event triggered  | None    | Yes      |
| `source`     | String           | The [source](#tbd) of the event             | None    | No       |

## Outputs

| Name | Data type | Description                |
|------|-----------|----------------------------|
| `id` | String    | The id of the change event |

## Usage

```yaml
parameters:
  summary:
    description: "The description of the change"
  source:
    description: "The source of the change"

steps:
- name: pagerduty-change-event
  image: relaysh/pagerduty-step-change-event-send
  spec:
    connection: !Connection { type: pagerduty, name: my-project }
    summary: !Parameter summary
    source: !Parameter source
```
