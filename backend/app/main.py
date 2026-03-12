from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router

app = FastAPI(title="SafeCrow API", description="AI powered escrow service backend", version="1.0.0")

# Set up CORS for React frontend (assuming default dev ports)
origins = [
    "http://localhost:3000",
    "http://localhost:5173", # Vite default
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to SafeCrow API"}
