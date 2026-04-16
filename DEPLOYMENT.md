# Deployment Guide: Render.com

## Step-by-Step Deployment

### Prerequisites
- GitHub account
- Render account (free at render.com)
- Your code pushed to GitHub

### 1. Prepare for Deployment

Ensure your project has:
- ✅ `requirements.txt` (all dependencies listed)
- ✅ `model.h5` and `scaler.pkl` (trained models)
- ✅ `Artificial_Neural_Network_Case_Study_data.csv` (in .gitignore or uploaded separately)
- ✅ `.gitignore` (exclude large files)

### 2. Create Render Service

1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Select "Build and deploy from a Git Repository"
4. Connect GitHub (authorize if first time)
5. Select your `ann-project` repository

### 3. Configure Service

Fill in these settings:

| Setting | Value |
|---------|-------|
| **Name** | ann-api |
| **Region** | US East (or closest to you) |
| **Runtime** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn app:app --host 0.0.0.0 --port 10000` |
| **Plan** | Free |

### 4. Environment Variables (if needed)

In Render dashboard:
- Settings → Environment
- Add variables if using `.env` file (optional)

### 5. Deploy

Click "Create Web Service"

Render will:
1. Clone your repo
2. Run build command
3. Start the server
4. Generate public URL (2-3 minutes)

### 6. Monitor Deployment

Check "Logs" tab to see:
```
INFO:     Uvicorn running on http://0.0.0.0:10000
```

### 7. Access Your API

Your public URL: `https://your-app-name.onrender.com`

Test it:
```bash
curl https://your-app-name.onrender.com/

# Should return:
# {"message":"ANN API is running",...}
```

### 8. Use the API

**Swagger Docs:** 
```
https://your-app-name.onrender.com/docs
```

**Make Prediction:**
```bash
curl -X POST "https://your-app-name.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -d '{"data": [45, 60000, 1, 0, 3]}'
```

## Important Notes

### ⚠️ Cold Starts
- Free tier: Server goes to sleep after 15 mins
- First request after sleep takes ~30 seconds
- Upgrade to paid plan to avoid this

### 📁 Large Files
If your CSV or model is large:
1. Add to `.gitignore`
2. Use Render's disk storage
3. Or download from cloud storage in app.py

### 💾 Persistent Storage
Free tier doesn't persist files between redeploys. To save files:
- Store in cloud (AWS S3, Google Cloud)
- Or upgrade to paid plan

### 🔄 Auto-Deploy
Set "Auto-Deploy" to "On" so changes to `main` branch auto-deploy

### 📈 Monitoring
Check these in Render dashboard:
- Logs
- Metrics (CPU, Memory)
- Events

## Troubleshooting

### Build Fails
Check "Logs" tab → look for error messages
Common issues:
- Missing dependencies in `requirements.txt`
- Syntax errors in Python code
- Missing data files

### Service Won't Start
```
ModuleNotFoundError: No module named 'tensorflow'
```
→ Run: `pip install -r requirements.txt` locally first to verify all packages work

### Port Issues
Change start command:
```
uvicorn app:app --host 0.0.0.0 --port 10000
```
(Port must be dynamic, Render assigns it)

### Model Not Found
If `model.h5` is in `.gitignore`:
1. Add to Git: `git rm -r --cached model.h5`
2. Push to repo
3. Redeploy

## Cost (2026)
- **Free tier:** 750 compute hours/month
- **Typical API:** Uses ~10-15 hours/month
- **Upgrade:** $7/month for better performance

## Next Steps

1. ✅ Deploy on Render
2. Share public link: `https://your-app-name.onrender.com`
3. Monitor logs
4. Upgrade if needed

---
**Status:** Ready for deployment! 🚀
