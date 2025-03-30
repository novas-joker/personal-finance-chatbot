from app.models.news_service import get_financial_news

# Dictionary of budgeting apps to recommend
BUDGETING_APPS = {
    'Mint': {
        'url': 'https://mint.intuit.com/',
        'description': 'Free budgeting app that connects to your accounts and helps track spending.'
    },
    'Personal Capital': {
        'url': 'https://www.personalcapital.com/',
        'description': 'Free financial dashboard that includes budgeting and investment tracking tools.'
    },
    'YNAB (You Need A Budget)': {
        'url': 'https://www.ynab.com/',
        'description': 'Budgeting app focused on giving every dollar a job using a zero-based budget approach.'
    }
}

# Sample investment educational resources
INVESTMENT_RESOURCES = {
    'Investopedia Investing Basics': 'https://www.investopedia.com/investing-4427685',
    'Yahoo Finance Education': 'https://finance.yahoo.com/education/',
    'Bogleheads Investment Philosophy': 'https://www.bogleheads.org/wiki/Bogleheads%C2%AE_investment_philosophy'
}

def process_message(message):
    """
    Process user message and return an appropriate response
    """
    message = message.lower()
    
    # Budgeting related queries
    if any(keyword in message for keyword in ['budget', 'spending', 'track expenses', 'save money']):
        return create_budget_response(message)
    
    # Investment related queries
    elif any(keyword in message for keyword in ['invest', 'stock', 'etf', 'fund', 'retirement']):
        return create_investment_response(message)
    
    # Financial news queries
    elif any(keyword in message for keyword in ['news', 'financial news', 'market news']):
        return create_news_response()
    
    # Default response if no specific category is matched
    else:
        return "Hi! I'm your personal finance assistant. I can help with budgeting, investments, and financial news. What would you like to know about?"

def create_budget_response(message):
    """Generate response for budget-related queries"""
    if 'app' in message or 'tool' in message:
        apps_info = "\n".join([f"• {name}: {info['description']} ({info['url']})" 
                              for name, info in BUDGETING_APPS.items()])
        return f"Here are some great free budgeting apps you can use:\n{apps_info}"
    
    return """
    Here are some budgeting tips:
    1. Track all your expenses for a month to understand your spending habits
    2. Create a zero-based budget where every dollar has a purpose
    3. Follow the 50/30/20 rule: 50% for needs, 30% for wants, and 20% for savings
    4. Set specific financial goals to stay motivated
    
    Would you like me to recommend some budgeting apps?
    """

def create_investment_response(message):
    """Generate response for investment-related queries"""
    resources = "\n".join([f"• {name}: {url}" for name, url in INVESTMENT_RESOURCES.items()])
    
    return f"""
    Investment education is crucial before putting your money in the market.
    
    Key investment principles:
    1. Start early and be consistent
    2. Diversify your investments
    3. Keep costs low with index funds
    4. Invest for the long term
    
    Here are some reliable resources to learn more:
    {resources}
    """

def create_news_response():
    """Generate response with current financial news"""
    news = get_financial_news(max_items=3)
    
    if not news:
        return "I'm having trouble fetching the latest financial news. Please try again later."
    
    news_text = "\n".join([f"• {item['title']} - {item['source']}" for item in news])
    
    return f"""
    Here are the latest financial headlines:
    {news_text}
    
    You can view more news in the News section of our app.
    """ 