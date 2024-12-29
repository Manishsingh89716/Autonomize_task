from . import models

'''define functions for each operations i.e crud operations'''
def get_user_by_username(db, username: str):
    return db.query(models.User).filter(models.User.username == username, models.User.active == True).first()

def create_user(db, user):
    db_user = models.User(**user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db, sort_by: str = None):
    query = db.query(models.User).filter(models.User.active == True)
    if sort_by:
        query = query.order_by(getattr(models.User, sort_by))
    return query.all()

def update_user(db, db_user, updates):
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db, db_user):
    db_user.active = False
    db.commit()