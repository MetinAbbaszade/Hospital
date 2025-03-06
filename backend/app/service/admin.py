from app.persistence.modelRepository.admin import AdminRepository
from app.models.admin import Admin
from app.api.v1.schemas.admin import PostAdminModel, UpdateAdminModel
from sqlalchemy.ext.asyncio import AsyncSession


class Facade:

    def __init__(self):
        self.admin_repo = AdminRepository()

    async def add_admin(self, Model: PostAdminModel, session: AsyncSession):
        admin = Admin(
            id=Model.id,
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
    
    async def update_admin(self, admin_id, Model: UpdateAdminModel, session: AsyncSession):
        return await self.admin_repo.update(obj_id=admin_id, obj=Model, session=session)

    async def delete_admin(self, admin_id, session: AsyncSession):
        return await self.admin_repo.delete(obj_id=admin_id, session=session)
    