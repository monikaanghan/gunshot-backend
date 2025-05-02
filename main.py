from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import gunshot, log_event, microphone, websocket
from app.utils.database import create_tables
from app.utils.database import engine


app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(gunshot.router)
app.include_router(log_event.router)
app.include_router(microphone.router)
app.include_router(websocket.router)

@app.on_event("startup")
async def startup():
    await create_tables()

@app.on_event("shutdown")
async def shutdown():
    print("Shutting down the application...")
    # Close the database engine
    await engine.dispose()
    print("Database connections closed.")