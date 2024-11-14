from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .init_config import startup_handler,shutdown_handler
from .Routes.AuthRoutes import  auth_router 



app = FastAPI(
    title="TaskRabbit Backend"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router,prefix="/api/v1")

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.add_event_handler("startup", startup_handler)
app.add_event_handler("shutdown", shutdown_handler)



