from app.persistence.modelRepository.doctortoappointcomment import DoctorToAppointRepository
from app.models.doctortoappointcomment import DoctorToAppointComment
from app.api.v1.schemas.doctortoappointcomment import PostDoctorToAppointCommentModel, UpdateDoctorToAppointCommentModel
from sqlalchemy.ext.asyncio import AsyncSession

class Facade:
    def __init__(self):
        self.doctortoappointcomment_repo = DoctorToAppointRepository()

    async def get_da_comment(self, doctortoappointcomment_id, session: AsyncSession):
        return await self.doctortoappointcomment_repo.get(obj_id=doctortoappointcomment_id, session=session)
    
    async def get_all_da_comments(self, session: AsyncSession):
        return await self.doctortoappointcomment_repo.get_all(session=session)
    
    async def get_da_comment_by_doctor_id(self, doctor_id, session: AsyncSession):
        return await self.doctortoappointcomment_repo.get_by_doctor_id(doctor_id=doctor_id, session=session)

    async def get_da_comment_by_appoint_id(self, appoint_id, session: AsyncSession):
        return await self.doctortoappointcomment_repo.get_by_appoint_id(appoint_id=appoint_id, session=session)
    
    async def add_da_comment(self, Model: PostDoctorToAppointCommentModel, session: AsyncSession):
        data = Model.model_dump()
        doctorcomment = DoctorToAppointComment(**data)
        await self.doctortoappointcomment_repo.add(obj=doctorcomment, session=session)
        return doctorcomment
    
    async def update_da_comment(self, Model: UpdateDoctorToAppointCommentModel, doctortoappointcomment_id, session: AsyncSession):
        return await self.doctortoappointcomment_repo.udaate(obj_id=doctortoappointcomment_id, obj=Model, session=session)
    
    async def delete_da_comment(self, doctortoappointcomment_id, session: AsyncSession):
        return await self.doctortoappointcomment_repo.delete(obj_id=doctortoappointcomment_id, session=session)
    
    async def delete_da_comment_by_doctor_id(self, doctor_id, session: AsyncSession):
        return await self.doctortoappointcomment_repo.delete_by_doctor_id(doctor_id=doctor_id, session=session)


    async def delete_da_comment_by_appoint_id(self, appoint_id, session: AsyncSession):
        return await self.doctortoappointcomment_repo.delete_by_appoint_id(appoint_id=appoint_id, session=session)
    