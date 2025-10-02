from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

def setup_tracer():
    resource = Resource(attributes={
        SERVICE_NAME: "ecommerce-backend"
    })

    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)

    #Jaeger exporter setup
    jaeger_exporter = JaegerExporter(
        agent_host_name="localhost",  # Jaeger agent host
        agent_port=6831,              # default UDP port
    )

    # Use BatchSpanProcessor for efficiency
    provider.add_span_processor(BatchSpanProcessor(jaeger_exporter))

    return trace.get_tracer(__name__)

tracer = setup_tracer()
