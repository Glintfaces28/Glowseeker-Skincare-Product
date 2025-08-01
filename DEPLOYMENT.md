# 🚀 GlowSeeker Skincare Website Deployment Guide

## Frontend Deployment (React App)

### Option 1: Vercel (Recommended - Free)
1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy from frontend directory:**
   ```bash
   cd frontend
   vercel
   ```

3. **Follow the prompts:**
   - Link to existing project: No
   - Project name: glowseeker-frontend
   - Directory: ./
   - Override settings: No

4. **Set environment variable:**
   - Go to Vercel Dashboard → Your Project → Settings → Environment Variables
   - Add: `REACT_APP_API_URL` = `https://your-backend-url.onrender.com`

### Option 2: Netlify (Alternative - Free)
1. **Build the project:**
   ```bash
   cd frontend
   npm run build
   ```

2. **Deploy to Netlify:**
   - Go to [netlify.com](https://netlify.com)
   - Drag and drop the `build` folder
   - Set environment variable: `REACT_APP_API_URL` = `https://your-backend-url.onrender.com`

## Backend Deployment (FastAPI)

### Option 1: Render (Recommended - Free)
1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add deployment config"
   git push origin main
   ```

2. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - Create account and connect GitHub
   - Click "New Web Service"
   - Select your repository
   - Choose the `Backend` directory
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Click "Create Web Service"

3. **Get your backend URL:**
   - Copy the URL (e.g., `https://glowseeker-backend.onrender.com`)
   - Update frontend environment variable with this URL

### Option 2: Railway (Alternative - Free)
1. **Deploy on Railway:**
   - Go to [railway.app](https://railway.app)
   - Connect GitHub repository
   - Select the `Backend` directory
   - Railway will auto-detect Python and deploy

## Environment Variables Setup

### Frontend (Vercel/Netlify):
```
REACT_APP_API_URL=https://your-backend-url.onrender.com
```

### Backend (Render/Railway):
```
PYTHON_VERSION=3.9.16
```

## Quick Deploy Commands

### Frontend (Vercel):
```bash
cd frontend
vercel --prod
```

### Backend (Render):
- Use the Render dashboard or GitHub integration

## Testing Your Deployment

1. **Frontend URL:** `https://your-frontend-url.vercel.app`
2. **Backend URL:** `https://your-backend-url.onrender.com`
3. **API Test:** Visit `https://your-backend-url.onrender.com/docs` for API documentation

## Troubleshooting

### Common Issues:
1. **CORS Error:** Backend needs to allow frontend domain
2. **Environment Variables:** Make sure `REACT_APP_API_URL` is set correctly
3. **Build Errors:** Check if all dependencies are in `requirements.txt` and `package.json`

### Support:
- Vercel: [vercel.com/docs](https://vercel.com/docs)
- Render: [render.com/docs](https://render.com/docs)
- FastAPI: [fastapi.tiangolo.com](https://fastapi.tiangolo.com)

## Share Your Links

Once deployed, you can share:
- **Frontend:** `https://your-frontend-url.vercel.app`
- **Backend API:** `https://your-backend-url.onrender.com`
- **API Docs:** `https://your-backend-url.onrender.com/docs` 