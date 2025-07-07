# GitHub Setup Guide for Euler's Method App

## Step 1: Prepare Your Files

You need these files for GitHub:
- `app.py` (your main application)
- `euler_requirements.txt` (rename this to `requirements.txt` when uploading)
- `README.md` (project description and instructions)

## Step 2: Create GitHub Repository

1. **Go to GitHub.com**
2. **Sign in** (create account if needed)
3. **Click "+" in top right** → "New repository"
4. **Name your repo** (e.g., "euler-method-app")
5. **Add description**: "Streamlit app for solving differential equations using Euler's method"
6. **Make it Public** (required for free Streamlit deployment)
7. **Check "Add a README file"**
8. **Click "Create repository"**

## Step 3: Upload Your Files

**Option A: Web Interface (Easier)**
1. Click "uploading an existing file" on your new repo page
2. Drag and drop or select files:
   - `app.py`
   - `euler_requirements.txt` (rename to `requirements.txt`)
   - `README.md`
3. Write commit message: "Initial upload of Euler's method app"
4. Click "Commit changes"

**Option B: Git Commands (Advanced)**
```bash
git clone https://github.com/yourusername/euler-method-app.git
cd euler-method-app
# Copy your files here
# Rename euler_requirements.txt to requirements.txt
git add .
git commit -m "Initial upload of Euler's method app"
git push origin main
```

## Step 4: Deploy with Streamlit Community Cloud (FREE)

1. **Go to share.streamlit.io**
2. **Sign up** with your GitHub account
3. **Click "New app"**
4. **Select your repository**: euler-method-app
5. **Main file path**: `app.py`
6. **Click "Deploy!"**

## Step 5: Get Your App URL

- Your app will be available at: `https://yourusername-euler-method-app-app-xyz123.streamlit.app`
- Share this URL with anyone!
- It updates automatically when you push changes to GitHub

## Important Notes:

### File Requirements:
- **requirements.txt**: Must be named exactly this (not euler_requirements.txt)
- **app.py**: Your main Streamlit application
- **README.md**: Project description (helps others understand your app)

### Common Issues:
- **Deployment fails**: Check that requirements.txt is named correctly
- **Import errors**: Make sure all packages are listed in requirements.txt
- **App won't load**: Ensure app.py is in the root directory

### Benefits of This Approach:
- ✅ Free hosting
- ✅ Automatic updates when you change code
- ✅ Professional-looking URL
- ✅ Easy to share
- ✅ Version control with Git

## Alternative: Just Share GitHub Repository

If you only want to share the code (not host it):
1. Upload files to GitHub (Steps 1-3 above)
2. Share the repository URL: `https://github.com/yourusername/euler-method-app`
3. Others can clone/download and run locally

## Quick Checklist:

- [ ] Create GitHub account
- [ ] Create new public repository
- [ ] Upload app.py
- [ ] Upload euler_requirements.txt (rename to requirements.txt)
- [ ] Upload README.md
- [ ] Go to share.streamlit.io
- [ ] Connect GitHub account
- [ ] Deploy your app
- [ ] Share the live URL!

Your app will be running live on the internet for anyone to use!