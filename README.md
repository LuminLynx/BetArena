# BetArena

Sports betting suggestions app - Monorepo scaffolding

## 🚀 Quick Start

```bash
# Start all services
docker compose up --build

# Services will be available at:
# - API: http://localhost:8000
# - Web: http://localhost:3000
# - Adminer (DB UI): http://localhost:8080
# - PostgreSQL: localhost:5432
```

## 🏥 Health Checks

```bash
# API health endpoint
curl http://localhost:8000/healthz

# Web health endpoint
curl http://localhost:3000/api/healthz
```

## 📁 Structure

```
BetArena/
├── apps/
│   ├── backend/       # FastAPI backend
│   └── web/          # Next.js frontend
├── .github/
│   └── workflows/    # CI/CD pipelines
└── docker-compose.yaml
```

## 🛠️ Development

### Backend (FastAPI)
```bash
cd apps/backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend (Next.js)
```bash
cd apps/web
npm install
npm run dev
```

## License

MIT License - see [LICENSE](LICENSE) for details

