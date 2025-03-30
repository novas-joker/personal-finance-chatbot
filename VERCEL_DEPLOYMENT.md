# Deploying to Vercel with GitHub Actions

This guide explains how to set up automatic deployment to Vercel using GitHub Actions.

## Prerequisites

1. A GitHub account
2. A Vercel account
3. Your repository pushed to GitHub

## Step 1: Link your project to Vercel

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click "Import Project"
3. Select "Import Git Repository" and connect your GitHub account
4. Select your personal finance chatbot repository
5. Configure the project:
   - Framework Preset: `Other`
   - Root Directory: `./`
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: (leave empty)
   - Install Command: (leave empty)
6. Add environment variables:
   - `SECRET_KEY` - a strong secret key for your Flask application
   - `NEWS_API_KEY` - optional, your NewsAPI key if you have one
7. Click "Deploy"

## Step 2: Get Vercel deployment tokens

To enable GitHub Actions to deploy to Vercel, you need three values:

1. **Vercel Token**:
   - Go to [Vercel Account Settings](https://vercel.com/account/tokens)
   - Create a new token with a descriptive name (e.g., "GitHub Actions")
   - Copy the token value

2. **Vercel Organization ID** and **Project ID**:
   - Run the following command with your token:
     ```bash
     npx vercel login
     npx vercel link
     ```
   - This will create a `.vercel` directory with a `project.json` file
   - The file contains `orgId` and `projectId` values

## Step 3: Add secrets to your GitHub repository

1. Go to your GitHub repository
2. Navigate to Settings > Secrets > Actions
3. Add the following secrets:
   - `VERCEL_TOKEN`: Your Vercel token
   - `VERCEL_ORG_ID`: Your Organization ID
   - `VERCEL_PROJECT_ID`: Your Project ID

## Step 4: Push changes to trigger deployment

With everything set up, any push to the `main` branch will trigger the GitHub Actions workflow that automatically deploys your application to Vercel.

## Troubleshooting

- **Deployment failures**: Check the GitHub Actions logs for detailed error information
- **API issues**: Make sure your Vercel token has the correct permissions
- **Missing environment variables**: Verify that all required environment variables are set in Vercel

## Manual Deployment

If you prefer to deploy manually:

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy your application:
   ```bash
   vercel --prod
   ```

3. Follow the prompts to configure your deployment

## Next Steps

- Set up a custom domain in Vercel Dashboard
- Configure preview deployments for pull requests
- Add environment variables for different deployment environments (development, staging, production) 