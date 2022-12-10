from sqlalchemy import delete, insert, select, update
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession

from source.models.database import Notes


async def deleteNote(
        session: AsyncSession,
        note_id: int):
    stmt = delete(Notes).where(Notes.ID == note_id)
    await session.execute(stmt)
    await session.commit()


async def getCountNotes(
        session: AsyncSession,
        owner_id: int):
    stmt = select(func.count()).select_from(
            Notes).where(
                    Notes.OwnerID == owner_id)
    result = await session.execute(stmt)
    answer = result.first()
    return answer[0]


async def getNotesTitleAndIDByOwnerID(
        session: AsyncSession,
        owner_id: int):
 
    class Note:
        def __init__(self, title: str, id_note: int) -> None:
    
            self.title = title
            self.id = id_note

    stmt = select(Notes.Title, Notes.ID).where(
            Notes.OwnerID==owner_id)
    result = await session.execute(stmt)
    arrow = result.all()
    response = [
        Note(title=item[0], id_note=item[1]) for item in arrow]
    return response


async def getNoteTitleAndTextByNoteID(
        session: AsyncSession,
        note_id: int):
    
    class Note:
        def __init__(self, title: str, text: str):

            self.title = title
            self.text = text

    stmt = select(
            Notes.Title,
            Notes.Text).where(
            Notes.ID == note_id)
    result = await session.execute(stmt)
    init_data = result.first()
    return Note(
            title=init_data[0],
            text=init_data[1])
    

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
    return result.scalars()


async def updateOwnerID(
        session: AsyncSession,
        old_id: int,
        new_id: int):
    stmt = update(Notes).where(
            Notes.OwnerID == old_id).values(
                    {Notes.OwnerID: new_id})
    await session.execute(stmt)
    await session.commit()


async def updateTextByNoteID(
        session: AsyncSession,
        text: str,
        note_id: int):
    stmt = update(Notes).where(
            Notes.ID == note_id).values(
                    {Notes.Text: text})
    await session.execute(stmt)
    await session.commit()
