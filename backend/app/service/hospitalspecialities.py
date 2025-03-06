from app.persistence.modelRepository.hospitalspecialization import HospitalSpecializationRepository
from app.models.hospitalspecialization import HospitalSpecialization
from app.api.v1.schemas.hospitalspecialization import PostHospitalSpecializationModel, UpdateHospitalSpecializationModel
from sqlalchemy.ext.asyncio import AsyncSession

class Facade:
    def __init__(self):
        self.hospitalspecialization_repo = HospitalSpecializationRepository()

    async def add_hospitalspecialization(self, Model: PostHospitalSpecializationModel, session: AsyncSession):
        data = Model.model_dump()
        hospitalspecialization = HospitalSpecialization(**data)
        await self.hospitalspecialization_repo.add(obj=hospitalspecialization, session=session)
        return hospitalspecialization

    async def get_all_hospitalspecializations(self, session: AsyncSession):
        return await self.hospitalspecialization_repo.get_all(session=session)

    async def get_hospitalspecialization(self, hospitalspecialization_id, session: AsyncSession):
        return await self.hospitalspecialization_repo.get(obj_id=hospitalspecialization_id, session=session)

    async def get_hospitalspecialization_by_hospital(self, hospital_id, session: AsyncSession):
        return await self.hospitalspecialization_repo.get_hospitalspecialization_by_hospital(hospital_id=hospital_id, session=session)

    async def get_hospitalspecialization_by_specialization(self, specialization_id, session: AsyncSession):
        return await self.hospitalspecialization_repo.get_hospitalspecialization_by_specialization(specialization_id=specialization_id, session=session)

    async def update_hospitalspecialization(self, Model: UpdateHospitalSpecializationModel, hospitalspecialization_id, session: AsyncSession):
        return await self.hospitalspecialization_repo.update(obj_id=hospitalspecialization_id, obj=Model, session=session)

    async def delete_hospitalspecialization(self, hospitalspecialization_id, session: AsyncSession):
        return await self.hospitalspecialization_repo.delete(obj_id=hospitalspecialization_id, session=session)

    async def delete_hospitalspecialization_by_hospital(self, hospital_id, session: AsyncSession):
        return await self.hospitalspecialization_repo.delete_hospitalspecialization_by_hospital(hospital_id=hospital_id, session=session)

    async def delete_hospitalspecialization_by_specialization(self, specialization_id, session: AsyncSession):
        return await self.hospitalspecialization_repo.delete_hospitalspecialization_by_specialization(specialization_id=specialization_id, session=session)