from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# دالة لإرسال رسالة مع لوحة المفاتيح المعطاة
async def send_message_with_keyboard(chat_id, text, keyboard):
    await app.send_message(chat_id, text, reply_markup=keyboard)

# دالة لإرسال الرسالة الترحيبية مع لوحة المفاتيح
async def start_command(client, message):
    text = "مرحبا! اختر ما تريد:"
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("1", callback_data="button1"),
                InlineKeyboardButton("2", callback_data="button2"),
            ]
        ]
    )
    await send_message_with_keyboard(message.chat.id, text, keyboard)

# دالة للتعامل مع الأزرار
async def button_click(client, callback_query):
    data = callback_query.data
    chat_id = callback_query.message.chat.id

    if data == "button1":
        text = "مرحبا"
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="back")]])
        await send_message_with_keyboard(chat_id, text, keyboard)
    elif data == "button2":
        text = "بك"
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="back")]])
        await send_message_with_keyboard(chat_id, text, keyboard)
    elif data == "back":
        text = "اختر ما تريد:"
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("1", callback_data="button1"),
                    InlineKeyboardButton("2", callback_data="button2"),
                ]
            ]
        )
        await send_message_with_keyboard(chat_id, text, keyboard)

# تسجيل الدوال كمنبثقة
app.start()
app.on_message(filters.command("start", prefixes="/"))(start_command)
app.on_callback_query()(button_click)
