from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salut! Envoie-moi un lien et je t’aiderai à le télécharger.")

def main():
    token = os.getenv("TOKEN")
    if not token:
        print("Erreur: TOKEN non défini dans les variables d'environnement")
        return

    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    print("Bot démarré...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
