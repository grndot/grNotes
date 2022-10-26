from sqlalchemy import insert, select, update
from sqlalchemy import func

from source.models.database import Notes


async def insertNewNote(
        session,
        owner_id,
        title,
        text):
    stmt = insert(Notes).values(
            OwnerID=owner_id,
            Title=title,
            Text=text)
    result = await session.execute(stmt)
    await session.commit()
    print(f"{owner_id=} inserted new note with {title=}")
    return result.scalars()


async def getNotesTitleAndIDByOwnerID(
        session,
        owner_id):
 
    class Note:
        def __init__(self, title, id_note) -> None:
    
            self.title = title
            self.id = id_note

    stmt = select(Notes.Title, Notes.ID).where(
            Notes.OwnerID==owner_id)
    result = await session.execute(stmt)
    arrow = result.all()
    answer = [Note(title=item[0], id_note=item[1]) for item in arrow]
    print(f"{owner_id=} got Titles and IDs his notes")
    return answer


async def getCountNotes(
        session,
        owner_id):
    stmt = select(func.count()).select_from(
            Notes).where(
                    Notes.OwnerID == owner_id)
    result = await session.execute(stmt)
    answer = result.first()
    print(f"{owner_id=} got {answer=} for query getCountNotes")
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
