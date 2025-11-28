from telegram import (
    Update, InlineKeyboardMarkup, InlineKeyboardButton
)
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
)

TOKEN = "7794227861:AAERIHSt6jU0T6Cy36yNQ7M4Mt3Wc4GnrZk"  # НЕ ИСПОЛЬЗУЙ старый токен!

# --- /start ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name

    text = (
        f"👾Привет, {user}!👾\n"
        "Этот бот создан для покупки Робуксов.\n\n"
        "🫟 Хочешь купить Робуксы по низкой цене?\n\n"
        "👾 Тогда быстрее заказывай у нас:\n\n"
        "1. Быстрая доставка без задержки👌\n"
        "2. Оплата звёздами Telegram😘\n"
        "3. Выдача робуксов по GamePass😎\n\n"
        "Заказывай Робуксы ниже ⬇️\n\n"
        "ТехПоддержка — @comatozeerbx"
    )

    keyboard = [
        [InlineKeyboardButton("Выбрать кол-во Робуксов", callback_data="choose")]
    ]

    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))


# --- обработка всех кнопок ---
async def callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    # --- Выбор количества Робуксов ---
    if q.data == "choose":
        text = (
            "Выберите число Робуксов✨\n"
            "100, 300, 600 🫟\n"
            "1000, 1500, 2000👾\n"
            "4000, 7000, 10000🖤\n"
            "20000🫠"
        )

        keyboard = [
            [InlineKeyboardButton("100", callback_data="rbx_100"),
             InlineKeyboardButton("300", callback_data="rbx_300"),
             InlineKeyboardButton("600", callback_data="rbx_600")],

            [InlineKeyboardButton("1000", callback_data="rbx_1000"),
             InlineKeyboardButton("1500", callback_data="rbx_1500"),
             InlineKeyboardButton("2000", callback_data="rbx_2000")],

            [InlineKeyboardButton("4000", callback_data="rbx_4000"),
             InlineKeyboardButton("7000", callback_data="rbx_7000"),
             InlineKeyboardButton("10000", callback_data="rbx_10000")],

            [InlineKeyboardButton("20000", callback_data="rbx_20000")]
        ]

        await q.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

    # --- Нажатие на количество ---
    elif q.data.startswith("rbx_"):
        amount = q.data.split("_")[1]

        text = f"Вы выбрали {amount} Robux.\nЧто дальше?"

        keyboard = [
            [InlineKeyboardButton("Посмотреть цену", callback_data=f"price_{amount}")],
            [InlineKeyboardButton("Купить прямо сейчас", callback_data="buy")]
        ]

        await q.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

    # --- Прайс ---
    elif q.data.startswith("price_"):
        text = (
            "💎 Покупка Robux за Telegram Stars 💎\n\n"
            "🔹 100 Robux ➔ 30 Stars 🌟\n"
            "🔹 300 Robux ➔ 100 Stars 🌟\n"
            "🔹 600 Robux ➔ 200 Stars 🌟\n"
            "🔹 1000 Robux ➔ 300 Stars 🌟\n"
            "🔹 1500 Robux ➔ 400 Stars 🌟\n"
            "🔹 2000 Robux ➔ 600 Stars 🌟\n"
            "🔹 4000 Robux ➔ 1200 Stars 🌟\n"
            "🔹 7000 Robux ➔ 2600 Stars 🌟\n"
            "🔹 10000 Robux ➔ 3200 Stars 🌟\n"
            "🔹 20000 Robux ➔ 6400 Stars 🌟\n\n"
            "🎁 Бонус: При покупке от 4000 Robux — +10% к скидке!\n\n"
            "📌 Техподдержка: Если готовы к покупке — @comatozeerbx 🚀"
        )

        keyboard = [
            [InlineKeyboardButton("Купить прямо сейчас", callback_data="buy")]
        ]

        await q.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

    # --- Купить прямо сейчас ---
    elif q.data == "buy":
        await q.edit_message_text(
            "Чтобы заказать, напишите нашему менеджеру — @comatozeerbx 🫟"
        )


# --- запуск ---
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(callbacks))
app.run_polling()