from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "Python Production App",
        "status": "running",
        "message": "Application deployed successfully!"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "hostname": socket.gethostname()
    }), 200


@app.route("/api/info")
def info():
    return jsonify({
        "application": "Python Production App",
        "environment": os.getenv("ENVIRONMENT", "production"),
        "version": os.getenv("APP_VERSION", "1.0.0")
    })


if __name__ == "__main__":
    app.run()
