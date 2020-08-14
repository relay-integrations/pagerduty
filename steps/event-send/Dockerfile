FROM relaysh/core:latest-python
RUN pip install pdpyras
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="PagerDuty Event Submission"
LABEL "org.opencontainers.image.description"="This step sends events to PagerDuty"
LABEL "com.puppet.nebula.sdk.version"="v1"
