# Personal Finance Assistant Chatbot

A web-based chatbot application that helps users manage their personal finances by providing budgeting guidance, investment advice, and financial news.

## Features

- Interactive chatbot interface to answer finance-related questions
- Budgeting guidance and recommendations for free budgeting apps
- 50/30/20 budget calculator tool
- Financial news feed from Yahoo Finance and other sources
- Investment education and resources

## Technology Stack

- Python 3.8+
- Flask web framework
- Bootstrap 5 for frontend styling
- jQuery for AJAX requests
- News API integration (optional)
- Beautiful Soup for web scraping

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd personal-finance-chatbot
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the following variables (optional):
   ```
   SECRET_KEY=your_secret_key_here
   NEWS_API_KEY=your_newsapi_key_here  # Get one at https://newsapi.org/
   ```

### Running Locally

1. Start the Flask development server:
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

### Deploying to Vercel

1. Push your code to a GitHub repository:
   ```
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. Connect the repository to Vercel:
   - Sign up or log in to [Vercel](https://vercel.com)
   - Click "Import Project" and select your GitHub repository
   - Vercel will automatically detect the project type and configure the build settings
   - Add your environment variables (SECRET_KEY and optional NEWS_API_KEY) in the Vercel dashboard
   - Click "Deploy"

3. Your application will be available at a URL provided by Vercel (e.g., `https://your-project-name.vercel.app`)

## Project Structure

- `app.py` - Application entry point for local development
- `api/index.py` - Entry point for Vercel deployment
- `vercel.json` - Vercel configuration file
- `app/` - Main package directory
  - `__init__.py` - Flask application factory
  - `routes.py` - Route definitions
  - `chatbot/` - Chatbot logic
    - `chat_processor.py` - Message processing and responses
  - `models/` - Data models and services
    - `news_service.py` - Financial news fetching service
  - `static/` - Static assets
    - `css/` - Stylesheets
    - `js/` - JavaScript files
  - `templates/` - HTML templates
    - `base.html` - Base template with layout
    - `index.html` - Chatbot interface
    - `budgeting.html` - Budgeting tools page
    - `news.html` - Financial news page

## Usage

1. **Chat Interface**: Ask the chatbot about budgeting, investments, or financial news.
2. **Budgeting Tools**: Access the budgeting page to use the 50/30/20 calculator and see app recommendations.
3. **Financial News**: View the latest financial headlines and access trusted news sources.

## License

MIT

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)
- [Font Awesome](https://fontawesome.com/)
- [Yahoo Finance](https://finance.yahoo.com/)
- [Investopedia](https://www.investopedia.com/)
- [Vercel](https://vercel.com/) 