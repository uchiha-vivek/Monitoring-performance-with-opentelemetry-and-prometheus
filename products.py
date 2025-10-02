from flask import Blueprint, request, jsonify
import requests
from tracing import tracer

products_bp = Blueprint("products", __name__)

DUMMY_API_URL = "https://dummyjson.com/products"

@products_bp.route("/api/v1/products", methods=["GET"])
def list_products():
    with tracer.start_as_current_span("list_products") as span:
        # Set HTTP attributes
        span.set_attribute("http.method", request.method)
        span.set_attribute("http.route", request.path)
        span.set_attribute("http.target", request.full_path)

        try:
            # Fetch products from external API
            response = requests.get(DUMMY_API_URL)
            data = response.json()

            # Add attributes for tracing
            span.set_attribute("http.status_code", response.status_code)
            span.set_attribute("external.api", DUMMY_API_URL)

            return jsonify(data), response.status_code

        except Exception as e:
            # Record error in trace
            span.record_exception(e)
            return jsonify({"error": "Failed to fetch products"}), 500

@products_bp.route("/api/v1/products/<int:pid>", methods=["GET"])
def get_product(pid):
    with tracer.start_as_current_span("get_product") as span:
        span.set_attribute("http.method", request.method)
        span.set_attribute("http.route", request.path)
        span.set_attribute("product.id", pid)

        try:
            url = f"{DUMMY_API_URL}/{pid}"
            response = requests.get(url)
            data = response.json()

            span.set_attribute("http.status_code", response.status_code)
            span.set_attribute("external.api", url)

            return jsonify(data), response.status_code

        except Exception as e:
            span.record_exception(e)
            return jsonify({"error": f"Failed to fetch product {pid}"}), 500