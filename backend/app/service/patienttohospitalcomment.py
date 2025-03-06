from app.persistence.modelRepository.patienttohospitalcomment import PatientToHospitalCommentRepository
from app.models.patienttohospitalcomment import PatientToHospitalComment
from app.api.v1.schemas.patienttohospitalcomment import PostPatientToHospitalCommentModel, UpdatePatientToHospitalCommentModel
from sqlalchemy.ext.asyncio import AsyncSession

class Facade:
    def __init__(self):
        self.patienttohospitalcomment_repo = PatientToHospitalCommentRepository()

    async def get_ph_comment(self, patienttohospitalcomment_id, session: AsyncSession):
        return await self.patienttohospitalcomment_repo.get(obj_id=patienttohospitalcomment_id, session=session)
    
    async def get_all_ph_comments(self, session: AsyncSession):
        return await self.patienttohospitalcomment_repo.get_all(session=session)
    
    async def get_ph_comment_by_patient_id(self, patient_id, session: AsyncSession):
        return await self.patienttohospitalcomment_repo.get_by_patient_id(patient_id=patient_id, session=session)

    async def get_ph_comment_by_hospital_id(self, hospital_id, session: AsyncSession):
        return await self.patienttohospitalcomment_repo.get_by_hospital_id(hospital_id=hospital_id, session=session)
    
    async def add_ph_comment(self, Model: PostPatientToHospitalCommentModel, session: AsyncSession):
        data = Model.model_dump()
        hospitalcomment = PatientToHospitalComment(**data)
        await self.patienttohospitalcomment_repo.add(obj=hospitalcomment, session=session)
        return hospitalcomment
    
    async def update_ph_comment(self, Model: UpdatePatientToHospitalCommentModel, patienttohospitalcomment_id, session: AsyncSession):
        return await self.patienttohospitalcomment_repo.update(obj_id=patienttohospitalcomment_id, obj=Model, session=session)
    
    async def delete_ph_comment(self, patienttohospitalcomment_id, session: AsyncSession):
        return await self.patienttohospitalcomment_repo.delete(obj_id=patienttohospitalcomment_id, session=session)
    
    async def delete_ph_comment_by_patient_id(self, patient_id, session: AsyncSession):
        return await self.patienttohospitalcomment_repo.delete_by_patient_id(patient_id=patient_id, session=session)


    async def delete_ph_comment_by_hospital_id(self, hospital_id, session: AsyncSession):
        return await self.patienttohospitalcomment_repo.delete_by_hospital_id(hospital_id=hospital_id, session=session)
    
