from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)


@app.route("/")
def home():
    return jsonify({
        "app": "K8sMonitor",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api")
def api():
    return jsonify({
        "message": "K8sMonitor API is working"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)


@app.route("/")
def home():
    return jsonify({
        "app": "K8sMonitor",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api")
def api():
    return jsonify({
        "message": "K8sMonitor API is working"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
