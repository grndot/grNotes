from sqlalchemy import insert, select, update
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession

from source.models.database import Notes


async def insertNewNote(
        session: AsyncSession,
        owner_id: int,
        title: str,
        text: str):
    stmt = insert(Notes).values(
            OwnerID=owner_id,
            Title=title,
            Text=text)
    result = await session.execute(stmt)
    await session.commit()
    print(f"{owner_id=} inserted new note with {title=}")
    return result.scalars()


async def getNotesDataByOwnerID(
        session: AsyncSession,
        owner_id: int):
 
    class Note:
        def __init__(
                self,
                title: str,
                id_note: int,
                text: str) -> None:
    
            self.title = title
            self.id = id_note
            self.text = text

    stmt = select(Notes.Title, Notes.ID, Notes.Text).where(
            Notes.OwnerID==owner_id)
    result = await session.execute(stmt)
    arrow = result.all()
    answer = [Note(
        title=item[0],
        id_note=item[1],
        text=item[2]) for item in arrow]
    print(f"{owner_id=} got Titles and IDs his notes")
    return answer


async def getCountNotes(
        session: AsyncSession,
        owner_id: int):
    stmt = select(func.count()).select_from(
            Notes).where(
                    Notes.OwnerID == owner_id)
    result = await session.execute(stmt)
    answer = result.first()
    print(f"{owner_id=} got {answer=} for query getCountNotes")
    return answer[0]


async def updateOwnerID(
        session: AsyncSession,
        old_id: int,
        new_id: int):
    stmt = update(Notes).where(
            Notes.OwnerID == old_id).values(
                    {Notes.OwnerID: new_id})
    await session.execute(stmt)
    await session.commit()
    print(f"Notes from {old_id=} has been provided for {new_id=}")
