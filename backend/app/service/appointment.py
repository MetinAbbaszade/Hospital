from app.persistence.modelRepository.appointment import AppointmentRepository
from app.models.appointment import Appointment
from app.api.v1.schemas.appointment import UpdateAppointmentModel, PostAppointmentModel
from sqlalchemy.ext.asyncio import AsyncSession

class Facade:
    def __init__(self):
        self.appointment_repo = AppointmentRepository()


    async def add_appointment(self, Model: PostAppointmentModel, session: AsyncSession):
        data = Model.model_dump()
        appointment = Appointment(**data)
        await self.appointment_repo.add(obj=appointment, session=session)
        return appointment
    
    async def get_all_appointments(self, session: AsyncSession):
        return await self.appointment_repo.get_all(session=session)
    
    async def get_appointment(self, appointment_id, session: AsyncSession):
        return await self.appointment_repo.get(obj_id=appointment_id, session=session)
    
    async def update_appointment(self, Model: UpdateAppointmentModel, appointment_id, session: AsyncSession):
        return await self.appointment_repo.update(obj_id=appointment_id, obj=Model, session=session)
    
    async def delete_appointment(self, appointment_id, session: AsyncSession):
        return await self.appointment_repo.delete(obj_id=appointment_id, session=session)
    
    
    async def get_appointment_by_doctor(self, doctor_id, session: AsyncSession):
        return await self.appointment_repo.get_appoint_by_doctor(doctor_id=doctor_id, session=session)
    
    async def get_appointment_by_patient(self, patient_id, session: AsyncSession):
        return await self.appointment_repo.get_appoint_by_patient(patient_id=patient_id, session=session)
    
    async def get_appointment_by_datetime(self, datetime, session: AsyncSession):
        return await self.appointment_repo.get_appoint_by_datetime(datetime=datetime, session=session)
   