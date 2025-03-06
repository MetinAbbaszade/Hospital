from app.persistence.modelRepository.hospital import HospitalRepository
from app.models.hospital import Hospital
from app.api.v1.schemas.hospital import HospitalModel, UpdateHospitalModel

from sqlalchemy.ext.asyncio import AsyncSession

class Facade:
    def __init__(self):
            self.hospital_repo = HospitalRepository()

    async def add_hospital(self, Model: HospitalModel, session: AsyncSession):
            data = Model.model_dump()
            hospital = Hospital(**data)
            await self.hospital_repo.add(obj=hospital, session=session)
            return hospital
        
    async def get_all_hospitals(self, session: AsyncSession):
        return await self.hospital_repo.get_all(session=session)
    
    async def get_hospital(self, hospital_id, session: AsyncSession):
        return await self.hospital_repo.get(obj_id=hospital_id, session=session)
    
    async def update_hospital(self, Model: UpdateHospitalModel, hospital_id, session: AsyncSession):
        return await self.hospital_repo.update(obj_id=hospital_id, obj=Model, session=session)
    
    async def delete_hospital(self, hospital_id, session: AsyncSession):
        return await self.hospital_repo.delete(obj_id=hospital_id, session=session)
    
    async def get_hospital_by_email(self, email, session: AsyncSession):
        return await self.hospital_repo.get_hospital_by_email(email=email, session=session)
    
    async def get_hospital_by_owner(self, owner_id, session: AsyncSession):
        return await self.hospital_repo.get_hospital_by_owner(owner_id=owner_id, session=session)
        