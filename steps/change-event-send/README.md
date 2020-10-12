# change-event-send

This step can be used to send change events to [PagerDuty](http://pagerduty.com/). Change events are the means by which updates and changes can be tracked.

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
