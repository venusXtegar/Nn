from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ===== CONFIG =====
BOT_TOKEN = "ISI_TOKEN_BOT_KAMU"
SERVER_PASSWORD = "password123"  # <<< ganti di sini kalo mau update

# ===== /start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Hello {user.first_name}! 🎉\nIni passwordmu:\n\n🔑 {SERVER_PASSWORD}"
    )

# ===== MAIN =====
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot jalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
