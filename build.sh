#!/bin/bash
set -e

echo "📦 Installing dependencies..."
cd /workspaces/BetArena/apps/web
npm install

echo ""
echo "🔨 Building Next.js app..."
npm run build

echo ""
echo "✅ Build successful!"
echo ""
echo "To start the app, run:"
echo "  cd /workspaces/BetArena/apps/web && npm start"
