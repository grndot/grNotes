import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from source.config import load_config
from source.filters.admin import AdminFilter
from source.handlers.menu.check_edit_note import reg_check_changes
from source.handlers.menu.del_note import reg_del_chosen_note
from source.handlers.menu.edit_note import reg_edit_chosen_note
from source.handlers.menu.settings.delete_all.check_delete_all import reg_check_delete_all
from source.handlers.menu.settings.delete_all.set_delete_all import reg_set_delete_all
from source.handlers.menu.settings.languages.set_lang import reg_update_lang
from source.handlers.menu.settings.languages.set_lang_pages import reg_update_lang_with_chosen_page
from source.handlers.menu.settings.recovery.set_recovery import reg_set_recovery_code
from source.handlers.menu.settings.settings_menu import reg_menu_settings
from source.handlers.menu.settings.confrim_language import reg_menu_setting_after_updating_language
from source.handlers.start.start import reg_start
from source.handlers.start.recovery.check import reg_check_recovery_code
from source.handlers.start.recovery.code import reg_get_recovery_code
from source.handlers.menu.menu import reg_main_menu
from source.handlers.menu.menu_pages import reg_main_menu_with_choosen_page
from source.handlers.menu.create.check import reg_check_title_of_note 
from source.handlers.menu.create.title import reg_create_note
from source.handlers.menu.show_note import reg_show_note

from source.middlewares.environment import EnvironmentMiddleware
from source.middlewares.db import DatabaseMiddleware
from source.middlewares.i18n import LanguageMiddleware
from source.services.db.session_pool import create_session_pool


logger = logging.getLogger(__name__)


def register_all_middlewares(dp, domain, locales_dir, config, session_pool):
    dp.setup_middleware(EnvironmentMiddleware(config=config))
    dp.setup_middleware(DatabaseMiddleware(session_pool=session_pool))
    dp.setup_middleware(LanguageMiddleware(
        domain=domain,
        path=locales_dir))


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    reg_start(dp)
    reg_get_recovery_code(dp)
    reg_check_recovery_code(dp)
    reg_main_menu(dp)
    reg_main_menu_with_choosen_page(dp)
    reg_set_delete_all(dp)
    reg_check_delete_all(dp)
    reg_menu_settings(dp)
    reg_menu_setting_after_updating_language(dp)
    reg_set_recovery_code(dp)
    reg_create_note(dp)
    reg_check_title_of_note(dp)
    reg_show_note(dp)
    reg_del_chosen_note(dp)
    reg_edit_chosen_note(dp)
    reg_check_changes(dp)
    reg_update_lang(dp)
    reg_update_lang_with_chosen_page(dp)



async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")
    
    domain = config.i18n.i18n_domain
    locales_dir = config.i18n.locales_dir
    session_pool = create_session_pool(config.db)
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp, domain, locales_dir, config, session_pool)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
