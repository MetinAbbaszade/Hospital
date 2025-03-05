from app.persistence.repository import Repository
from app.models.patienttodoctorcomment import PatientToDoctorComment
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select


class PatientToDoctorCommentRepository(Repository):
    def __init__(self):
        super().__init__(PatientToDoctorComment)

    async def get_by_doctor_id(self, doctor_id, session: AsyncSession):
        try:
            if isinstance(doctor_id, str):
                doctor_id = UUID(doctor_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        return session.execute(select(self.model).where(self.model.doctor_id == doctor_id)).scalars().all()
    
    async def get_by_patient_id(self, patient_id, session: AsyncSession):
        try:
            if isinstance(patient_id, str):
                patient_id = UUID(patient_id)
            else:
                pass
        except:
            raise ValueError('Id not suitable for uuid format.')
        
        return session.execute(select(self.model).where(self.model.patient_id == patient_id)).scalars().all()
    
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