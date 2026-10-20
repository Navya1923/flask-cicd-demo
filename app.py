import logging
import os
from flask import Flask, jsonify

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger("app")

FAIL_MODE = os.getenv("FAIL_MODE", "false") == "true"


@app.route("/")
def home():
    log.info("Home page requested")
    return jsonify(message="Hello from my CI/CD pipeline!", version="2.0")


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/ready")
def ready():
    if FAIL_MODE:
        log.error("Dependency check failed: cache connection refused (host=cache:6379)")
        return jsonify(status="not ready"), 503
    log.info("Readiness check passed")
    return jsonify(status="ready"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)