
import os
import openai
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from django.core.management.base import BaseCommand


load_dotenv()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

async def handle_message(update: Update, context: CallbackContext) -> None:
    try:
        user_message = update.message.text

        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=user_message,
            max_tokens=150
        )
        
        bot_reply = response.choices[0].text.strip()
        await update.message.reply_text(bot_reply)

    except Exception as e:
        logger.error(f"Error handling message: {e}")
        await update.message.reply_text("Sorry, something went wrong.")

async def start(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text('Hello! I am your AI-powered bot. How can I help you today?')
    except Exception as e:
        logger.error(f"Error in start command: {e}")

def main() -> None:
    try:
        application = Application.builder().token(os.getenv('TELEGRAM_BOT_TOKEN')).build()

        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        application.run_polling()

    except Exception as e:
        logger.error(f"Error in main: {e}")

class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **kwargs):
        main()

import os
import openai
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from django.core.management.base import BaseCommand


load_dotenv()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

async def handle_message(update: Update, context: CallbackContext) -> None:
    try:
        user_message = update.message.text

        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=user_message,
            max_tokens=150
        )
        
        bot_reply = response.choices[0].text.strip()
        await update.message.reply_text(bot_reply)

    except Exception as e:
        logger.error(f"Error handling message: {e}")
        await update.message.reply_text("Sorry, something went wrong.")

async def start(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text('Hello! I am your AI-powered bot. How can I help you today?')
    except Exception as e:
        logger.error(f"Error in start command: {e}")

def main() -> None:
    try:
        application = Application.builder().token(os.getenv('TELEGRAM_BOT_TOKEN')).build()

        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        application.run_polling()

    except Exception as e:
        logger.error(f"Error in main: {e}")

class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **kwargs):
        main()

