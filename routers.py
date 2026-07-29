from fastapi import APIRouter, status
from sqlmodel import select

from models import ItemPublic, ItemCreate, Item
from deps import DBDep


router = APIRouter(prefix="/items", tags=["Items"])

@router.post("", response_model=ItemPublic, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: DBDep):
    item_db = Item.model_validate(item)
    db.add(item_db)
    db.commit()
    db.refresh(item_db)
    return item_db


@router.get("", response_model=list[ItemPublic])
def list_items(db: DBDep):
    items = db.exec(select(Item)).all()
    return items
