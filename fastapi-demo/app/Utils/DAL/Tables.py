from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, UUID,String
from sqlalchemy import event
import uuid
import hashlib
import os

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ ="users"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4(),index=True, primary_key=True)
    fullname = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

@event.listens_for(User,"before_insert")
def encrypt_password(mapper, connect, target):
    salt = os.urandom(32)
    hash_object = hashlib.sha256()
    hash_object.update(salt + target.password.encode())
    target.password = hash_object.hexdigest()
    