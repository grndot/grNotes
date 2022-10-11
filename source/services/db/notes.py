from sqlalchemy import update

from source.models.database import Notes


async def updateOwnerID(
        session,
        old_id,
        new_id):
    stmt = update(Notes.OwnerID).where(
            Notes.OwnerID == old_id).order_by(
                    ).values(
                    {Notes.OwnerID: new_id})
    await session.execute(stmt)
    await session.commit()
    print(f"Notes from {old_id=} has been provided for {new_id=}")
