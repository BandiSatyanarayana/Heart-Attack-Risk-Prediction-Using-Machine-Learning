# ⚡ Deploy Heart Attack Risk Prediction on Vercel

This guide will walk you through deploying your Heart Attack Risk Prediction application on Vercel's serverless platform.

## 📋 Prerequisites

- GitHub account with your project repository
- Vercel account (free tier available)
- Python 3.8+ project ready for deployment

## 🛠️ Pre-deployment Setup

### 1. Project Structure for Vercel
```
Heart-Attack-Risk-Prediction-lnm71a/
├── api/                    # Serverless functions
│   └── predict.py         # Main API endpoint
├── models/                # Pre-trained ML models
├── vercel.json           # Vercel configuration
├── requirements-vercel.txt # Optimized dependencies
└── .gitignore            # Git ignore file
```

### 2. Key Changes Made for Vercel
- ✅ Created `vercel.json` for Vercel configuration
- ✅ Converted Flask app to serverless function
- ✅ Created `api/predict.py` for API endpoint
- ✅ Optimized `requirements-vercel.txt` for serverless
- ✅ Added CORS support for cross-origin requests

## 🚀 Deployment Steps

### Step 1: Push Changes to GitHub

```bash
# Add all new files
git add .

# Commit changes
git commit -m "Prepare for Vercel deployment - Add serverless functions and Vercel config"

# Push to GitHub
git push origin main
```

### Step 2: Deploy on Vercel

1. **Sign up/Login to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign up with your GitHub account

2. **Import Project**
   - Click "New Project"
   - Import your GitHub repository: `Heart-Attack-Risk-Prediction-Using-Machine-Learning`

3. **Configure Project**
   - **Framework Preset**: Other
   - **Root Directory**: `Heart-Attack-Risk-Prediction-lnm71a`
   - **Build Command**: Leave empty (Vercel auto-detects)
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements-vercel.txt`

4. **Environment Variables (Optional)**
   - No environment variables needed for basic deployment

5. **Deploy**
   - Click "Deploy"
   - Vercel will automatically build and deploy your app

## 🔧 Vercel Configuration Details

### vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/predict.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/predict",
      "dest": "api/predict.py"
    },
    {
      "src": "/(.*)",
      "dest": "index.html"
    }
  ],
  "functions": {
    "api/predict.py": {
      "maxDuration": 30
    }
  }
}
```

### requirements-vercel.txt (Optimized)
```
numpy==2.2.6
pandas==2.2.3
scikit_learn==1.6.1
joblib==1.5.0
```

## 🌐 Post-Deployment

### 1. Access Your Application
- Vercel will provide a URL like: `https://your-app-name.vercel.app`
- Your app will be accessible from anywhere on the internet

### 2. API Endpoints
- **Main App**: `https://your-app-name.vercel.app/`
- **API Endpoint**: `https://your-app-name.vercel.app/api/predict`

### 3. Monitor Deployment
- Check the "Functions" tab for serverless function logs
- Monitor "Analytics" for performance
- View real-time logs in Vercel dashboard

## 🔍 Troubleshooting

### Common Issues:

1. **Build Failures**
   - Check `requirements-vercel.txt` for compatibility
   - Ensure all dependencies are available
   - Check Python version compatibility

2. **Function Timeout**
   - Vercel has 10-second timeout for free tier
   - Model loading may take time on first request
   - Consider upgrading to Pro plan for longer timeouts

3. **Model Loading Issues**
   - Ensure model files are included in deployment
   - Check file paths in `api/predict.py`
   - Models are cached between invocations

4. **CORS Issues**
   - API includes CORS headers for cross-origin requests
   - Check browser console for CORS errors

### Debug Commands:
```bash
# Test locally with Vercel CLI
npm i -g vercel
vercel dev

# Test API endpoint
curl -X POST https://your-app-name.vercel.app/api/predict \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","age":45,"totChol":200,"sysBP":120,"diaBP":80,"BMI":25.0,"heartRate":72,"glucose":100,"model":"knn"}'
```

## 📊 Performance Optimization

### For Free Tier:
- **Function Size**: Keep under 50MB total
- **Dependencies**: Minimize packages in requirements
- **Cold Start**: First request may be slower
- **Timeout**: 10-second limit for free tier

### For Paid Plans:
- **Pro Plan**: 60-second timeout, better performance
- **Enterprise**: Custom limits and dedicated resources

## 🔒 Security Considerations

1. **Input Validation**
   - All inputs are validated in the API
   - Range checks for health parameters
   - Model selection validation

2. **HTTPS**
   - Vercel provides automatic HTTPS
   - All requests are encrypted

3. **Rate Limiting**
   - Vercel includes basic rate limiting
   - Consider additional rate limiting for production

## 📈 Vercel vs Render Comparison

### Vercel Advantages:
- **Serverless**: Pay only for what you use
- **Global CDN**: Faster worldwide access
- **Auto-scaling**: Handles traffic spikes automatically
- **Better for APIs**: Optimized for serverless functions

### Render Advantages:
- **Long-running processes**: Better for traditional web apps
- **More generous free tier**: 750 hours/month
- **Simpler setup**: Less configuration needed

## 🎯 Next Steps

1. **Monitor Performance**
   - Track function execution times
   - Monitor cold start performance
   - Set up alerts for errors

2. **Optimize Models**
   - Consider model compression for faster loading
   - Implement caching strategies
   - Optimize for serverless environment

3. **Add Features**
   - User authentication
   - Result history
   - Additional API endpoints
   - Mobile app integration

## 📞 Support Resources

- **Vercel Documentation**: [vercel.com/docs](https://vercel.com/docs)
- **Vercel Community**: [github.com/vercel/vercel/discussions](https://github.com/vercel/vercel/discussions)
- **GitHub Issues**: Report bugs in your repository
- **Stack Overflow**: Tag with `vercel` and `serverless`

---

## ⚡ **Vercel-Specific Features**

### 1. **Serverless Functions**
- Automatic scaling based on demand
- Pay only for execution time
- Global edge network deployment

### 2. **Edge Network**
- Deployed to multiple regions worldwide
- Automatic CDN for static assets
- Reduced latency for global users

### 3. **Real-time Analytics**
- Function execution metrics
- Performance monitoring
- Error tracking and alerting

### 4. **Git Integration**
- Automatic deployments on push
- Preview deployments for pull requests
- Easy rollback to previous versions

---

**🎉 Congratulations! Your Heart Attack Risk Prediction app is now deployed on Vercel!**

**🌐 Access it at**: `https://your-app-name.vercel.app`

**🔄 Auto-deploy**: Every push to main branch will trigger a new deployment

**⚡ Serverless**: Your app scales automatically with traffic!
