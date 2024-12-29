from pydantic import BaseModel

'''define data types of each columns'''
class User(BaseModel):
    username: str
    location: str | None
    bio: str | None
    public_repos: int
    following: int
    followers: int

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    location: str | None
    bio: str | None