import telebot
from telebot import types

# --- الإعدادات الأساسية ---
API_TOKEN = '8751745566:AAERQxfQ5fkHca6XNzTm53HgsfmTCcrLFt0'
ADMIN_ID = 8592689169 
ADMIN_USER = "BRHOOMSE" 
CHANNEL_ID = "@AWM_Charge"
CHANNEL_LINK = "https://t.me/AWM_Charge"

bot = telebot.TeleBot(API_TOKEN)

# --- قائمة خدمات ببجي (الأسعار النهائية المحدثة) ---
PUBG_SERVICES = {
    "p1": {"label": "📦 60 UC", "price": "⚡ 0.99$ ➜ 12,500 SYP 🇸🇾"},
    "p2": {"label": "📦 325 UC", "price": "⚡ 4.76$ ➜ 60,000 SYP 🇸🇾"},
    "p3": {"label": "📦 660 UC", "price": "⚡ 9.44$ ➜ 118,900 SYP 🇸🇾"},
    "p4": {"label": "📦 1800 UC", "price": "⚡ 23.61$ ➜ 297,400 SYP 🇸🇾"},
    "p5": {"label": "📦 3850 UC", "price": "⚡ 45.51$ ➜ 573,400 SYP 🇸🇾"},
    "p6": {"label": "📦 8100 UC", "price": "⚡ 87.79$ ➜ 1,106,100 SYP 🇸🇾"}
}

# --- قائمة خدمات فري فاير (الأسعار المحدثة سابقاً) ---
FF_SERVICES = {
    "f1": {"label": "💎 110 Diamond", "price": "⚡ 1.10$ ➜ 13,500 SYP 🇸🇾"},
    "f2": {"label": "💎 221 Diamond", "price": "⚡ 2.10$ ➜ 26,100 SYP 🇸🇾"},
    "f3": {"label": "💎 583 Diamond", "price": "⚡ 4.80$ ➜ 61,100 SYP 🇸🇾"},
    "f4": {"label": "💎 1188 Diamond", "price": "⚡ 9.40$ ➜ 119,100 SYP 🇸🇾"},
    "f5": {"label": "💎 2420 Diamond", "price": "⚡ 18.50$ ➜ 234,100 SYP 🇸🇾"}
}

