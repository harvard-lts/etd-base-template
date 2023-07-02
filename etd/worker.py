import os
import requests
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

"""
This is a template of a basic worker class for etds.

Since: 2023-05-23
Author: cgoines
"""


class Worker():
    version = None

    def __init__(self):
        self.version = os.getenv("APP_VERSION", "0.0.1")

    def get_version(self):
        return self.version

    # this is call to the DASH healthcheck for integration testing
    def call_api(self):
        with tracer.start_as_current_span("server_request", 
                                          attributes={ "endpoint": "/call_api"}):
            url = "https://dash.harvard.edu/rest/test"
            r = requests.get(url)
            span = trace.get_current_span()
            span.add_event("log", {"call.api": r.text})
            return r.text
