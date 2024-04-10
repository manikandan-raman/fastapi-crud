import uuid

from sqlalchemy import BOOLEAN, INT, TEXT, TIMESTAMP, UUID, VARCHAR, Column, func

from db.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(VARCHAR(100))
    age = Column(INT, nullable=True)
    is_qualified = Column(BOOLEAN, default=False)
    email = Column(VARCHAR(255), unique=True)
    password = Column(TEXT)
    created_at = Column(TIMESTAMP, default=func.now())
