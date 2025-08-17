# 🚀 Deploy Heart Attack Risk Prediction Backend on Render

This guide will walk you through deploying your Heart Attack Risk Prediction Flask application on Render's free tier.

## 📋 Prerequisites

- GitHub account with your project repository
- Render account (free tier available)
- Python 3.8+ project ready for deployment

## 🛠️ Pre-deployment Setup

### 1. Project Structure
Ensure your project has these files:
```
Heart-Attack-Risk-Prediction-lnm71a/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies (includes gunicorn)
├── render.yaml           # Render deployment configuration
├── Procfile              # Process file for Render
├── .gitignore            # Git ignore file
├── models/               # Pre-trained ML models
├── templates/            # HTML templates
└── dataset/              # Training dataset
```

### 2. Key Changes Made for Deployment
- ✅ Added `gunicorn==21.2.0` to requirements.txt
- ✅ Created `render.yaml` for Render configuration
- ✅ Created `Procfile` for process management
- ✅ Modified `app.py` for production environment
- ✅ Created `.gitignore` to exclude virtual environment

## 🚀 Deployment Steps

### Step 1: Push Changes to GitHub

```bash
# Add all new files
git add .

# Commit changes
git commit -m "Prepare for Render deployment - Add gunicorn, render.yaml, Procfile"

# Push to GitHub
git push origin main
```

### Step 2: Deploy on Render

1. **Sign up/Login to Render**
   - Go to [render.com](https://render.com)
   - Sign up with your GitHub account

2. **Create New Web Service**
   - Click "New +" button
   - Select "Web Service"
   - Connect your GitHub repository

3. **Configure the Service**
   - **Name**: `heart-attack-risk-prediction` (or your preferred name)
   - **Environment**: `Python 3`
   - **Region**: Choose closest to your users
   - **Branch**: `main`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

4. **Advanced Settings (Optional)**
   - **Health Check Path**: `/`
   - **Auto-Deploy**: Enable for automatic deployments

5. **Create Web Service**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app

## 🔧 Render Configuration Details

### render.yaml
```yaml
services:
  - type: web
    name: heart-attack-risk-prediction
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.12.4
    healthCheckPath: /
    autoDeploy: true
```

### Procfile
```
web: gunicorn app:app
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
- Render will provide a URL like: `https://your-app-name.onrender.com`
- Your app will be accessible from anywhere on the internet

### 2. Monitor Deployment
- Check the "Logs" tab for any errors
- Monitor "Metrics" for performance
- Set up alerts if needed

### 3. Custom Domain (Optional)
- In Render dashboard, go to "Settings" → "Custom Domains"
- Add your domain and configure DNS

## 🔍 Troubleshooting

### Common Issues:

1. **Build Failures**
   - Check requirements.txt for compatibility
   - Ensure all dependencies are available
   - Check Python version compatibility

2. **Runtime Errors**
   - Check application logs in Render dashboard
   - Verify model files are included in deployment
   - Ensure proper file paths

3. **Memory Issues (Free Tier)**
   - Free tier has 512MB RAM limit
   - Consider optimizing large models
   - Use model compression if needed

4. **Cold Start Delays**
   - Free tier services sleep after inactivity
   - First request may take 30-60 seconds
   - Consider upgrading to paid plan for always-on service

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
   - Use Render's environment variable feature
   - Secure API keys and credentials

2. **HTTPS**
   - Render provides automatic HTTPS
   - Ensure all external calls use HTTPS

3. **Input Validation**
   - Validate all user inputs
   - Implement rate limiting if needed
   - Sanitize data before processing

## 📈 Scaling Options

### Free Tier Limitations:
- 512MB RAM
- 0.1 CPU
- Sleeps after inactivity
- 750 hours/month

### Paid Plans:
- **Starter**: $7/month - 512MB RAM, always on
- **Standard**: $25/month - 1GB RAM, auto-scaling
- **Pro**: $50/month - 2GB RAM, advanced features

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

- **Render Documentation**: [docs.render.com](https://docs.render.com)
- **Render Community**: [community.render.com](https://community.render.com)
- **GitHub Issues**: Report bugs in your repository
- **Stack Overflow**: Tag with `render` and `flask`

---

**🎉 Congratulations! Your Heart Attack Risk Prediction app is now deployed on Render!**

**🌐 Access it at**: `https://your-app-name.onrender.com`

**🔄 Auto-deploy**: Every push to main branch will trigger a new deployment
