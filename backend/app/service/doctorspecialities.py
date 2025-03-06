from app.persistence.modelRepository.doctorspecialization import DoctorSpecializationRepository
from app.models.doctorspecialization import DoctorSpecialization

from app.api.v1.schemas.doctorspecialization import PostDoctorSpecializationModel, UpdateDoctorSpecializationModel
from sqlalchemy.ext.asyncio import AsyncSession

class Facade:
    def __init__(self):
        self.doctorspecialization_repo = DoctorSpecializationRepository()
    async def add_doctorspecialization(self, Model: PostDoctorSpecializationModel, session: AsyncSession):
        data = Model.model_dump()
        doctorspecialization = DoctorSpecialization(**data)
        await self.doctorspecialization_repo.add(obj=doctorspecialization, session=session)
        return doctorspecialization
    
    async def get_all_doctorspecializations(self, session: AsyncSession):
        return await self.doctorspecialization_repo.get_all(session=session)
    
    async def get_doctorspecialization(self, doctorspecialization_id, session: AsyncSession):
        return await self.doctorspecialization_repo.get(obj_id=doctorspecialization_id, session=session)
    
    async def get_doctorspecialization_by_doctor(self, doctor_id, session: AsyncSession):
        return await self.doctorspecialization_repo.get_doctorspecialization_by_doctor(doctor_id=doctor_id, session=session)
    
    async def get_doctorspecialization_by_specialization(self, specialization_id, session: AsyncSession):
        return await self.doctorspecialization_repo.get_doctorspecialization_by_specialization(specialization_id=specialization_id, session=session)
    
    async def update_doctorspecialization(self, Model: UpdateDoctorSpecializationModel, doctorspecialization_id, session: AsyncSession):
        return await self.doctorspecialization_repo.update(obj_id=doctorspecialization_id, obj=Model, session=session)
    
    async def delete_doctorspecialization(self, doctorspecialization_id, session: AsyncSession):
        return await self.doctorspecialization_repo.delete(obj_id=doctorspecialization_id, session=session)
    
    async def delete_doctorspecialization_by_doctor(self, doctor_id, session: AsyncSession):
        return await self.doctorspecialization_repo.delete_doctorspecialization_by_doctor(doctor_id=doctor_id, session=session)
    
    async def delete_doctorspecialization_by_specialization(self, specialization_id, session: AsyncSession):
        return await self.doctorspecialization_repo.delete_doctorspecialization_by_specialization(specialization_id=specialization_id, session=session)
    