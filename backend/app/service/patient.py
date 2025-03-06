from app.persistence.modelRepository.patient import PatientRepository
from app.models.patient import Patient
from app.api.v1.schemas.patient import PostPatientModel, UpdatePatientModel
from sqlalchemy.ext.asyncio import AsyncSession

class Facade:
    def __init__(self):
        self.patient_repo = PatientRepository()

    async def add_patient(self, Model: PostPatientModel, session: AsyncSession):
        patient = Patient(
            id=Model.id,
            fname=Model.fname,
            lname=Model.lname,
            created_at=Model.created_at,
            updated_at=Model.updated_at
        )
        await self.patient_repo.add(obj=patient, session=session)
        return patient
    
    async def get_patient(self, patient_id, session: AsyncSession):
        return await self.patient_repo.get(obj_id=patient_id, session=session)

    async def get_all_patients(self, session: AsyncSession):
        return await self.patient_repo.get_all(session=session)
    
    async def update_patient(self, Model: UpdatePatientModel, patient_id, session: AsyncSession):
        return await self.patient_repo.update(obj=Model, obj_id=patient_id, session=session)

    async def delete_patient(self, patient_id, session: AsyncSession):
        return await self.patient_repo.delete(obj_id=patient_id, session=session)

    