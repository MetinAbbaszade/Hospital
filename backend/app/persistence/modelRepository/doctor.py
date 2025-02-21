from app.persistence.repository import Repository
from app.models.doctor import Doctor
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

class DoctorRepository(Repository):
    def __init__(self):
        super().__init__(Doctor)

    async def get_doctor_by_hospital(self, hospital_id: UUID, session: AsyncSession):
        try:
            if isinstance(hospital_id, str):
                hospital_id = UUID(hospital_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        return session.execute(select(self.model).where(self.model.hospital_id == hospital_id)).scalars().all()
    
    async def get_doctor_by_specialities(self, specialization, session: AsyncSession):
        return session.execute(select(self.model).where(self.model.specialization == specialization)).scalars().all()