from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.user import User

from routes import auth, ai, destinations, user, weather, agent


load_dotenv()

app = FastAPI(title="Roamly API", version="1.0.0")


limiter = Limiter(key_func=get_remote_address, default_limits=["100/15minutes"])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db():
    uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017/roamly")
    client = AsyncIOMotorClient(uri)
    await init_beanie(database=client.get_default_database(), document_models=[User])
    print("✅ MongoDB connected and Beanie initialized")

app.include_router(auth.router,         prefix="/api/auth")
app.include_router(ai.router,           prefix="/api/ai")
app.include_router(destinations.router, prefix="/api/destinations")
app.include_router(user.router,         prefix="/api/user")
app.include_router(weather.router,      prefix="/api/weather")
app.include_router(agent.router,        prefix="/api/ai/agent")
from routes.analytics import router as analytics_router
app.include_router(analytics_router, prefix="/api/admin")

@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "🌍 Roamly API is running"}


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 5000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
