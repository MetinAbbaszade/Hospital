from app.persistence.modelRepository.doctor import DoctorRepository
from app.models.doctor import Doctor
from app.api.v1.schemas.doctor import PostDoctorModel, UpdateDoctorModel
from sqlalchemy.ext.asyncio import AsyncSession
#Doctor facade

class Facade:

    def __init__(self):
        self.doctor_repo = DoctorRepository()

    async def add_doctor(self, Model: PostDoctorModel, session: AsyncSession):
        doctor = Doctor(
            id=Model.id,
            hospital_id=Model.hospital_id,
            fname=Model.fname,
            lname=Model.lname,
            phone_num=Model.phone_num,
            experience=Model.experience,
            created_at=Model.created_at,
            updated_at=Model.updated_at
        )
        await self.doctor_repo.add(obj=doctor, session=session)
        return doctor

    async def get_all_doctors(self, session: AsyncSession):
        return await self.doctor_repo.get_all(session=session)

    async def get_doctor(self, doctor_id, session: AsyncSession):
        return await self.doctor_repo.get(obj_id=doctor_id, session=session)
    
    async def update_doctor(self, Model: UpdateDoctorModel, doctor_id, session: AsyncSession):
        return await self.doctor_repo.update(obj=Model, obj_id=doctor_id, session=session)

    async def delete_doctor(self, doctor_id, session: AsyncSession):
        return await self.doctor_repo.delete(obj_id=doctor_id, session=session)
    
    async def get_doctor_by_hospital(self, hospital_id, session: AsyncSession):
        return await self.doctor_repo.get_doctor_by_hospital(hospital_id=hospital_id, session=session)
    
    async def get_doctor_by_specialization(self, specialization, session: AsyncSession):
        return await self.doctor_repo.get_doctor_by_specialities(specialization=specialization, session=session)