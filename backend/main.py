import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.user import User

from routes import auth, ai, destinations, user, weather, agent

load_dotenv()

app = FastAPI(title="Roamly API", version="1.0.0")

# --- GLOBAL STORAGE FOR DB CLIENT ---
# This allows us to access the client across the app and close it on shutdown
db_client: AsyncIOMotorClient | None = None

# --- CORE LIVENESS & HEALTH ROUTES ---

@app.get("/")
def home():
    return {"message": "Roamly backend is running smoothly 🚀"}


@app.get("/api/health")
def health_check():
    # Render-optimized liveness probe (lightweight and lightning fast)
    return {"status": "ok", "service": "roamly"}

# -------------------------------------

# Rate Limiter Configuration
limiter = Limiter(key_func=get_remote_address, default_limits=["100/15minutes"])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Predictable, Production-Safe CORS Setup
if not os.getenv("FRONTEND_URL"):
    print("⚠️ FRONTEND_URL not set — CORS will be restrictive only for localhost")

allowed_origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]

if os.getenv("FRONTEND_URL"):
    allowed_origins.append(os.getenv("FRONTEND_URL"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- APPLICATION LIFECYCLE HOOKS ---

@app.on_event("startup")
async def startup_db():
    global db_client
    uri = os.getenv("MONGODB_URI")
    if not uri:
        raise RuntimeError("CRITICAL STARTUP FAILURE: MONGODB_URI is missing from environment variables.")

    try:
        # Motor internally handles retries for brief network fluctuations
        db_client = AsyncIOMotorClient(uri)
        db = db_client.get_database("roamly")
        
        await init_beanie(database=db, document_models=[User])
        print("✅ MongoDB connected and Beanie initialized securely")
        
    except Exception as e:
        print("❌ CRITICAL: Database connection failed during startup loop!")
        print(f"Error Details: {e}")
        # Fail-fast to protect live traffic via Render's deployment safety mechanism
        raise e


@app.on_event("shutdown")
async def shutdown_db():
    global db_client
    if db_client:
        print("🛑 Closing MongoDB connection pool gracefully...")
        db_client.close()

# -------------------------------------

# Include Routers
app.include_router(auth.router,         prefix="/api/auth")
app.include_router(ai.router,           prefix="/api/ai")
app.include_router(destinations.router, prefix="/api/destinations")
app.include_router(user.router,         prefix="/api/user")
app.include_router(weather.router,      prefix="/api/weather")
app.include_router(agent.router,        prefix="/api/ai/agent")

from routes.analytics import router as analytics_router
app.include_router(analytics_router, prefix="/api/admin")


# Local debugging utility (Ignored by Render)
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 5000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)