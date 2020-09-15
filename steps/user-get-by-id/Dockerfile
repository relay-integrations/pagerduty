FROM relaysh/core:latest-python
RUN pip install pdpyras
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="PagerDuty User details by id"
LABEL "org.opencontainers.image.description"="This step gets the details of a user from PagerDuty"
LABEL "com.puppet.nebula.sdk.version"="v1"
