from dataclasses import dataclass
from pathlib import Path

from environs import Env
from sqlalchemy.engine.url import URL


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str
    port: int

    def construct_alchemy_url(self, library="asyncpg") -> str|URL:
        return str(URL.create(
            drivername=f"postgresql+{library}",
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password,
            database=self.database))


@dataclass
class Internationalization:
    i18n_domain: str
    base_dir: Path
    locales_dir: Path


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous
    i18n: Internationalization


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME'),
            port=env.int("DB_PORT")
        ),
        misc=Miscellaneous(),
        i18n=Internationalization(
            i18n_domain=env.str('I18N_DOMAIN'),
            base_dir=Path('bot.py').parent,
            locales_dir=Path('locales') 
            )
    )

