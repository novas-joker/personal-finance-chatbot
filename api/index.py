from flask import Flask, request, jsonify, send_from_directory
import os
from app import create_app

app = create_app()

def handler(request):
    """
    Vercel serverless function handler
    """
    if not isinstance(request, dict):
        return {
            'statusCode': 500,
            'body': 'Invalid request format'
        }

    # Get the HTTP method and path
    method = request.get('method', 'GET')
    path = request.get('path', '/')
    
    # Handle static files
    if path.startswith('/static/'):
        try:
            file_path = path.replace('/static/', '')
            return {
                'statusCode': 200,
                'body': send_from_directory('app/static', file_path).get_data(as_text=True),
                'headers': {'Content-Type': 'text/html'}
            }
        except Exception as e:
            return {
                'statusCode': 404,
                'body': f'File not found: {str(e)}'
            }
    
    # Handle root path
    if path == '/':
        try:
            return {
                'statusCode': 200,
                'body': send_from_directory('app/static', 'index.html').get_data(as_text=True),
                'headers': {'Content-Type': 'text/html'}
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': f'Error serving index.html: {str(e)}'
            }
    
    # Handle API routes
    try:
        with app.test_request_context(
            path=path,
            method=method,
            headers=request.get('headers', {}),
            query_string=request.get('query', {}),
            data=request.get('body', '')
        ):
            response = app.full_dispatch_request()
            return {
                'statusCode': response.status_code,
                'body': response.get_data(as_text=True),
                'headers': dict(response.headers)
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error processing request: {str(e)}'
        } 