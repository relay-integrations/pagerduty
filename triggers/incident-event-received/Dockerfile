FROM python:3-alpine
RUN apk --no-cache add ca-certificates && update-ca-certificates
RUN pip --no-cache-dir install relay-sdk quart
COPY handler.py /relay/handler.py
ENTRYPOINT []
CMD ["python3", "/relay/handler.py"]

LABEL "org.opencontainers.image.title"="PagerDuty incident event received"
LABEL "org.opencontainers.image.description"="This trigger fires when a PagerDuty incident is triggered or resolved."
LABEL "com.puppet.nebula.sdk.version"="v1"
