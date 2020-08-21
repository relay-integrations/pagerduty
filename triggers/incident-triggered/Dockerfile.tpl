FROM python:3-alpine
RUN apk --no-cache add ca-certificates && update-ca-certificates
RUN pip --no-cache-dir install relay-sdk quart
COPY handler.py /relay/handler.py
ENTRYPOINT []
CMD ["python3", "/relay/handler.py"]
