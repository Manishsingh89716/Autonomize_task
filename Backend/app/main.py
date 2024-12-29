'''import all required libraries'''

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import crud, schemas, services, models, database

'''intialize the app'''

app = FastAPI()

'''the application starts running and is initializing its components'''

@app.on_event("startup")
def startup():
    database.Base.metadata.create_all(bind=database.engine)

'''get the database'''
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

'''define users endpoint'''

@app.post("/users/", response_model=schemas.User)
def create_user(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=username)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    user_data = services.fetch_github_user(username)
    return crud.create_user(db=db, user=user_data)

'''define endpoint that get the user details by name'''

@app.get("/users/{username}", response_model=schemas.User)
def read_user(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=username)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

'''define the endpoint that get the all users detail'''

@app.get("/users/", response_model=list[schemas.User])
def list_users(sort_by: str = None, db: Session = Depends(get_db)):
    return crud.get_users(db, sort_by)

'''define the endpoint that update users and details'''

@app.put("/users/{username}", response_model=schemas.User)
def update_user(username: str, updates: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db, db_user, updates)

'''define endpoint that delete the existing users'''

@app.delete("/users/{username}")
def delete_user(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db, db_user)
    return {"message": "User deleted successfully"}