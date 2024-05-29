from telegram import Update
from telegram.ext import Updater, Application, CommandHandler, MessageHandler, filters, CallbackContext

# Function to echo the user message
async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(update.message.text)

def main():
    # Replace 'YOUR_TOKEN' with your actual bot token
    app = Application.builder().token('TOKEN').build()
    app.add_handler(MessageHandler(filters.TEXT, echo))
    # Start the bot
    app.run_polling()

if __name__ == '__main__':
    main()
