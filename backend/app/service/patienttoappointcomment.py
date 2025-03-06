from app.persistence.modelRepository.patienttoappointcomment import PatientToAppointCommentRepository
from app.models.patienttoappointcomment import PatientToAppointComment
from app.api.v1.schemas.patienttoappointcomment import PostPatientToAppointCommentModel, UpdatePatientToAppointCommentModel
from sqlalchemy.ext.asyncio import AsyncSession

class Facade:
    def __init__(self):
        self.patienttoappointcomment_repo = PatientToAppointCommentRepository()

    async def get_pa_comment(self, patienttoappointcomment_id, session: AsyncSession):
        return await self.patienttoappointcomment_repo.get(obj_id=patienttoappointcomment_id, session=session)
    
    async def get_all_pa_comments(self, session: AsyncSession):
        return await self.patienttoappointcomment_repo.get_all(session=session)
    
    async def get_pa_comment_by_patient_id(self, patient_id, session: AsyncSession):
        return await self.patienttoappointcomment_repo.get_by_patient_id(patient_id=patient_id, session=session)

    async def get_pa_comment_by_appoint_id(self, appoint_id, session: AsyncSession):
        return await self.patienttoappointcomment_repo.get_by_appoint_id(appoint_id=appoint_id, session=session)
    
    async def add_pa_comment(self, Model: PostPatientToAppointCommentModel, session: AsyncSession):
        data = Model.model_dump()
        patientcomment = PatientToAppointComment(**data)
        await self.patienttoappointcomment_repo.add(obj=patientcomment, session=session)
        return patientcomment
    
    async def update_pa_comment(self, Model: UpdatePatientToAppointCommentModel, patienttoappointcomment_id, session: AsyncSession):
        return await self.patienttoappointcomment_repo.update(obj_id=patienttoappointcomment_id, obj=Model, session=session)
    
    async def delete_pa_comment(self, patienttoappointcomment_id, session: AsyncSession):
        return await self.patienttoappointcomment_repo.delete(obj_id=patienttoappointcomment_id, session=session)
    
    async def delete_pa_comment_by_patient_id(self, patient_id, session: AsyncSession):
        return await self.patienttoappointcomment_repo.delete_by_patient_id(patient_id=patient_id, session=session)


    async def delete_pa_comment_by_appoint_id(self, appoint_id, session: AsyncSession):
        return await self.patienttoappointcomment_repo.delete_by_appoint_id(appoint_id=appoint_id, session=session)
    