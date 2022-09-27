from typing import AsyncContextManager, Callable
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from source.config import DbConfig


def create_session_pool(
        db: DbConfig,
        echo=False
        ) -> Callable[[], AsyncContextManager[AsyncSession]]:
    async_engine = create_async_engine(
            db.construct_alchemy_url(),
                query_cache_size=1200,
                pool_size=20,
                max_overflow=200,
                future=True,
                echo=echo)
    """
    future: 
    we will use it to create a future engine
    
    echo: 
    we will use it to print the queries
    
    query_cache_size: 
    size of the cache used to cache the SQL string form of queries
    
    pool_size: 
    the number of connections to keep open inside the connection pool
    
    max_overflow: 
    the number of connections to allow in connection pool "overflow", 
    that is connections that can be opened above and 
    beyond the pool_size setting, which defaults to five.
    
    """
    session_pool = sessionmaker(
            bind=async_engine,
            class_=AsyncSession)
    return session_pool
