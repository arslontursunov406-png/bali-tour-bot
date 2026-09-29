import asyncio
import os
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, BotCommand

# Tokeningiz
TOKEN = "8379437156:AAG7smYDEKdztR-pM9LIn2hI-OdaCwMD9-8"

# Siz bergan Menejerning Telegram raqamli ID'si
MANAGER_CHAT_ID = 8662388456

# Siz bergan Menejerning Telegram linki
MANAGER_USERNAME_LINK = "https://t.me/alitravel_bali"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🌴 Bali Turlari"), KeyboardButton(text="📞 Bog'lanish")],
            [KeyboardButton(text="ℹ️ Biz Haqimizda")]
        ],
        resize_keyboard=True
    )

async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="🔄 Asosiy menyuni ochish"),
        BotCommand(command="help", description="❓ Yordam va ko'rsatmalar")
    ]
    await bot.set_my_commands(commands)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Assalomu alaykum, <b>{message.from_user.full_name}</b>!\n\n"
        "<b>ALI TRAVEL BALI TOUR</b> rasmiy botiga xush kelibsiz! 🌴\n\n"
        "Quyidagi menyudan kerakli bo'limni tanlang yoki safar rejangizni (necha kishi, qaysi sanada, qayerga borishni) yozib yuboring!",
        reply_markup=get_main_menu(),
        parse_mode="HTML"
    )

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "🛠 Botdan foydalanish uchun pastdagi tugmalardan foydalaning yoki o'z istaklaringizni yozib yuboring.",
        reply_markup=get_main_menu(),
        parse_mode="HTML"
    )

@dp.message(F.text == "ℹ️ Biz Haqimizda")
async def about_us(message: types.Message):
    await message.answer(
        "🌴 <b>ALI TRAVEL BALI TOUR</b> — Bali oroliga unutilmas sayohatlarni tashkil qiladi.\n"
        "Eng sara yo'nalishlar, qulay turlar va professional gidlar.",
        parse_mode="HTML"
    )

@dp.message(F.text == "📞 Bog'lanish")
async def contact_us(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 Menejer bilan bog'lanish", url=MANAGER_USERNAME_LINK)]
        ]
    )
    await message.answer(
        "📞 Savollaringiz bo'lsa to'g'ridan-to'g'ri menejerimizga yozishingiz mumkin:",
        reply_markup=keyboard,
        parse_mode="HTML"
    )

# --- BALI TURLARI ---
@dp.message(F.text == "🌴 Bali Turlari")
async def bali_tours(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🏞 Ubud Tour", callback_data="tour_ubud")],
            [InlineKeyboardButton(text="🌋 Kintamani Vulkan", callback_data="tour_kintamani")],
            [InlineKeyboardButton(text="🐬 Lovina Dolphins", callback_data="tour_lovina")],
            [InlineKeyboardButton(text="🏝️ Nusa Penida Oroli", callback_data="tour_nusa")],
            [InlineKeyboardButton(text="🚁 Helicopter Tour", callback_data="tour_helicopter")],
            [InlineKeyboardButton(text="🌊 Melasti Beach", callback_data="tour_melasti")],
            [InlineKeyboardButton(text="🌴 Nusa Dua", callback_data="tour_nusadua")]
        ]
    )
    await message.answer("🇺🇿 <b>BALI TOURLARI</b> 🌴\n\nQuyidagi yo'nalishlardan birini tanlang:", reply_markup=keyboard, parse_mode="HTML")

