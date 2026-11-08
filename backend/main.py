from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import analysis, images

app = FastAPI(title="BananaSense AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(images.router)
app.include_router(analysis.router)
