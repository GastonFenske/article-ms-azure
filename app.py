import os, logging
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
# from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter

# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Configurar el logging
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)  # Establecer el nivel de logging deseado

def create_app() -> Flask:
    app = Flask(__name__)
    load_dotenv()
    CORS(app)
    return app

app: Flask = create_app()

app.app_context().push()

# Set global TracerProvider before instrumenting
trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({SERVICE_NAME: "article-ms-opentelemetry"})
    )
)

# Enable tracing for sqlalchemy library
# SQLAlchemyInstrumentor().instrument()

# Enable tracing for Flask library
FlaskInstrumentor().instrument_app(app)

# Enable tracing for requests library
RequestsInstrumentor().instrument()

trace_exporter = AzureMonitorTraceExporter(
    connection_string="InstrumentationKey=63c8e473-95e8-40ee-822f-819240c88ef0;IngestionEndpoint=https://eastus-8.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus.livediagnostics.monitor.azure.com/"
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(trace_exporter)
)

@app.route('/healthcheck', methods=['GET'])
def health_check():
    app.logger.info('Health check endpoint accessed')  # Ejemplo de log
    return 'App working correctly', 200

if __name__ == '__main__':
    app.logger.info('Starting the application')  # Ejemplo de log al inicio de la aplicación
    app.run(host = '0.0.0.0', debug = True, port = 6000)