@dp.callback_query(F.data.startswith("tour_"))
async def process_tour(callback: types.CallbackQuery):
    action = callback.data
    
    if action == "tour_ubud":
        photo = "AgACAgIAAxkBAAICA2q70b6aSrMrl3PdSPkFQ2bhQKMcAALsIGsbGtPgSab_UCiq94SbAQADAgADeAADPQQ"
        text = (
            "🏞 <b>Ubud — Bali madaniyati va tabiati</b>\n\n"
            "• Tirta Empul Temple\n"
            "• Tegalalang Rice Terrace\n"
            "• Alas Harum Bali\n\n"
            "💬 <i>Sanani, odam sonini yoki savolingizni shu yerga yozib yuboring (masalan: 13 iyul, 3 kishi), u to'g'ridan-to'g'ri menejerga boradi!</i>"
        )
    elif action == "tour_kintamani":
        photo = "AgACAgIAAxkBAAIB_mq70b4LioUHq24d6OwlJ9yuGT9zAALnIGsbGtPgSeE8szbP-hafAQADAgADeAADPQQ"
        text = (
            "🌋 <b>Kintamani — vulkan va ajoyib manzaralar</b>\n\n"
            "• Рассвет на вулкане Батур\n"
            "• Приключение на джипе\n"
            "• Посещение горячих источников\n\n"
            "💬 <i>Sanani, odam sonini yoki savolingizni shu yerga yozib yuboring, menejerga boradi!</i>"
        )
    elif action == "tour_lovina":
        photo = "AgACAgIAAxkBAAIB_2q70b7Ib34WdksgEGy_wQj-1ywEAALoIGsbGtPgSb-Yy6o6r5hEAQADAgADeAADPQQ"
        text = (
            "🐬 <b>Lovina Dolphins — delfinlar bilan tonggi sayohat</b>\n\n"
            "• НАБЛЮДЕНИЕ ЗА ДЕЛЬФИНАМИ\n"
            "• ВОДОПАД БАНЬЮМАЛА\n\n"
            "💬 <i>Sanani, odam sonini yoki savolingizni shu yerga yozib yuboring, menejerga boradi!</i>"
        )
    elif action == "tour_nusa":
        photo = "AgACAgIAAxkBAAICAWq70b54xDEH3F3G8so3eOyPs4kkAALrIGsbGtPgSXddjpt3u4bkAQADAgADeQADPQQ"
        text = (
            "🏝 <b>Nusa Penida — Bali’ning eng mashhur oroli</b>\n\n"
            "• Kelingking Beach\n"
            "• Angel’s Bilabong\n"
            "• Broken Beach\n\n"
            "💬 <i>Sanani, odam sonini yoki savolingizni shu yerga yozib yuboring, menejerga boradi!</i>"
        )
    elif action == "tour_helicopter":
        photo = "AgACAgIAAxkBAAIB_Wq70b4mhW36hIHLnirxdSVMHpitAALmIGsbGtPgSVXnMsk2fyX9AQADAgADeAADPQQ"
        text = (
            "🚁 <b>Helicopter Tour — Bali osmonidan unutilmas manzara</b>\n\n"
            "Bali orolining go'zal qirg'oqlari va tabiatini qush parvozi ostidan tomosha qiling.\n\n"
            "💬 <i>Sanani, odam sonini yoki savolingizni shu yerga yozib yuboring, menejerga boradi!</i>"
        )
    elif action == "tour_melasti":
        photo = "AgACAgIAAxkBAAICAAFqu9G-0w9m4ac3jpKjY9Bp3gWdfwAC6SBrGxrT4El4uPckqYSjdwEAAwIAA3gAAz0E"
        text = (
            "🌊 <b>Melasti Beach — tropik plyaj va okean manzarasi</b>\n\n"
            "Oq qumli qirg'oqlar, moviy okean va ajoyib dam olish muhiti.\n\n"
            "💬 <i>Sanani, odam sonini yoki savolingizni shu yerga yozib yuboring, menejerga boradi!</i>"
        )
    elif action == "tour_nusadua":
        photo = "AgACAgIAAxkBAAICAmq70b5pK03WSIAXuEAYKozgwub7AALqIGsbGtPgSfPKA9Jy04_EAQADAgADeAADPQQ"
        text = (
            "🌴 <b>Nusa Dua — premium dam olish va plyaj</b>\n\n"
            "Hashamatli dam olish maskanlari, tinch va toza plyajlar.\n\n"
            "💬 <i>Sanani, odam sonini yoki savolingizni shu yerga yozib yuboring, menejerga boradi!</i>"
        )

    await callback.message.answer_photo(photo=photo, caption=text, parse_mode="HTML")
    await callback.answer()

# --- KLIENT NIMA YOZSA HAM MENEJERGA YUBORISH VA LINK BERISH ---
@dp.message()
async def forward_to_manager(message: types.Message):
    if message.text in ["🌴 Bali Turlari", "📞 Bog'lanish", "ℹ️ Biz Haqimizda"]:
        return

    user = message.from_user
    user_info = (
        "📥 <b>Yangi xabar / buyurtma!</b>\n\n"
        f"👤 <b>Mijoz:</b> {user.full_name}\n"
        f"🔗 <b>Username:</b> @{user.username if user.username else 'mavjud emas'}\n"
        f"🆔 <b>ID:</b> <code>{user.id}</code>\n\n"
        f"✍️ <b>Yozgan matni / so'rovi:</b>\n"
    )

    try:
        # 1. Menejerga mijoz ma'lumotini va xabarini forward qilamiz
        await bot.send_message(MANAGER_CHAT_ID, user_info, parse_mode="HTML")
        await message.forward(chat_id=MANAGER_CHAT_ID)
        
        # 2. Klientga javob qaytaramiz va o'zingizning link tugmangizni chiqaramiz
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="💬 Menejer bilan to'g'ridan-to'g'ri yozishish", url=MANAGER_USERNAME_LINK)]
            ]
        )
        await message.answer(
            "✅ Xabaringiz qabul qilindi va menejerimizga yo'naltirildi!\n\n"
            "Tezroq bog'lanishni istasangiz, quyidagi tugmani bosing:",
            reply_markup=keyboard,
            parse_mode="HTML"
        )
    except Exception as e:
        print(f"Xatolik: {e}")
        keyboard_err = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="💬 Menejer", url=MANAGER_USERNAME_LINK)]]
        )
        await message.answer("Xabarni yuborishda xatolik yuz berdi. Iltimos, to'g'ridan-to'g'ri bog'laning:", reply_markup=keyboard_err)

async def main():
    await set_bot_commands(bot)
    print("Bot muvaffaqiyatli ishga tushdi va tayyor!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())