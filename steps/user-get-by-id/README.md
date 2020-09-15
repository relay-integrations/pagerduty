# user-get-by-id

This step can be used to retrieve a user's details from [PagerDuty](http://pagerduty.com/).

## Specification

This step expects the following fields in the `spec` section of a workflow step definition that uses it:

| Setting      | Data type        | Description                                       | Default | Required |
|--------------|------------------|---------------------------------------------------|---------|----------|
| `connection` | Relay connection | A pagerduty connection containing the admin token | None    | Yes      |
| `userID`     | String           | The PagerDuty ID of the user to be looked up      | None    | Yes      |

## Outputs

| Name          | Data type | Description                                               |
|---------------|-----------|-----------------------------------------------------------|
| `name`        | String    | The name of the user                                      |
| `email`       | String    | The user's email address                                  |
| `description` | String    | The user's bio                                            |
| `timeZone`    | String    | The user's preferred time zone                            |
| `apiURL`      | String    | The URL to the user record in the PagerDuty API           |
| `appURL`      | String    | The URL to the user record in the PagerDuty web interface |


## Usage

```yaml
steps:
- name: pagerduty-user
  image: relaysh/pagerduty-step-user-get-by-id
  spec:
    connection: !Connection [pagerduty, relay-pagerduty-service-integration]
    userID: !Parameter userID
```
