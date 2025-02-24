from app.models.doctorspecialization import DoctorSpecialization
from app.persistence.repository import Repository
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select


class DoctorSpecializationRepository(Repository):
    def __init__(self):
        super().__init__(DoctorSpecialization)


    async def get_doctorspecialization_by_doctor(self, doctor_id: UUID, session: AsyncSession):
        try:
            if isinstance(doctor_id, str):
                doctor_id = UUID(doctor_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        return session.execute(select(self.model).where(self.model.doctor_id == doctor_id)).scalars().all()
    
    async def get_doctorspecialization_by_specialization(self, specialization_id: UUID, session: AsyncSession):
        try:
            if isinstance(specialization_id, str):
                specialization_id = UUID(specialization_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')                
        return session.execute(select(self.model).where(self.model.specialization_id == specialization_id)).scalars().all()
    
    async def delete_doctorspecialization_by_doctor(self, doctor_id: UUID, session: AsyncSession):
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

    async def delete_doctorspecialization_by_specialization(self, specialization_id: UUID, session: AsyncSession):
        try:
            if isinstance(specialization_id, str):
                specialization_id = UUID(specialization_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        objects = session.execute(select(self.model).where(self.model.specialization_id == specialization_id)).scalars().all()
        for obj in objects:
            session.delete(obj)
        session.commit()