# --- الواجهة الرئيسية ---
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🔥 شحن ببجي موبايل | PUBG", callback_data="list_pubg"),
        types.InlineKeyboardButton("💎 شحن فري فاير | FREE FIRE", callback_data="list_ff"),
        types.InlineKeyboardButton("📈 قناة الإثباتات والضمان", url=CHANNEL_LINK),
        types.InlineKeyboardButton("💳 طرق الدفع المقبولة", callback_data="payments_menu"),
        types.InlineKeyboardButton("🛠 الدعم الفني والمساعدة", callback_data="support")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    text = (f"👋 أهلاً بك يا {message.from_user.first_name}\n\n"
            "🚀 **مرحباً بك في بوت AWM Charge المطور**\n"
            "أسرع خدمة شحن ألعاب في سوريا ⚡️\n\n"
            "📩 اختر القسم المطلوب للبدء:")
    bot.send_message(message.chat.id, text, reply_markup=main_menu(), parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "list_pubg":
        markup = types.InlineKeyboardMarkup(row_width=1)
        for key, item in PUBG_SERVICES.items():
            markup.add(types.InlineKeyboardButton(f"{item['label']} | {item['price']}", callback_data=f"buy_pubg_{key}"))
        markup.add(types.InlineKeyboardButton("🔙 العودة", callback_data="back_main"))
        bot.edit_message_text("📊 **قائمة أسعار ببجي (PUBG):**", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    elif call.data == "list_ff":
        markup = types.InlineKeyboardMarkup(row_width=1)
        for key, item in FF_SERVICES.items():
            markup.add(types.InlineKeyboardButton(f"{item['label']} | {item['price']}", callback_data=f"buy_ff_{key}"))
        markup.add(types.InlineKeyboardButton("🔙 العودة", callback_data="back_main"))
        bot.edit_message_text("📊 **قائمة أسعار فري فاير (Free Fire):**", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    elif call.data == "payments_menu":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("📞 سيريتل كاش", callback_data="pay_syriatel"),
            types.InlineKeyboardButton("📲 MTN كاش", callback_data="pay_mtn"),
            types.InlineKeyboardButton("🏦 شام كاش", callback_data="pay_sham"),
            types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main")
        )
        bot.edit_message_text("💰 **اختر وسيلة الدفع لعرض الرقم:**", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    elif call.data.startswith("pay_"):
        if call.data == "pay_syriatel": msg = "📞 **سيريتل كاش:** `95246739` 📱"
        elif call.data == "pay_mtn": msg = "📲 **MTN كاش:** `8198291506524965` 💸"
        elif call.data == "pay_sham": msg = "🏦 **شام كاش:** `7e311921b4cadde505444adfc0f3d2e5` 🏛️"
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🚀 إرسال الوصل للمسؤول", url=f"https://t.me/{ADMIN_USER}"))
        markup.add(types.InlineKeyboardButton("🔙 العودة", callback_data="payments_menu"))
        bot.edit_message_text(f"{msg}\n\n💡 **اضغط على الرقم لنسخه.**\n⚠️ أرسل صورة الوصل للمسؤول بعد التحويل.", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    elif call.data.startswith("buy_"):
        data = call.data.split("_")
        game_type, service_key = data[1], data[2]
        service_name = PUBG_SERVICES[service_key]['label'] if game_type == "pubg" else FF_SERVICES[service_key]['label']
        msg = bot.send_message(call.message.chat.id, f"🎯 لقد اخترت: **{service_name}**\n\n📝 أرسل الآن **(ID اللاعب)** ليتم تسجيل طلبك:", parse_mode="Markdown")
        bot.register_next_step_handler(msg, process_order, service_name)

    elif call.data == "support":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("💬 مراسلة المسؤول", url=f"https://t.me/{ADMIN_USER}"),
                   types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
        bot.edit_message_text(f"💡 تواصل معنا عبر: @{ADMIN_USER} ✅", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "back_main":
        bot.edit_message_text("⬇️ اختر القسم المطلوب للبدء:", call.message.chat.id, call.message.message_id, reply_markup=main_menu())

def process_order(message, service_name):
    player_id = message.text
    full_name = message.from_user.first_name
    user_name = f"@{message.from_user.username}" if message.from_user.username else "غير متوفر"

    channel_post = (f"🚀 **طلب شحن جديد!**\n"
                    f"━━━━━━━━━━━━━━\n"
                    f"👤 **الاسم:** {full_name}\n"
                    f"🆔 **الأيدي:** `{player_id}`\n"
                    f"📦 **الطلب:** {service_name}\n"
                    f"🔗 **اليوزر:** {user_name}\n"
                    "━━━━━━━━━━━━━━\n"
                    "✅ **تم استلام الطلب وبانتظار تأكيد الدفع**\n"
                    "⚡️ **شكراً لاختياركم AWM Charge**")

    try: bot.send_message(CHANNEL_ID, channel_post, parse_mode="Markdown")
    except: pass

    bot.send_message(ADMIN_ID, f"🔔 **طلب جديد:** {full_name}\nالطلب: {service_name}\nالآيدي: `{player_id}`", parse_mode="Markdown")
    bot.send_message(message.chat.id, f"✔️ **تم تسجيل طلبك بنجاح!**\n\nتجد طلبك الآن في قناة الإثباتات. يرجى إرسال صورة الوصل للمسؤول @{ADMIN_USER}. 🚀", reply_markup=main_menu(), parse_mode="Markdown")

print("⚡ البوت جاهز للعمل بالأسعار الجديدة!")
bot.infinity_polling()
