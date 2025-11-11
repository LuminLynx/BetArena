#!/bin/bash

# BetArena AWS EC2 Setup Script
# Run this after SSH-ing into your EC2 instance

set -e

echo "🚀 Starting BetArena AWS Setup..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
newgrp docker

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install Git
sudo apt install git -y

# Install AWS CLI
sudo apt install awscli -y

# Create app directory
mkdir -p ~/betarena && cd ~/betarena

# Clone repository
git clone https://github.com/LuminLynx/BetArena.git .

# Create .env file
cat > .env << 'EOF'
# Database Configuration
DATABASE_URL=postgresql+psycopg2://betarena:PASSWORD@RDS_ENDPOINT:5432/betarena
POSTGRES_DB=betarena
POSTGRES_USER=betarena
POSTGRES_PASSWORD=betarena123

# API Configuration
ENV=production
LOG_LEVEL=INFO

# Frontend Configuration
NEXT_PUBLIC_API_URL=http://EC2_IP:8000
EOF

echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Edit .env file with your credentials:"
echo "   nano .env"
echo ""
echo "2. Update these values in .env:"
echo "   - DATABASE_URL with your RDS credentials"
echo "   - NEXT_PUBLIC_API_URL with your EC2 public IP"
echo ""
echo "3. Start the application:"
echo "   docker-compose up -d"
echo ""
echo "4. Your app will be available at:"
echo "   Web: http://YOUR_EC2_IP:3000"
echo "   API: http://YOUR_EC2_IP:8000"
