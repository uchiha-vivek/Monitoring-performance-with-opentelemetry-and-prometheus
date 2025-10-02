from flask import Flask
from products import products_bp
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Auto-instrument Flask routes (adds http.method, http.route, etc.)
FlaskInstrumentor().instrument_app(app)

metrics = PrometheusMetrics(app)

# Register blueprints
app.register_blueprint(products_bp)

metrics.info("app_info", "E-commerce backend with Flask, OTel, Jaeger, Prometheus", version="1.0.0")


if __name__ == "__main__":
    app.run(debug=True)
