from app.persistence.repository import Repository
from app.models.user import User
from app.models.patient import Patient
from app.models.admin import Admin
from app.models.doctor import Doctor
from app.models.owner import Owner
from app.models.hospital import Hospital
from app.api.v1.schemas.doctor import DoctorModel
from app.api.v1.schemas.patient import PatientModel
from app.api.v1.schemas.user import UserModel
from app.api.v1.schemas.admin import AdminModel
from app.api.v1.schemas.hospital import HospitalModel
from app.api.v1.schemas.owner import OwnerModel
from sqlalchemy.ext.asyncio import AsyncSession


class Facade:
    def __init__(self):
        self.user_repo = Repository(User)
        self.patient_repo = Repository(Patient)
        self.admin_repo = Repository(Admin)
        self.doctor_repo = Repository(Doctor)
        self.owner_repo = Repository(Owner)
        self.hospital_repo = Repository(Hospital)


    async def add_user(self, Model: UserModel, session: AsyncSession):
        userModel = User(
        id=Model.id,
        role=Model.role,
        fname=Model.fname,
        lname=Model.lname,
        email=Model.email,
        password=Model.password,
        created_at=Model.created_at,
        updated_at=Model.updated_at
    )
        await self.user_repo.add(obj=userModel, session=session)
        return userModel

    async def get_user(self, user_id, session: AsyncSession):
        return await self.user_repo.get(obj_id=user_id, session=session)

    async def get_all_users(self, session: AsyncSession):
        return await self.user_repo.get_all(session=session)
    
    async def update_user(self, Model: UserModel, user_id, session: AsyncSession):
        data = User(
            id = Model.id | None,
            role = Model.role | None,
            fname = Model.fname | None,
            lname = Model.lname | None,
            email = Model.email | None,
            password = Model.password | None,
            created_at = Model.created_at | None,
            updated_at = Model.updated_at | None
        )
        return await self.user_repo.update(obj_id=user_id, obj=data, session=session)
    
    async def delete_user(self, user_id, session: AsyncSession):
        return await self.doctor_repo.delete(obj_id=user_id, session=session)
    
    async def get_user_by_email(self, email:str, session:AsyncSession):
        users = await self.user_repo.get_all(session=session)
        return next((user for user in users if user.email == email), None)
    
    async def add_patient(self, Model: PatientModel, session: AsyncSession):
        patient = Patient(
            id=Model.id,
            role=Model.role,
            fname=Model.fname,
            lname=Model.lname,
            created_at=Model.created_at,
            updated_at=Model.updated_at
        )
        await self.patient_repo.add(obj=patient, session=session)
        return patient
    
    async def get_patient(self, patient_id, session: AsyncSession):
        return await self.patient_repo.get(obj_id=patient_id, session=session)

    async def get_all_patients(self, session: AsyncSession):
        return await self.patient_repo.get_all(session=session)
    
    async def update_patient(self, Model: PatientModel, patient_id, session: AsyncSession):
        data = Patient(
            id=Model.id | None,
            role=Model.role | None,
            fname=Model.fname | None,
            lname=Model.lname | None,
            created_at=Model.created_at | None,
            updated_at=Model.updated_at | None
        )
        return await self.patient_repo.update(obj_id=patient_id, obj=data, session=session)

    async def delete_patient(self, patient_id, session: AsyncSession):
        return await self.patient_repo.delete(obj_id=patient_id, session=session)

    async def add_doctor(self, Model: DoctorModel, session: AsyncSession):
        doctor = Doctor(
            id=Model.id,
            hospital_id=Model.hospital_id,
            fname=Model.fname,
            lname=Model.lname,
            role=Model.role,
            specialization=Model.specialization,
            phone_num=Model.phone_num,
            experience=Model.experience,
            created_at=Model.created_at,
            updated_at=Model.updated_at
        )
        await self.doctor_repo.add(obj=doctor, session=session)
        return doctor

    async def get_all_doctors(self, session: AsyncSession):
        return await self.doctor_repo.get_all(session=session)

    async def get_doctor(self, doctor_id, session: AsyncSession):
        return await self.doctor_repo.get(obj_id=doctor_id, session=session)
    
    async def update_doctor(self, Model: DoctorModel, doctor_id, session: AsyncSession):
        data = Doctor(
            id=Model.id | None,
            hospital_id=Model.hospital_id | None,
            fname=Model.fname | None,
            lname=Model.lname | None,
            role=Model.role | None,
            specialization=Model.specialization | None,
            phone_num=Model.phone_num | None,
            experience=Model.experience | None,
            created_at=Model.created_at | None,
            updated_at=Model.updated_at | None
        )
        return await self.doctor_repo.update(obj=data, obj_id=doctor_id, session=session)

    async def delete_doctor(self, doctor_id, session: AsyncSession):
        return await self.doctor_repo.delete(obj_id=doctor_id, session=session)
    
    async def add_admin(self, Model: AdminModel, session: AsyncSession):
        admin = Admin(
            id=Model.id,
            role=Model.role,
            lname=Model.lname,
            fname=Model.fname,
            created_at=Model.created_at,
            updated_at=Model.updated_at
        )
        await self.admin_repo.add(obj=admin, session=session)
        return admin

    async def get_all_admins(self, session: AsyncSession):
        return await self.admin_repo.get_all(session=session)
    
    async def get_admin(self, admin_id, session: AsyncSession):
        return await self.admin_repo.get(obj_id=admin_id, session=session)
    
    async def update_admin(self, admin_id, Model: AdminModel, session: AsyncSession):
        data = Admin(
            id=Model.id | None,
            role=Model.role | None,
            lname=Model.lname | None,
            fname=Model.fname | None,
            created_at=Model.created_at | None,
            updated_at=Model.updated_at | None
        )
        return await self.admin_repo.update(obj_id=admin_id, obj=data, session=session)

    async def delete_admin(self, admin_id, session: AsyncSession):
        return await self.admin_repo.delete(obj_id=admin_id, session=session)
    
    async def add_hospital(self, Model: HospitalModel, session: AsyncSession):
        data = Model.model_dump()
        hospital = Hospital(**data)
        await self.hospital_repo.add(obj=hospital, session=session)
        return hospital
    
    async def get_all_hospitals(self, session: AsyncSession):
        return await self.hospital_repo.get_all(session=session)
    
    async def get_hospital(self, hospital_id, session: AsyncSession):
        return await self.hospital_repo.get(obj_id=hospital_id, session=session)
    
    async def update_hospital(self, Model: HospitalModel, hospital_id, session: AsyncSession):
        data = Hospital(
            id=Model.id | None,
            owner_id=Model.owner_id | None,
            name=Model.name | None,
            phone_number=Model.phone_number | None,
            email=Model.email | None,
            state=Model.state | None,
            city=Model.city | None,
            zipcode=Model.zipcode | None,
            street=Model.street | None,
            created_at=Model.created_at | None,
            updated_at=Model.updated_at | None
        )

        return await self.hospital_repo.update(obj_id=hospital_id, obj=data, session=session)
    
    async def delete_hospital(self, hospital_id, session: AsyncSession):
        return await self.hospital_repo.delete(obj_id=hospital_id, session=session)
    
    async def add_hospital_owner(self, Model: OwnerModel, session: AsyncSession):
        owner = Owner(
            id=Model.id,
            fname=Model.fname,
            lname=Model.lname,
            role=Model.role,
            created_at=Model.created_at,
            updated_at=Model.updated_at
        )


        await self.owner_repo.add(obj=owner, session=session)
        return owner

    async def get_all_hospital_owners(self, session: AsyncSession):
        return await self.owner_repo.get_all(session=session)

    async def get_hospital_owner(self, owner_id, session: AsyncSession):
        return await self.owner_repo.get(obj_id=owner_id, session=session)

    async def update_hospital_owner(self, owner_id, Model: OwnerModel, session: AsyncSession):
        owner = Owner(
            id=Model.id | None,
            fname=Model.fname | None,
            lname=Model.lname | None,
            role=Model.role | None,
            created_at=Model.created_at | None,
            updated_at=Model.updated_at | None
        )

    async def delete_hospital_owner(self, owner_id, session: AsyncSession):
        return await self.owner_repo.delete(obj_id=owner_id, session=session)