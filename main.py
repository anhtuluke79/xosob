import os
import logging
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from handlers.menu import menu, menu_callback_handler
from handlers.input_handler import handle_user_free_input

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN")

def main():
    if not TOKEN:
        raise ValueError("❌ BOT_TOKEN chưa được set")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler(["start", "menu"], menu))
    app.add_handler(CallbackQueryHandler(menu_callback_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_user_free_input))

    logger.info("🤖 Bot is running with LONG POLLING (no webhook).")
    app.run_polling(drop_pending_updates=True, close_loop=False)

if __name__ == "__main__":
    main()
