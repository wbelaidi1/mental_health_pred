#!/bin/bash

# Mental Wellness Prediction App - Docker Build Script

echo "🧠 Building Mental Wellness Prediction App Docker Image"
echo "======================================================"

# Build the Docker image
echo "Building Docker image..."
docker build -t mental-wellness-app:latest .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully!"
    echo ""
    echo "To run the app:"
    echo "  docker run -p 8501:8501 mental-wellness-app:latest"
    echo ""
    echo "Or use docker-compose:"
    echo "  docker-compose up"
    echo ""
    echo "The app will be available at: http://localhost:8501"
else
    echo "❌ Docker build failed!"
    exit 1
fi
