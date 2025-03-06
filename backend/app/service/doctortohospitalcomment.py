from app.persistence.modelRepository.doctortohospitalcomment import DoctorToHospitalCommentRepository
from app.models.doctortohospitalcomments import DoctorToHospitalComment
from app.api.v1.schemas.doctortohospitalcomment import PostDoctorToHospitalCommentModel, UpdateDoctorToHospitalCommentModel
from sqlalchemy.ext.asyncio import AsyncSession

class Facade:
    def __init__(self):
        self.doctortohospitalcomment_repo = DoctorToHospitalCommentRepository()

    async def get_dh_comment(self, doctortohospitalcomment_id, session: AsyncSession):
        return await self.doctortohospitalcomment_repo.get(obj_id=doctortohospitalcomment_id, session=session)
    
    async def get_all_dh_comments(self, session: AsyncSession):
        return await self.doctortohospitalcomment_repo.get_all(session=session)
    
    async def get_dh_comment_by_doctor_id(self, doctor_id, session: AsyncSession):
        return await self.doctortohospitalcomment_repo.get_by_doctor_id(doctor_id=doctor_id, session=session)

    async def get_dh_comment_by_hospital_id(self, hospital_id, session: AsyncSession):
        return await self.doctortohospitalcomment_repo.get_by_hospital_id(hospital_id=hospital_id, session=session)
    
    async def add_dh_comment(self, Model: PostDoctorToHospitalCommentModel, session: AsyncSession):
        data = Model.model_dump()
        hospitalcomment = DoctorToHospitalComment(**data)
        await self.doctortohospitalcomment_repo.add(obj=hospitalcomment, session=session)
        return hospitalcomment
    
    async def update_dh_comment(self, Model: UpdateDoctorToHospitalCommentModel, doctortohospitalcomment_id, session: AsyncSession):
        return await self.doctortohospitalcomment_repo.update(obj_id=doctortohospitalcomment_id, obj=Model, session=session)
    
    async def delete_dh_comment(self, doctortohospitalcomment_id, session: AsyncSession):
        return await self.doctortohospitalcomment_repo.delete(obj_id=doctortohospitalcomment_id, session=session)
    
    async def delete_dh_comment_by_doctor_id(self, doctor_id, session: AsyncSession):
        return await self.doctortohospitalcomment_repo.delete_by_doctor_id(doctor_id=doctor_id, session=session)

    async def delete_dh_comment_by_hospital_id(self, hospital_id, session: AsyncSession):
        return await self.doctortohospitalcomment_repo.delete_by_hospital_id(hospital_id=hospital_id, session=session)