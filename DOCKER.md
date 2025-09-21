# 🐳 Docker Containerization Guide

This guide explains how to containerize and deploy the Mental Wellness Prediction App using Docker.

## 📋 Prerequisites

- Docker installed on your system
- Docker Compose (optional, for easier deployment)

## 🚀 Quick Start

### Option 1: Using Docker Compose (Recommended)

```bash
# Build and run the application
docker-compose up --build

# Run in background
docker-compose up -d --build
```

### Option 2: Using Docker Commands

```bash
# Build the image
docker build -t mental-wellness-app:latest .

# Run the container
docker run -p 8501:8501 mental-wellness-app:latest
```

## 🛠️ Build Scripts

### Windows
```bash
# Run the Windows build script
build.bat
```

### Linux/Mac
```bash
# Make script executable and run
chmod +x build.sh
./build.sh
```

## 📁 Container Structure

```
/app/
├── app.py                          # Main Streamlit application
├── data.csv                        # Training dataset
├── mental_wellness_model.pkl       # Trained ML model
├── requirements.txt                # Python dependencies
└── run_tests.py                   # Test runner
```

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `STREAMLIT_SERVER_PORT` | 8501 | Port for Streamlit server |
| `STREAMLIT_SERVER_ADDRESS` | 0.0.0.0 | Server address |
| `STREAMLIT_BROWSER_GATHER_USAGE_STATS` | false | Disable usage statistics |

### Ports

- **8501**: Streamlit web interface

## 🏥 Health Checks

The container includes health checks that monitor:
- Application startup
- Streamlit server availability
- Response time

## 🔒 Security Features

- **Non-root user**: App runs as `app` user instead of root
- **Read-only data**: Data volume mounted as read-only
- **Minimal base image**: Uses Python slim image
- **No unnecessary packages**: Clean dependency installation

## 📊 Monitoring

### View Logs
```bash
# Using docker-compose
docker-compose logs -f

# Using docker
docker logs -f <container_name>
```

### Check Health
```bash
# Check container status
docker ps

# Inspect health check
docker inspect <container_name> | grep -A 10 Health
```

## 🚀 Deployment Options

### 1. Local Development
```bash
docker-compose up
```
Access: http://localhost:8501

### 2. Production Deployment
```bash
# Build production image
docker build -t mental-wellness-app:prod .

# Run with production settings
docker run -d \
  --name mental-wellness-prod \
  -p 8501:8501 \
  --restart unless-stopped \
  mental-wellness-app:prod
```

### 3. Cloud Deployment

#### AWS ECS
```bash
# Tag for ECR
docker tag mental-wellness-app:latest <account>.dkr.ecr.<region>.amazonaws.com/mental-wellness-app:latest

# Push to ECR
docker push <account>.dkr.ecr.<region>.amazonaws.com/mental-wellness-app:latest
```

#### Google Cloud Run
```bash
# Build for Cloud Run
docker build -t gcr.io/<project-id>/mental-wellness-app .

# Push to Container Registry
docker push gcr.io/<project-id>/mental-wellness-app
```

#### Azure Container Instances
```bash
# Build and push to Azure Container Registry
az acr build --registry <registry-name> --image mental-wellness-app:latest .
```

## 🧪 Testing

### Run Tests in Container
```bash
# Build test image
docker build -t mental-wellness-test .

# Run tests
docker run --rm mental-wellness-test python run_tests.py
```

### Interactive Testing
```bash
# Run container with shell access
docker run -it --rm mental-wellness-app:latest /bin/bash

# Run tests interactively
python run_tests.py
```

## 🔧 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Find process using port 8501
   netstat -tulpn | grep 8501
   
   # Kill process or use different port
   docker run -p 8502:8501 mental-wellness-app:latest
   ```

2. **Permission denied**
   ```bash
   # Check file permissions
   ls -la data.csv mental_wellness_model.pkl
   
   # Fix permissions
   chmod 644 data.csv mental_wellness_model.pkl
   ```

3. **Container won't start**
   ```bash
   # Check logs
   docker logs <container_name>
   
   # Run interactively for debugging
   docker run -it --rm mental-wellness-app:latest /bin/bash
   ```

### Performance Optimization

1. **Multi-stage builds** (for production)
2. **Image size optimization**
3. **Resource limits**
4. **Caching strategies**

## 📈 Scaling

### Horizontal Scaling
```yaml
# docker-compose.override.yml
version: '3.8'
services:
  mental-wellness-app:
    deploy:
      replicas: 3
    ports:
      - "8501-8503:8501"
```

### Load Balancing
Use nginx or traefik for load balancing multiple instances.

## 🔄 CI/CD Integration

### GitHub Actions Example
```yaml
name: Build and Deploy
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build Docker image
        run: docker build -t mental-wellness-app .
      - name: Run tests
        run: docker run --rm mental-wellness-app python run_tests.py
```

## 📚 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Streamlit Deployment](https://docs.streamlit.io/streamlit-community-cloud)
- [Docker Compose Reference](https://docs.docker.com/compose/)
