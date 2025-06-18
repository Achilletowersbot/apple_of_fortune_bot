import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN = "7987044763:AAF_3F5DKlXXVzbQkgJ_Sg0BHNmP5G17jzk"

# Historique des tentatives précédentes
historique = []

# Prédiction intelligente (simple pattern learning)
def predire_case():
    if not historique:
        return random.choice(["left", "center", "right"])
    # Analyser les tendances
    dernier = historique[-1]
    if historique.count(dernier) > len(historique) // 2:
        return dernier  # répétition d’un choix gagnant
    return random.choice(["left", "center", "right"])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🍏 Bienvenue dans le bot Apple of Fortune prédicteur !\nTape /jouer pour recevoir une prédiction.")

async def jouer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prediction = predire_case()
    historique.append(prediction)
    await update.message.reply_text(f"🔮 Je prédis que la meilleure case est : *{prediction.upper()}*", parse_mode="Markdown")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jouer", jouer))

    app.run_polling()
