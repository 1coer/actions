from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from db import engine


def get_db_session():
    with Session(engine) as session:
        yield session


DBDep = Annotated[Session, Depends(get_db_session)]
