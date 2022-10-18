from sqlalchemy import select, update
from sqlalchemy import func

from source.models.database import Notes


async def getCountNotes(
        session,
        user_id):
    stmt = select(func.count()).select_from(
            Notes).where(
                    Notes.OwnerID == user_id)
    result = await session.execute(stmt)
    answer = result.first()
    print(f"{user_id=} got {answer=} for query getCountNotes")
    return answer[0]


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
