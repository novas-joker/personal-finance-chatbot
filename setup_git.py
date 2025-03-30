#!/usr/bin/env python
import os
import subprocess
import sys

def run_command(command, error_message="Command failed"):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {error_message}")
        print(f"Command: {command}")
        print(f"Output: {e.stdout}")
        print(f"Error: {e.stderr}")
        return None

def setup_git_repository(github_repo_url=None):
    print("Setting up Git repository for Vercel deployment...")
    
    # Initialize Git repository if not already initialized
    if not os.path.exists('.git'):
        print("Initializing Git repository...")
        run_command("git init", "Failed to initialize Git repository")
    else:
        print("Git repository already initialized.")
    
    # Create .gitignore if it doesn't exist
    if not os.path.exists('.gitignore'):
        print("Creating .gitignore file...")
        with open('.gitignore', 'w') as f:
            f.write("""
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Environment variables
.env
.env.local
.env.development
.env.test
.env.production

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS specific
.DS_Store
Thumbs.db
            """)
    
    # Add all files to Git
    print("Adding files to Git...")
    run_command("git add .", "Failed to add files to Git")
    
    # Initial commit
    print("Creating initial commit...")
    run_command('git commit -m "Initial commit for Vercel deployment"', "Failed to create initial commit")
    
    # Add GitHub remote if URL provided
    if github_repo_url:
        print(f"Adding GitHub remote: {github_repo_url}")
        run_command(f"git remote add origin {github_repo_url}", "Failed to add GitHub remote")
        
        # Push to GitHub
        print("Pushing to GitHub...")
        run_command("git push -u origin main", "Failed to push to GitHub")
    else:
        print("\nRepository prepared locally. To push to GitHub:")
        print("1. Create a new repository on GitHub")
        print("2. Run the following commands:")
        print("   git remote add origin <your-github-repo-url>")
        print("   git push -u origin main")
    
    print("\nRepository is now ready for Vercel deployment.")
    print("To deploy to Vercel:")
    print("1. Go to https://vercel.com/")
    print("2. Connect your GitHub account")
    print("3. Import your repository")
    print("4. Configure your environment variables (SECRET_KEY, NEWS_API_KEY)")
    print("5. Deploy!")

if __name__ == "__main__":
    github_url = None
    if len(sys.argv) > 1:
        github_url = sys.argv[1]
    
    setup_git_repository(github_url) 