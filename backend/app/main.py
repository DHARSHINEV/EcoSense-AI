"""
EcoSense AI - Main FastAPI Application Server.
Track: Smart Buildings – Energy Efficiency & Occupant Experience.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.api.endpoints import router
from app.data_store.db import data_store

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize deterministic simulation, baseline, ML forecast, and optimizations on startup
    print("Initializing EcoSense AI building simulation engine...")
    data_store.initialize()
    print("EcoSense AI initialization complete. Ready to serve requests.")
    yield

app = FastAPI(
    title="EcoSense AI API",
    description="Intelligent Building Energy Optimizer REST API",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS for Next.js frontend (default port 3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
