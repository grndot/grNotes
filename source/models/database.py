from sqlalchemy import (
        BIGINT,
        INT,
        TEXT,
        VARCHAR,
        Column,
        ForeignKey,
        create_engine)
from sqlalchemy.orm import declarative_base
from sqlalchemy.engine.url import URL

from source.config import load_config


Base = declarative_base()


URL = URL.create(
        drivername="postgresql+psycopg2",
        username=load_config().db.user,
        password=load_config().db.password,
        host=load_config().db.host,
        database=load_config().db.database)


engine = create_engine(
        URL,
        echo=True,
        future=True)


class Languages(Base):
    __tablename__ = "Languages"

    ID = Column(
            INT,
            autoincrement=True, 
            primary_key=True, 
            nullable=False)
    
    Name = Column(
            VARCHAR(25),
            nullable=False,
            unique=True)


class Users(Base):
    __tablename__ = "Users"
 
    ID = Column(
            INT,
            nullable=False,
            primary_key=True,
            autoincrement=True)
    
    TelegramID = Column(
            BIGINT, 
            unique=True)
    
    LanguageID = Column(
            INT,
            ForeignKey(
                'Languages.ID',
                ondelete="cascade",
                onupdate="cascade"), 
            nullable=False)    
    
    RecoveryKey = Column(
            TEXT,
            unique=True)


class Notes(Base):
    __tablename__ = "Notes"

    ID = Column(
            INT,
            nullable=False,
            primary_key=True,
            autoincrement=True)
    OwnerID = Column(
            INT,
            ForeignKey('Users.ID',
                ondelete="cascade",
                onupdate="cascade"),
            nullable=False)
    Title = Column(
            VARCHAR(64),
            nullable=False)
    Text = Column(
            VARCHAR(2048),
            nullable=False
            )


if __name__ == "__main__":
    Base.metadata.create_all
