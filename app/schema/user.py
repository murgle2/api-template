from typing import Optional
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    # is_active: Optional[bool] = True
    # add a field here for level of the user (mark premium users)
    # image: Optional[str] = None

    class Config:
        orm_mode = True


# This inherits above properties to reduce code
class UserVerified(User):
    email: EmailStr
    full_name: Optional[str] = None
    password: Optional[str] = None
    hashed_password: Optional[str] = None
