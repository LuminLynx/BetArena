from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.models.league import League

app = FastAPI(title="BetArena API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthz")
async def health_check():
    """Health check endpoint"""
    return {"ok": True, "service": "api"}


@app.get("/healthz/db")
async def db_health_check(db: Session = Depends(get_db)):
    """Database health check endpoint"""
    try:
        # Try to query the database
        league_count = db.query(League).count()
        return {"ok": True, "database": "connected", "leagues_count": league_count}
    except Exception:
        # Don't expose internal error details to external users
        return {"ok": False, "database": "error"}


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to BetArena API"}
