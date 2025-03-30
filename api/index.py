from app import create_app

app = create_app()

# For Vercel serverless function handler
from flask import request as flask_request
import json

# Required for serving static files on Vercel
@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)

@app.route('/')
def index_redirect():
    return app.redirect('/')

# Vercel handler
def handler(request, context):
    environ = {
        'wsgi.input': request.body,
        'wsgi.errors': None,
        'wsgi.version': (1, 0),
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
        'wsgi.url_scheme': request.url.split('://')[0],
        'REQUEST_METHOD': request.method,
        'PATH_INFO': request.path,
        'QUERY_STRING': request.query.decode() if request.query else '',
        'SERVER_NAME': 'vercel',
        'SERVER_PORT': '443',
        'HTTP_HOST': request.headers.get('host', 'vercel.app'),
    }
    
    # Add all the headers
    for key, value in request.headers.items():
        key = key.upper().replace('-', '_')
        if key not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            key = 'HTTP_' + key
        environ[key] = value
    
    # Process the request
    response_data = {}
    
    def start_response(status, response_headers, exc_info=None):
        status_code = int(status.split(' ')[0])
        response_data['statusCode'] = status_code
        response_data['headers'] = dict(response_headers)
    
    body = b''.join(app(environ, start_response))
    
    if isinstance(body, bytes):
        body = body.decode('utf-8')
    
    response_data['body'] = body
    
    return response_data 