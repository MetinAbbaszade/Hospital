from app.models.specialization import Specialization
from app.persistence.repository import Repository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select


class SpecializationRepository(Repository):
    def __init__(self):
        super().__init__(Specialization)

    async def get_specialization_by_name(self, name: str, session: AsyncSession):
        return session.execute(select(self.model).where(self.model.name == name)).scalars().first()