from app.persistence.modelRepository.patienttodoctorcomment import PatientToDoctorCommentRepository
from app.models.patienttodoctorcomment import PatientToDoctorComment
from app.api.v1.schemas.patienttodoctorcomment import PostPatientToDoctorCommentModel, UpdatePatientToDoctorCommentModel
from sqlalchemy.ext.asyncio import AsyncSession

class Facade:
    def __init__(self):
        self.patienttodoctorcomment_repo = PatientToDoctorCommentRepository()

    async def get_pd_comment(self, patienttodoctorcomment_id, session: AsyncSession):
        return await self.patienttodoctorcomment_repo.get(obj_id=patienttodoctorcomment_id, session=session)
    
    async def get_all_pd_comments(self, session: AsyncSession):
        return await self.patienttodoctorcomment_repo.get_all(session=session)
    
    async def get_pd_comment_by_doctor_id(self, doctor_id, session: AsyncSession):
        return await self.patienttodoctorcomment_repo.get_by_doctor_id(doctor_id=doctor_id, session=session)
    
    async def get_pd_comment_by_patient_id(self, patient_id, session: AsyncSession):
        return await self.patienttodoctorcomment_repo.get_by_patient_id(patient_id=patient_id, session=session)
    
    async def add_pd_comment(self, Model: PostPatientToDoctorCommentModel, session: AsyncSession):
        data = Model.model_dump()
        doctorcomment = PatientToDoctorComment(**data)
        await self.patienttodoctorcomment_repo.add(obj=doctorcomment, session=session)
        return doctorcomment
    
    async def update_pd_comment(self, Model: UpdatePatientToDoctorCommentModel, patienttodoctorcomment_id, session: AsyncSession):
        return await self.patienttodoctorcomment_repo.update(obj_id=patienttodoctorcomment_id, obj=Model, session=session)
    
    async def delete_pd_comment(self, patienttodoctorcomment_id, session: AsyncSession):
        return await self.patienttodoctorcomment_repo.delete(obj_id=patienttodoctorcomment_id, session=session)
    
    async def delete_pd_comment_by_doctor_id(self, doctor_id, session: AsyncSession):
        return await self.patienttodoctorcomment_repo.delete_by_doctor_id(doctor_id=doctor_id, session=session)
    
    async def delete_pd_comment_by_patient_id(self, patient_id, session: AsyncSession):
        return await self.patienttodoctorcomment_repo.delete_by_patient_id(patient_id=patient_id, session=session)
    