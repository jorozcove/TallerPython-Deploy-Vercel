from sqlalchemy import Column, Integer, String

from .database import Base

class User(Base):
	__tablename__ = "usuarios"

	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String, index=True)
	edad = Column(String, index=True)
	tipo = Column(String, index=True)