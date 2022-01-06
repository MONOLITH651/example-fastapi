from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from app import database





# models.Base.metadata.create_all(bind=engine)



app = FastAPI()

# origins = ["https://www.google.com"]
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    # function that runs before every request
    allow_origins=origins,
    # what domains
    allow_credentials=True,
    allow_methods=["*"],
    # what type of methods are allowed
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/") 
def root():
    return {"message": "Hello World"}



