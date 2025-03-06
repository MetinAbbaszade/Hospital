from app.api.v1.schemas.user import UserModel
from app.api.v1.schemas.admin import PostAdminModel
from app.api.v1.schemas.patient import PostPatientModel
from app.api.v1.schemas.doctor import PostDoctorModel
from app.api.v1.schemas.owner import PostOwnerModel
from app.persistence.modelRepository.user import UserRepository
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession

class Facade:
    def __init__(self):
        self.user_repo = UserRepository()

    async def add_user(
            self, 
            Model: UserModel | PostAdminModel | PostPatientModel | PostDoctorModel | PostOwnerModel,
            session: AsyncSession):
        userModel = User(
        id=Model.id,
        role=Model.role,
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
        return await self.user_repo.delete(obj_id=user_id, session=session)
    
    async def get_user_by_email(self, email:str, session:AsyncSession):
        users = await self.user_repo.get_all(session=session)
        return next((user for user in users if user.email == email), None)