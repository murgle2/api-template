from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from app import schema, crud
from app.router import dep

router = APIRouter(
    prefix="/user"
)

# DO I NEED ASYNC HERE?
# Order matters, if you had the paramter first it would fail
# @router.get("/me", status_code=status.HTTP_200_OK)
# async def read_user_me(token: str = Depends(oauth2_scheme)):
#     return {"token": token}


@router.get("/{user_id}", response_model=schema.User, status_code=status.HTTP_200_OK)
def read_user_by_id(user_id: int, db: Session = Depends(dep.get_db)):
    db_user = crud.User.get_user(user_id, db)
    return db_user


# Here, takes user from the body
# We also return same model to user. Could create
# separate in and out models with different properties
@router.post("/", response_model=schema.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schema.User, db: Session = Depends(dep.get_db)):
    db_user = crud.User.get_user_by_email(user.email, db)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.User.create_user(user, db)
