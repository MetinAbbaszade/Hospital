from app.persistence.repository import Repository
from app.models.appointment import Appointment
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

class AppointmentRepository(Repository):
    def __init__(self):
        super().__init__(Appointment)

    async def get_appoint_by_doctor(self, doctor_id, session: AsyncSession):
         try:
            if isinstance(doctor_id, str):
                doctor_id = UUID(doctor_id)
            else:
                pass
         except:
            raise ValueError('Id not suitable for uuid format.')
         
         return session.execute(select(self.model).where(self.model.doctor_id == doctor_id)).scalars().all()
    
    async def get_appoint_by_patient(self, patient_id, session: AsyncSession):
         try:
            if isinstance(patient_id, str):
                patient_id = UUID(patient_id)
            else:
                pass
         except:
            raise ValueError('Id not suitable for uuid format.')
         
         return session.execute(select(self.model).where(self.model.patient_id == patient_id)).scalars().all()
    
    async def get_appoint_by_datetime(self, datetime, session: AsyncSession):
        return session.execute(select(self.model).where(self.model.datetime == datetime)).scalars().all()
    

    async def get_appoint_by_status(self, status, session: AsyncSession):
        return session.execute(select(self.model).where(self.model.status == status)).scalars().all()