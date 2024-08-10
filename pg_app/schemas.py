from pydantic import BaseModel

class UserBase(BaseModel):
	nombre: str
	edad: str
	tipo: str

class UserCreate(UserBase):
	pass

class User(UserBase):
	id: int

	class Config:
		orm_mode = True