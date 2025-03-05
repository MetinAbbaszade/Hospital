from app.persistence.repository import Repository
from app.models.patienttohospitalcomment import PatientToHospitalComment
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from uuid import UUID


class PatientToHospitalCommentRepository(Repository):
    def __init__(self):
        super().__init__(PatientToHospitalComment)

    async def get_by_hospital_id(self, hospital_id, session: AsyncSession):
        try:
            if isinstance(hospital_id, str):
                hospital_id = UUID(hospital_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        return session.execute(select(self.model).where(self.model.hospital_id == hospital_id)).scalars().all()
    
    async def get_by_patient_id(self, patient_id, session: AsyncSession):
        try:
            if isinstance(patient_id, str):
                patient_id = UUID(patient_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        return session.execute(select(self.model).where(self.model.patient_id == patient_id)).scalars().all()
    
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

    async def delete_by_patient_id(self, patient_id, session: AsyncSession):
        try:
            if isinstance(patient_id, str):
                patient_id = UUID(patient_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        objects = session.execute(select(self.model).where(self.model.patient_id == patient_id)).scalars().all()

        for obj in objects:
            session.delete(obj)

        session.commit()