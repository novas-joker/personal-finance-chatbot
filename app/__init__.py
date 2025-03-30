from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    # Load environment variables
    load_dotenv()
    
    # Create and configure the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-for-development')
    
    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app 