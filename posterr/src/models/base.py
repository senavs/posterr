from typing import Any, Optional

from ..database.client import DatabaseClient


class BaseModel:

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def search(cls, connection: DatabaseClient, id: int) -> 'BaseModel':
        return connection.query(cls).get(id)

    def insert(self, connection: DatabaseClient, *, flush: bool = False, commit: bool = True):
        connection.add(self)
        if flush:
            connection.flush()
        if commit:
            connection.commit()

    def to_dict(self, *, exclude: Optional[list] = None, **include) -> dict:
        if not exclude:
            exclude = []

        attrs = {attr.lower(): getattr(self, attr) for attr in self.__dir__() if attr.isupper() and attr not in exclude}
        attrs.update(**include)
        return attrs

    def __repr__(self):
        return f"{type(self).__qualname__}({self.to_dict()})"
