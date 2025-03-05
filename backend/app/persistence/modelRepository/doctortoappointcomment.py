from app.persistence.repository import Repository
from app.models.doctortoappointcomment import DoctorToAppointComment
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from uuid import UUID


class DoctorToAppointRepository(Repository):
    def __init__(self):
        super().__init__(DoctorToAppointComment)

    async def get_by_doctor_id(self, doctor_id, session: AsyncSession):
        try:
            if isinstance(doctor_id, str):
                doctor_id = UUID(doctor_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        return session.execute(select(self.model).where(self.model.doctor_id == doctor_id)).scalars().all()
    
    async def get_by_appoint_id(self, appoint_id, session: AsyncSession):
        try:
            if isinstance(appoint_id, str):
                appoint_id = UUID(appoint_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        return session.execute(select(self.model).where(self.model.appoint_id == appoint_id)).scalars().all()
    
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

    async def delete_by_appoint_id(self, appoint_id, session: AsyncSession):
        try:
            if isinstance(appoint_id, str):
                appoint_id = UUID(appoint_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        objects = session.execute(select(self.model).where(self.model.appoint_id == appoint_id)).scalars().all()

        for obj in objects:
            session.delete(obj)

        session.commit()