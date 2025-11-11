# 🚀 AWS Deployment Guide

## Quick Summary

Deploy your BetArena PWA on AWS with free tier (first 12 months):
- **EC2**: t2.micro (FREE - 730 hours/month)
- **RDS**: db.t3.micro (FREE - 730 hours/month)
- **After 12 months**: ~$28/month

## Prerequisites

1. AWS Account (free tier eligible)
2. GitHub account with this repository
3. SSH key pair for EC2

## Step 1: Create AWS Account

1. Go to [aws.amazon.com](https://aws.amazon.com/free)
2. Click "Create Free Account"
3. Follow registration process
4. Verify email and payment method
5. Ensure free tier is enabled

## Step 2: Launch EC2 Instance

1. Go to **AWS Console → EC2 → Instances**
2. Click **Launch Instance**
3. Configure:
   - **Name**: betarena-app
   - **OS**: Ubuntu 24.04 LTS
   - **Type**: t2.micro (FREE)
   - **Key Pair**: Create new `betarena-key.pem` (download & save!)
   - **Storage**: 30 GB (FREE tier)
   - **Security**: Open ports 22 (SSH), 3000 (web), 8000 (api), 5432 (db)

4. Click **Launch**
5. Save the instance's **public IP address**

## Step 3: Create RDS Database

1. Go to **AWS Console → RDS → Databases**
2. Click **Create Database**
3. Configure:
   - **Engine**: PostgreSQL
   - **Free Tier Template**: Yes
   - **Instance Class**: db.t3.micro (FREE)
   - **Name**: betarena-db
   - **Master Username**: betarena
   - **Master Password**: Create strong password (save it!)
   - **Storage**: 20 GB (FREE)
   - **Public Accessibility**: Yes

4. Click **Create Database** (wait 5-10 minutes)
5. Copy the **Endpoint** (e.g., `betarena-db.xxxxx.us-east-1.rds.amazonaws.com`)

## Step 4: Create IAM User for GitHub

1. Go to **AWS Console → IAM → Users**
2. Click **Create User**
3. Name: `github-actions-betarena`
4. Click **Next**
5. Attach policies:
   - `AmazonEC2ContainerRegistryPowerUser`
   - `AmazonEC2ReadOnlyAccess`
6. Click **Create User**
7. Click the user → **Security Credentials**
8. Click **Create Access Key**
9. Select **Application running outside AWS**
10. Copy **Access Key ID** and **Secret Access Key** (save them!)

## Step 5: Configure GitHub Secrets

1. Go to your GitHub repo
2. **Settings → Secrets and variables → Actions**
3. Add these 6 secrets:

```
Name: AWS_ACCESS_KEY_ID
Value: <Your IAM Access Key>

Name: AWS_SECRET_ACCESS_KEY
Value: <Your IAM Secret Key>

Name: EC2_HOST
Value: <EC2 Public IP>

Name: EC2_USER
Value: ubuntu

Name: EC2_SSH_KEY
Value: <Contents of betarena-key.pem file>

Name: DATABASE_URL
Value: postgresql+psycopg2://betarena:PASSWORD@ENDPOINT:5432/betarena
Example: postgresql+psycopg2://betarena:MyPassword123@betarena-db.xxxxx.us-east-1.rds.amazonaws.com:5432/betarena
```

## Step 6: Set Up EC2 Instance

SSH into your EC2 instance:

```bash
ssh -i betarena-key.pem ubuntu@<EC2_PUBLIC_IP>
```

Run the setup script:

```bash
curl -O https://raw.githubusercontent.com/LuminLynx/BetArena/main/setup-ec2.sh
bash setup-ec2.sh
```

Edit the .env file with your credentials:

```bash
nano .env
```

Update these values:
```
DATABASE_URL=postgresql+psycopg2://betarena:YOUR_PASSWORD@YOUR_RDS_ENDPOINT:5432/betarena
NEXT_PUBLIC_API_URL=http://YOUR_EC2_IP:8000
```

Save and exit (Ctrl+X, then Y, then Enter).

## Step 7: Deploy!

```bash
# Push changes to main branch
git push origin main

# Watch GitHub Actions
# Go to: GitHub → Actions → Deploy to AWS

# After 5-10 minutes, your app is live!
```

## Access Your App

Once deployed:

- **Web App**: http://your-ec2-ip:3000
- **API**: http://your-ec2-ip:8000
- **API Docs**: http://your-ec2-ip:8000/docs

## Troubleshooting

### EC2 can't connect to RDS
- Check RDS security group allows EC2 on port 5432
- Test: `psql -h <rds-endpoint> -U betarena`

### GitHub Actions fails
- Check all 6 secrets are correct
- Check AWS IAM user has ECR permissions

### Docker containers won't start
- SSH to EC2: `docker ps`
- Check logs: `docker logs betarena-api`

### App not accessible
- Check EC2 security group allows ports 3000, 8000
- Verify containers are running: `docker ps`

## Useful Commands

```bash
# SSH to EC2
ssh -i betarena-key.pem ubuntu@your-ec2-ip

# Check running containers
docker ps

# View API logs
docker logs betarena-api

# View Web logs
docker logs betarena-web

# Restart API
docker restart betarena-api

# Stop everything
docker-compose down

# Start everything
docker-compose up -d
```

## Cost

First 12 months: **FREE**
After 12 months: **~$28/month**

---

**That's it! You now have a live PWA deployed to AWS! 🎉**
