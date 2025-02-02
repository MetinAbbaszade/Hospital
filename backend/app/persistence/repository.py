from app.persistence.abstract import AbstractRepository
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select, inspect

class Repository(AbstractRepository):
    def __init__(self, model):
        self.model = model

    async def add(self, obj, session: AsyncSession):
        session.add(obj)
        session.commit()
        session.refresh(obj)

        return obj

    async def get(self, obj_id, session: AsyncSession):
        try:
            if isinstance(obj_id, str):
                obj_id = UUID(obj_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        object = session.execute(select(self.model).where(self.model.id == obj_id)).scalars().first()
        if object:
            return {c.key: getattr(object, c.key) for c in inspect(object).mapper.column_attrs}
        else:
            return None

    async def get_all(self, session: AsyncSession):
        return session.execute(select(self.model)).scalars().all()

    async def update(self, obj_id, obj, session: AsyncSession):
        data = obj.dict()
        existing_object = self.get(obj_id=obj_id, session=session)
        for key, value in data:
            if existing_object.get(key) != value:
                setattr(existing_object, key, value)
        session.commit()
        session.refresh(existing_object)

        return existing_object

    
    async def delete(self, obj_id, session: AsyncSession):
        existing_object = session.execute(select(self.model).where(self.model.id == obj_id)).scalars().first()
        if existing_object:
            session.delete(existing_object)
            session.commit()

        else:
            raise ValueError(f'Product with ID {obj_id} not found')