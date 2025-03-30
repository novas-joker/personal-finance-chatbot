from flask import Flask, request, jsonify, send_from_directory
import os
from app import create_app

app = create_app()

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def serve_static(path):
    return app.send_static_file(path)

# Vercel requires a handler function
def handler(request):
    with app.request_context(request):
        try:
            return app.handle_request()
        except Exception as e:
            return jsonify({"error": str(e)}), 500 