import uuid
from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str


class ItemBase(SQLModel):
    name: str = Field(max_length=128)
    description: str = Field(default="", max_length=255)


class Item(ItemBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class ItemPublic(ItemBase):
    id: uuid.UUID


class ItemCreate(ItemBase):
    pass
