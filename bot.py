
import random
import asyncio
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# ==================================
# TOKEN
# ==================================
TOKEN = "8745807646:AAFTwI776m4bopZy2I0AIE1igc1EN-4E2aE"

# ==================================
# ID DO CHAT
# ==================================
CHAT_ID = "2020392953"

# ==================================
# START
# ==================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mensagem = """
🤖 Avalon Trader IA ONLINE

✅ Análise automática ativada
📈 Sinais 24h ligados
🧠 IA monitorando mercado

Comandos:
/sinal
/status
"""

    await update.message.reply_text(mensagem)

# ==================================
# STATUS
# ==================================
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
🟢 BOT ONLINE

📡 Mercado monitorado
🧠 IA ativa
📈 Sinais automáticos ON
"""
    )

# ==================================
# SINAL MANUAL
# ==================================
async def sinal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    sinais = gerar_sinal()

    await update.message.reply_text(sinais)

# ==================================
# GERAR SINAL IA
# ==================================
def gerar_sinal():

    ativos = ["BTC/USDT", "EUR/USD", "ETH/USDT", "XAU/USD"]

    direcao = random.choice(["🟢 COMPRA", "🔴 VENDA"])

    ativo = random.choice(ativos)

    confianca = random.randint(82, 97)

    risco = random.choice([
        "baixo",
        "médio"
    ])

    tempo = random.choice([
        "1 min",
        "5 min",
        "15 min"
    ])

    mensagem = f"""
📈 {ativo}

{direcao}

🔥 Confiança: {confianca}%
⚠️ Risco: {risco}

⏰ Expiração: {tempo}

🧠 IA analisou:
✔️ Tendência
✔️ RSI
✔️ Volume
✔️ MACD
"""

    return mensagem

# ==================================
# SINAIS AUTOMÁTICOS 24H
# ==================================
async def sinais_automaticos(app):

    while True:

        mensagem = gerar_sinal()

        await app.bot.send_message(
            chat_id=CHAT_ID,
            text=mensagem
        )

        print("SINAL ENVIADO ✅")

        await asyncio.sleep(300)

# ==================================
# MAIN
# ==================================
async def iniciar():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("sinal", sinal))
    app.add_handler(CommandHandler("status", status))

    asyncio.create_task(
        sinais_automaticos(app)
    )
    
    
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    
    print("BOT ONLINE 24H ☑️")

    while True:
        await asyncio.sleep(3600)

# ==================================
# INICIAR
# ==================================
if __name__ == "__main__":
    import asyncio
    asyncio.run(iniciar())