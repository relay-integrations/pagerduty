# user-get-by-id

This step can be used to retrieve a user's details from [PagerDuty](http://pagerduty.com/).

## Specification

This step expects the following fields in the `spec` section of a workflow step definition that uses it:

| Setting      | Data type        | Description                                       | Default | Required |
|--------------|------------------|---------------------------------------------------|---------|----------|
| `connection` | Relay connection | A pagerduty connection containing the admin token | None    | Yes      |
| `userID`     | String           | The PagerDuty ID of the user to be looked up      | None    | Yes      |

## Outputs

| Name    | Data type | Description      |
|---------|-----------|------------------|
| `response` | Object    | not correct TODO |

example output value:
```json
{"user":{"name":"Hunter Haugen","email":"hunter@puppet.com", ... }}
```


## Usage

```yaml
steps:
- name: pagerduty-user
  image: relaysh/pagerduty-step-user-get-by-id
  spec:
```
