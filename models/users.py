import uuid

from db.database import Base
from sqlalchemy import Column, UUID, VARCHAR, INT, BOOLEAN, TIMESTAMP, func


class Users(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(VARCHAR(100))
    age = Column(INT, nullable=True)
    is_qualified = Column(BOOLEAN, default=False)
    created_at = Column(TIMESTAMP, default=func.now())
