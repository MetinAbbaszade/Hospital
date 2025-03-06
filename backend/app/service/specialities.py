from app.persistence.modelRepository.specialization import SpecializationRepository
from app.models.specialization import Specialization
from app.api.v1.schemas.specialization import PostSpecialization, UpdateSpecialization
from sqlalchemy.ext.asyncio import AsyncSession


class Facade:
    def __init__(self):
        self.specialization_repo = SpecializationRepository()

    async def add_specialization(self, Model: PostSpecialization, session: AsyncSession):
        data = Model.model_dump()
        specialization = Specialization(**data)
        await self.specialization_repo.add(obj=specialization, session=session)
        return specialization
    
    async def get_all_specializations(self, session: AsyncSession):
        return await self.specialization_repo.get_all(session=session)
    
    async def get_specialization(self, specialization_id, session: AsyncSession):
        return await self.specialization_repo.get(obj_id=specialization_id, session=session)
    
    async def get_specialization_by_name(self, name, session: AsyncSession):
        return await self.specialization_repo.get_specialization_by_name(name=name, session=session)
    
    async def update_specialization(self, Model: UpdateSpecialization, specialization_id, session: AsyncSession):
        return await self.specialization_repo.update(obj_id=specialization_id, obj=Model, session=session)
    
    async def delete_specialization(self, specialization_id, session: AsyncSession):
        return await self.specialization_repo.delete(obj_id=specialization_id, session=session)
    