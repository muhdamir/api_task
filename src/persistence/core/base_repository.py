from typing import Generic, TypeVar

from fastapi import Depends
from sqlalchemy.orm import Session

from domain.entities import Base
from infrastructure.db import get_session

Entity = TypeVar("Entity", bound=Base)
T = TypeVar("T")


class BaseRepository(
    Generic[Entity],
):
    """
    >>> SampleClas(BaseRepository[SampleEntity]):
    ...     entity = SampleEntity
    """

    entity: type[Entity]

    def __init__(
        self,
        session: Session = Depends(get_session),
    ) -> None:
        self.session = session

    def get_by_id(
        self,
        id_: int,
    ):
        return self.session.query(self.entity).get(ident=id_)

    def get_all(
        self,
    ):
        return self.session.query(self.entity).all()

    # def create(
    #     self,
    # ):
    #     ...

    # def update(
    #     self,
    # ):
    #     ...

    # def delete(
    #     self,
    # ):
    #     ...
