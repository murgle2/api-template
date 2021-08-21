from sqlalchemy.orm import Session
from app import model, schema


class User():
    def get_user(user_id: int, db: Session):
        return db.query(model.User).filter(model.User.id == user_id).first()

    def get_user_by_email(email: str, db: Session):
        return db.query(model.User).filter(model.User.email == email).first()

    def create_user(user: schema.User, db: Session):
        db_user = model.User(username=user.username, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
