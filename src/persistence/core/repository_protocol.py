from typing import Protocol, Any
from domain.entities import Base


class Repository(Protocol):
    entity: type[Base]

    def get_by_id(
        self,
        id_: int,
    ) -> Any:
        ...

    def get_all(
        self,
    ) -> Any:
        ...
