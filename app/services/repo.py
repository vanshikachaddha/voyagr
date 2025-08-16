from typing import TypeVar, Generic, Optional
from sqlalchemy.orm import Session

T = TypeVar('T')

# Users
class BaseRepo():
    @staticmethod

    def insert(db: Session, model: Generic[T]):
        db.add(model)
        db.commit()
        db.refresh(model)

class UsersRepo(BaseRepo):
    @staticmethod

    def find_username(db: Session, model: Generic[T], username: str):
        return db.query(model).filter(model.username == username).first()




