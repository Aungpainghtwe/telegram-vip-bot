import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "မင်္ဂလာပါဗျ ❤️\nVipnow Bot မှ ကြိုဆိုပါတယ်။"
    )

def main():
    app = Application.builder().token(
        os.environ["BOT_TOKEN"]
    ).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
  telegram.
