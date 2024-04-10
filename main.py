from fastapi import FastAPI

from routers import auth, users

# from db.database import engine
# from models import users as users_model

# users_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "success"}
