from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

class AbstractRepository(ABC):
    @abstractmethod
    async def add(self, obj, session: AsyncSession):
        ...

    @abstractmethod
    async def get(self, obj_id, session: AsyncSession):
        ...

    @abstractmethod
    async def get_all(self, session: AsyncSession):
        ...

    @abstractmethod
    async def update(self, obj_id, obj, session: AsyncSession):
        ...
    
    @abstractmethod
    async def delete(self, obj_id, session: AsyncSession):
        ...