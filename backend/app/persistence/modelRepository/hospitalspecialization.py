from app.persistence.repository import Repository
from app.models.hospitalspecialization import HospitalSpecialization
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

class HospitalSpecializationRepository(Repository):
    def __init__(self):
        super().__init__(HospitalSpecialization)

    async def get_hospitalspecialization_by_hospital(self, hospital_id: UUID, session: AsyncSession):
        try:
            if isinstance(hospital_id, str):
                hospital_id = UUID(hospital_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        return session.execute(select(self.model).where(self.model.hospital_id == hospital_id)).scalars().all()
    
    async def get_hospitalspecialization_by_specialization(self, specialization_id: UUID, session: AsyncSession):
        try:
            if isinstance(specialization_id, str):
                specialization_id = UUID(specialization_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')                
        return session.execute(select(self.model).where(self.model.specialization_id == specialization_id)).scalars().all()
    
    async def delete_hospitalspecialization_by_hospital(self, hospital_id: UUID, session: AsyncSession):
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

    async def delete_hospitalspecialization_by_specialization(self, specialization_id: UUID, session: AsyncSession):
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