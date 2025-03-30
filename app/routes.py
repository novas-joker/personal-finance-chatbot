from flask import Blueprint, render_template, request, jsonify
from app.chatbot.chat_processor import process_message
from app.models.news_service import get_financial_news

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Render the main chatbot interface"""
    return render_template('index.html')

@main_bp.route('/chat', methods=['POST'])
def chat():
    """Process chat messages and return responses"""
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    response = process_message(user_message)
    return jsonify({'response': response})

@main_bp.route('/news')
def news():
    """Fetch and display financial news"""
    news_items = get_financial_news()
    return render_template('news.html', news_items=news_items)

@main_bp.route('/budgeting')
def budgeting():
    """Display budgeting tools and recommendations"""
    return render_template('budgeting.html')

@main_bp.route('/api/news')
def api_news():
    """API endpoint to get financial news as JSON"""
    news_items = get_financial_news()
    return jsonify(news_items) 