from app.persistence.repository import Repository
from app.models.user import User
from app.models.patient import Patient
from sqlalchemy.ext.asyncio import AsyncSession


class Facade:
    def __init__(self):
        self.user_repo = Repository(User)
        self.patient_repo = Repository(Patient)

    async def add_user(self, user, session: AsyncSession):
        await self.user_repo.add(obj=user, session=session)
        return user

    async def get_user(self, user_id, session: AsyncSession):
        return await self.user_repo.get(obj_id=user_id, session=session)
    

    async def get_all_users(self, session: AsyncSession):
        return await self.user_repo.get_all(session=session)
    
    async def get_user_by_email(self, email:str, session:AsyncSession):
        users = await self.user_repo.get_all(session=session)
        return next((user for user in users if user.email == email), None)
    
    async def add_patient(self, patient: Patient, session: AsyncSession):
        await self.patient_repo.add(obj=patient, session=session)
        return patient
    
    async def get_patient(self, patient_id, session: AsyncSession):
        return await self.patient_repo.get(obj_id=patient_id, session=session)

    async def get_all_patients(self, session: AsyncSession):
        return await self.patient_repo.get_all(session=session)