from app.persistence.modelRepository.owner import OwnerRepository
from app.models.owner import Owner
from app.api.v1.schemas.owner import PostOwnerModel, UpdateOwnerModel
from sqlalchemy.ext.asyncio import AsyncSession

class Facade:
    def __init__(self):
        self.owner_repo = OwnerRepository()
        
    async def add_hospital_owner(self, Model: PostOwnerModel, session: AsyncSession):
        owner = Owner(
            id=Model.id,
            fname=Model.fname,
            lname=Model.lname,
            created_at=Model.created_at,
            updated_at=Model.updated_at
        )
        
        await self.owner_repo.add(obj=owner, session=session)
        return owner

    async def get_all_hospital_owners(self, session: AsyncSession):
        return await self.owner_repo.get_all(session=session)

    async def get_hospital_owner(self, owner_id, session: AsyncSession):
        return await self.owner_repo.get(obj_id=owner_id, session=session)

    async def update_hospital_owner(self, owner_id, Model: UpdateOwnerModel, session: AsyncSession):
        return await self.owner_repo.update(obj_id=owner_id, obj=Model, session=session)

    async def delete_hospital_owner(self, owner_id, session: AsyncSession):
        return await self.owner_repo.delete(obj_id=owner_id, session=session)
    