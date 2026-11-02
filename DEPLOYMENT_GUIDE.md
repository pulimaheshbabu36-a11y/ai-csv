# Deployment Guide: AI CSV Report Generator

This guide explains how to deploy the AI CSV Report Generator to **Vercel** as well as alternative production container hosts (**Render / Railway / Docker**).

---

## Option 1: Deploy to Vercel (Serverless)

Vercel provides free global hosting for web applications and serverless Python functions.

### Step 1: Initialize Git Repository (if not already done)
Open your terminal in the project directory:
```bash
git init
git add .
git commit -m "Configure AI CSV Report Generator for Vercel deployment"
```

### Step 2: Push to GitHub
Create a new repository on [GitHub](https://github.com/new) (public or private), then link and push:
```bash
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git branch -M main
git push -u origin main
```

### Step 3: Import Project into Vercel
1. Go to [vercel.com](https://vercel.com) and log in.
2. Click **"Add New..."** -> **"Project"**.
3. Select your GitHub repository and click **Import**.
4. In the **Environment Variables** section, add your OpenAI API key:
   - **Key**: `OPENAI_API_KEY`
   - **Value**: `sk-proj-...` (your actual OpenAI key)
5. Leave Build & Output settings default (Vercel automatically detects `vercel.json`).
6. Click **Deploy**.

Your application will be live at `https://<your-project-name>.vercel.app` within 1–2 minutes!

> [!NOTE]
> **Vercel Serverless Behavior**:
> - Vercel Serverless functions run in ephemeral instances where `/tmp` is wiped between cold starts.
> - The application automatically routes file uploads, generated charts, PDF reports, and SQLite history to `/tmp` in the Vercel environment.
> - The maximum execution duration for serverless functions on Vercel Hobby accounts is 10–15 seconds (Pro accounts allow up to 60–300 seconds).

---

## Option 2: Deploy to Render (Persistent & Free Tier)

If you want persistent SQLite report history across sessions and support for longer AI execution times, **Render** is an excellent free-tier platform.

1. Push your repository to GitHub (as in Option 1).
2. Go to [render.com](https://render.com) and log in.
3. Click **"New +"** -> **"Web Service"**.
4. Connect your GitHub repository.
5. Render will automatically detect `render.yaml` or you can specify:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
6. In **Environment Variables**, add:
   - `OPENAI_API_KEY`: `your_key_here`
7. Click **Create Web Service**.

---

## Option 3: Deploy with Docker (Self-Hosted / Any Cloud)

A complete production `Dockerfile` is included in the project.

### Run with Docker locally:
```bash
docker build -t ai-csv-report .
docker run -p 8000:8000 -e OPENAI_API_KEY="your_key_here" ai-csv-report
```
Then open `http://localhost:8000` in your browser.

---

## Testing Locally Before Cloud Deployment

You can test the entire full-stack application (frontend + FastAPI backend) locally with a single command:
```powershell
.\venv\Scripts\python.exe -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```
Then visit:
- **Web Dashboard**: `http://127.0.0.1:8000/`
- **Interactive API Docs (Swagger)**: `http://127.0.0.1:8000/docs`
- **Health Check**: `http://127.0.0.1:8000/api/health`
