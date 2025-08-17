# 🚂 Deploy Heart Attack Risk Prediction Backend on Railway

This guide will walk you through deploying your Heart Attack Risk Prediction Flask application on Railway's platform.

## 📋 Prerequisites

- GitHub account with your project repository
- Railway account (free tier available)
- Python 3.8+ project ready for deployment

## 🛠️ Pre-deployment Setup

### 1. Project Structure
Ensure your project has these files:
```
Heart-Attack-Risk-Prediction-lnm71a/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies (includes gunicorn)
├── railway.json          # Railway deployment configuration
├── Procfile              # Process file (optional for Railway)
├── .gitignore            # Git ignore file
├── models/               # Pre-trained ML models
├── templates/            # HTML templates
└── dataset/              # Training dataset
```

### 2. Key Changes Made for Deployment
- ✅ Added `gunicorn==21.2.0` to requirements.txt
- ✅ Created `railway.json` for Railway configuration
- ✅ Modified `app.py` for production environment
- ✅ Created `.gitignore` to exclude virtual environment

## 🚀 Deployment Steps

### Step 1: Push Changes to GitHub

```bash
# Add all new files
git add .

# Commit changes
git commit -m "Prepare for Railway deployment - Add railway.json and deployment config"

# Push to GitHub
git push origin main
```

### Step 2: Deploy on Railway

1. **Sign up/Login to Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up with your GitHub account

2. **Create New Project**
   - Click "Start a New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository: `Heart-Attack-Risk-Prediction-Using-Machine-Learning`

3. **Configure the Service**
   - Railway will automatically detect it's a Python project
   - **Service Name**: `heart-attack-risk-prediction` (or your preferred name)
   - **Branch**: `main`
   - **Root Directory**: Leave empty (or specify if needed)

4. **Deploy Settings**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Health Check Path**: `/`

5. **Environment Variables (Optional)**
   - Add any environment variables if needed
   - Railway automatically sets `PORT` environment variable

6. **Deploy**
   - Click "Deploy Now"
   - Railway will automatically build and deploy your app

## 🔧 Railway Configuration Details

### railway.json
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "gunicorn app:app",
    "healthcheckPath": "/",
    "healthcheckTimeout": 100,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### requirements.txt (Updated)
```
Boruta==0.4.3
Flask==3.1.1
gunicorn==21.2.0          # Added for production
imbalanced_learn==0.13.0
joblib==1.5.0
matplotlib==3.10.3
numpy==2.2.6
pandas==2.2.3
scikit_learn==1.6.1
seaborn==0.13.2
statsmodels==0.14.4
```

## 🌐 Post-Deployment

### 1. Access Your Application
- Railway will provide a URL like: `https://your-app-name.railway.app`
- Your app will be accessible from anywhere on the internet

### 2. Monitor Deployment
- Check the "Deployments" tab for build status
- Monitor "Metrics" for performance
- View logs in real-time

### 3. Custom Domain (Optional)
- In Railway dashboard, go to "Settings" → "Domains"
- Add your custom domain and configure DNS

## 🔍 Troubleshooting

### Common Issues:

1. **Build Failures**
   - Check requirements.txt for compatibility
   - Ensure all dependencies are available
   - Check Python version compatibility

2. **Runtime Errors**
   - Check application logs in Railway dashboard
   - Verify model files are included in deployment
   - Ensure proper file paths

3. **Memory Issues (Free Tier)**
   - Free tier has 512MB RAM limit
   - Consider optimizing large models
   - Use model compression if needed

4. **Port Configuration**
   - Railway automatically sets `PORT` environment variable
   - Ensure your app uses: `os.environ.get('PORT', 5000)`

### Debug Commands:
```bash
# Check local build
pip install -r requirements.txt
gunicorn app:app

# Test locally
curl http://localhost:8000
```

## 📊 Performance Optimization

### For Free Tier:
- **Model Size**: Keep models under 100MB total
- **Dependencies**: Minimize unnecessary packages
- **Caching**: Implement basic caching if possible
- **Async**: Use async operations where applicable

### For Paid Plans:
- **Auto-scaling**: Configure based on traffic
- **CDN**: Enable for global performance
- **Monitoring**: Set up detailed metrics
- **Backups**: Configure automatic backups

## 🔒 Security Considerations

1. **Environment Variables**
   - Never commit sensitive data
   - Use Railway's environment variable feature
   - Secure API keys and credentials

2. **HTTPS**
   - Railway provides automatic HTTPS
   - Ensure all external calls use HTTPS

3. **Input Validation**
   - Validate all user inputs
   - Implement rate limiting if needed
   - Sanitize data before processing

## 📈 Railway vs Render Comparison

### Railway Advantages:
- **Easier Setup**: More intuitive interface
- **Better Free Tier**: More generous limits
- **Faster Deployments**: Optimized build process
- **Better Logs**: Real-time log streaming
- **Auto-scaling**: Built-in scaling features

### Render Advantages:
- **More Mature**: Established platform
- **Custom Domains**: Better domain management
- **Static Sites**: Better for frontend-only apps

## 🎯 Next Steps

1. **Monitor Performance**
   - Track response times
   - Monitor error rates
   - Set up alerts

2. **Optimize Models**
   - Consider model compression
   - Implement caching strategies
   - Optimize feature engineering

3. **Add Features**
   - User authentication
   - Result history
   - API endpoints
   - Mobile app integration

## 📞 Support Resources

- **Railway Documentation**: [docs.railway.app](https://docs.railway.app)
- **Railway Discord**: [discord.gg/railway](https://discord.gg/railway)
- **GitHub Issues**: Report bugs in your repository
- **Stack Overflow**: Tag with `railway` and `flask`

---

## 🚂 **Railway-Specific Features**

### 1. **Automatic Deployments**
- Every push to main branch triggers deployment
- Preview deployments for pull requests
- Rollback to previous versions easily

### 2. **Environment Management**
- Separate environments for dev/staging/prod
- Environment-specific variables
- Easy switching between environments

### 3. **Monitoring & Logs**
- Real-time log streaming
- Performance metrics
- Error tracking and alerting

### 4. **Scaling**
- Automatic scaling based on traffic
- Manual scaling controls
- Resource usage optimization

---

**🎉 Congratulations! Your Heart Attack Risk Prediction app is now deployed on Railway!**

**🌐 Access it at**: `https://your-app-name.railway.app`

**🔄 Auto-deploy**: Every push to main branch will trigger a new deployment

**📊 Monitoring**: Real-time logs and performance metrics available in Railway dashboard
