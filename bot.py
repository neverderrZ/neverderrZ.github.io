import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "-"
WEBAPP_URL = "https://neverderrZ.github.io"

bot = Bot(token=TOKEN)
dp = Dispatcher()


def play_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎮 Начать игру",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )


@dp.message(Command("start"))
@dp.message(Command("play"))
async def start_cmd(message: types.Message):
    await message.answer(
        "✨ Крестики-нолики ✨\n\n"
        "Побеждайте и получайте промокоды 💖",
        reply_markup=play_keyboard()
    )


@dp.message()
async def webapp_result(message: types.Message):
    if not message.web_app_data:
        return

    data = message.web_app_data.data

    if data.startswith("win:"):
        promo = data.split(":")[1]
        await message.answer(
            f"🎉 Победа!\nПромокод выдан: {promo}",
            reply_markup=play_keyboard()
        )

    elif data == "lose":
        await message.answer(
            "😔 Проигрыш",
            reply_markup=play_keyboard()
        )

    elif data == "draw":
        await message.answer(
            "🤍 Ничья",
            reply_markup=play_keyboard()
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
