from app.persistence.repository import Repository
from app.models.doctortohospitalcomments import DoctorToHospitalComment
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from uuid import UUID

class DoctorToHospitalCommentRepository(Repository):
    def __init__(self):
        super().__init__(DoctorToHospitalComment)

    async def get_by_doctor_id(self, doctor_id, session: AsyncSession):
        try:
            if isinstance(doctor_id, str):
                doctor_id = UUID(doctor_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        return session.execute(select(self.model).where(self.model.doctor_id == doctor_id)).scalars().all()
    
    async def get_by_hospital_id(self, hospital_id, session: AsyncSession):
        try:
            if isinstance(hospital_id, str):
                hospital_id = UUID(hospital_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        return session.execute(select(self.model).where(self.model.hospital_id == hospital_id)).scalars().all()
    
    async def delete_by_doctor_id(self, doctor_id, session: AsyncSession):
        try:
            if isinstance(doctor_id, str):
                doctor_id = UUID(doctor_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        objects = session.execute(select(self.model).where(self.model.doctor_id == doctor_id)).scalars().all()

        for obj in objects:
            session.delete(obj)

        session.commit()

    async def delete_by_hospital_id(self, hospital_id, session: AsyncSession):
        try:
            if isinstance(hospital_id, str):
                hospital_id = UUID(hospital_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        objects = session.execute(select(self.model).where(self.model.hospital_id == hospital_id)).scalars().all()

        for obj in objects:
            session.delete(obj)

        session.commit()