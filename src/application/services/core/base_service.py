from typing import Generic, TypeVar

from application.exceptions.app_exceptions import IdNotFound
from persistence.core import BaseRepository

Repository = TypeVar("Repository", bound=BaseRepository)


class BaseService(
    Generic[Repository],
):
    def __init__(
        self,
        repository: Repository,
    ) -> None:
        self.repository = repository

    def get_by_id(
        self,
        id_: int,
    ):
        if data := self.repository.get_by_id(id_=id_):
            return data

        raise IdNotFound(id_=id_)

    def get_all(
        self,
    ):
        return self.repository.get_all()
