from app.persistence.repository import Repository
from app.models.hospital import Hospital
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

class HospitalRepository(Repository):
    def __init__(self):
        super().__init__(Hospital)

    async def get_hospital_by_owner(self, owner_id: UUID, session: AsyncSession):
        try:
            if isinstance(owner_id, str):
                owner_id = UUID(owner_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        return session.execute(select(self.model).where(self.model.owner_id == owner_id)).scalars().all()
    
    async def get_hospital_by_email(self, email: str, session: AsyncSession):
        return session.execute(select(self.model).where(self.model.email == email)).scalars().first()