import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
import json
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

# You would need to sign up for a NewsAPI key at https://newsapi.org/
NEWS_API_KEY = os.environ.get('NEWS_API_KEY', '')

def get_financial_news(max_items=10):
    """
    Fetch financial news from multiple sources.
    Falls back to scraping Yahoo Finance if API key is not available.
    """
    # Try to use NewsAPI if key is available
    if NEWS_API_KEY:
        return get_news_from_api(max_items)
    else:
        # Fall back to scraping Yahoo Finance
        return get_news_from_yahoo(max_items)

def get_news_from_api(max_items=10):
    """Fetch financial news from NewsAPI"""
    # NewsAPI endpoint for financial news
    url = "https://newsapi.org/v2/top-headlines"
    
    # Get yesterday's date in the required format
    yesterday = datetime.now() - timedelta(days=1)
    from_date = yesterday.strftime('%Y-%m-%d')
    
    # Parameters for the API request
    params = {
        'apiKey': NEWS_API_KEY,
        'category': 'business',
        'language': 'en',
        'from': from_date,
        'pageSize': max_items
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200 and data.get('status') == 'ok':
            articles = data.get('articles', [])
            
            # Format the news items
            news_items = [
                {
                    'title': article.get('title'),
                    'description': article.get('description'),
                    'url': article.get('url'),
                    'source': article.get('source', {}).get('name', 'Unknown'),
                    'published_at': article.get('publishedAt')
                }
                for article in articles[:max_items]
            ]
            
            return news_items
        else:
            print(f"Error fetching news: {data.get('message', 'Unknown error')}")
            return []
            
    except Exception as e:
        print(f"Exception when fetching news: {str(e)}")
        return []

def get_news_from_yahoo(max_items=10):
    """Scrape financial news from Yahoo Finance as a fallback"""
    url = "https://finance.yahoo.com/topic/stock-market-news"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Error fetching Yahoo Finance: Status code {response.status_code}")
            return []
            
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find news articles
        articles = soup.find_all('div', {'class': 'Ov(h)'})
        
        news_items = []
        for article in articles[:max_items]:
            title_elem = article.find('h3')
            link_elem = article.find('a')
            
            if title_elem and link_elem:
                title = title_elem.text.strip()
                link = link_elem['href']
                
                # Format the URL correctly
                if link.startswith('/'):
                    link = f"https://finance.yahoo.com{link}"
                
                news_items.append({
                    'title': title,
                    'description': '',  # No description in the simple scraping
                    'url': link,
                    'source': 'Yahoo Finance',
                    'published_at': datetime.now().isoformat()
                })
        
        return news_items
            
    except Exception as e:
        print(f"Exception when scraping Yahoo Finance: {str(e)}")
        return [] 