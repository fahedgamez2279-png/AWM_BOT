import telebot
from telebot import types

# --- الإعدادات الأساسية ---
API_TOKEN = '8751745566:AAERQxfQ5fkHca6XNzTm53HgsfmTCcrLFt0'
ADMIN_ID = 8592689169 
ADMIN_USER = "BRHOOMSE" 
CHANNEL_ID = "@AWM_Charge"
CHANNEL_LINK = "https://t.me/AWM_Charge"

bot = telebot.TeleBot(API_TOKEN)

# --- قوائم الخدمات (بأسعارك المحدثة) ---
PUBG_SERVICES = {
    "p1": {"label": "📦 60 UC", "price": "12,500 SYP"},
    "p2": {"label": "📦 325 UC", "price": "60,000 SYP"},
    "p3": {"label": "📦 660 UC", "price": "118,900 SYP"},
    "p4": {"label": "📦 1800 UC", "price": "297,400 SYP"},
    "p5": {"label": "📦 3850 UC", "price": "573,400 SYP"},
    "p6": {"label": "📦 8100 UC", "price": "1,106,100 SYP"}
}

FF_SERVICES = {
    "f1": {"label": "💎 110 Diamond", "price": "13,500 SYP"},
    "f2": {"label": "💎 221 Diamond", "price": "26,100 SYP"},
    "f3": {"label": "💎 583 Diamond", "price": "61,100 SYP"},
    "f4": {"label": "💎 1188 Diamond", "price": "119,100 SYP"},
    "f5": {"label": "💎 2420 Diamond", "price": "234,100 SYP"}
}

# --- الواجهة الرئيسية المطورة ---
def main_menu():
    markup = types.InlineKeyboardMarkup()
    
    # السطر الأول: أزرار الشحن الأساسية (جنب بعض)
    btn_pubg = types.InlineKeyboardButton("🔥 PUBG MOBILE", callback_data="list_pubg")
    btn_ff = types.InlineKeyboardButton("💎 FREE FIRE", callback_data="list_ff")
    
    # السطر الثاني: قناة الإثباتات (زر عريض)
    btn_channel = types.InlineKeyboardButton("📈 قناة الإثباتات والضمان", url=CHANNEL_LINK)
    
    # السطر الثالث: طرق الدفع والدعم (جنب بعض)
    btn_pay = types.InlineKeyboardButton("💳 طرق الدفع", callback_data="payments_menu")
    btn_supp = types.InlineKeyboardButton("🛠 الدعم الفني", callback_data="support")
    
    # بناء الهيكل
    markup.row(btn_pubg, btn_ff)
    markup.add(btn_channel)
    markup.row(btn_pay, btn_supp)
    
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = (f"👋 أهلاً بك يا {message.from_user.first_name}\n\n"
                    "🚀 **مرحباً بك في AWM Charge v2.0**\n"
                    "أسرع وأضمن خدمة شحن في سوريا ⚡️\n\n"
                    "📍 **اختر لعبتك المفضلة وابدأ الشحن فوراً:**")
    
    # ملاحظة: إذا بدك تضيف صورة البانر، ارفعها واستخدم send_photo
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu(), parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    # --- قائمة ببجي ---
    if call.data == "list_pubg":
        markup = types.InlineKeyboardMarkup(row_width=1)
        for key, item in PUBG_SERVICES.items():
            markup.add(types.InlineKeyboardButton(f"{item['label']} ➜ {item['price']}", callback_data=f"buy_pubg_{key}"))
        markup.add(types.InlineKeyboardButton("🔙 العودة للقائمة", callback_data="back_main"))
        bot.edit_message_text("📊 **قائمة أسعار ببجي (PUBG):**", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    # --- قائمة فري فاير ---
    elif call.data == "list_ff":
        markup = types.InlineKeyboardMarkup(row_width=1)
        for key, item in FF_SERVICES.items():
            markup.add(types.InlineKeyboardButton(f"{item['label']} ➜ {item['price']}", callback_data=f"buy_ff_{key}"))
        markup.add(types.InlineKeyboardButton("🔙 العودة للقائمة", callback_data="back_main"))
        bot.edit_message_text("📊 **قائمة أسعار فري فاير (Free Fire):**", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    # --- قائمة طرق الدفع ---
    elif call.data == "payments_menu":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton("📞 سيريتل كاش", callback_data="pay_syriatel"),
            types.InlineKeyboardButton("📲 MTN كاش", callback_data="pay_mtn"),
            types.InlineKeyboardButton("🏦 شام كاش", callback_data="pay_sham"),
            types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main")
        )
        bot.edit_message_text("💰 **اختر وسيلة الدفع المناسبة لك:**", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    # --- تفاصيل الدفع ---
    elif call.data.startswith("pay_"):
        if call.data == "pay_syriatel": 
            msg = "📞 **سيريتل كاش:**\n`95246739`"
        elif call.data == "pay_mtn": 
            msg = "📲 **MTN كاش:**\n`8198291506524965`"
        elif call.data == "pay_sham": 
            msg = "🏦 **شام كاش:**\n`7e311921b4cadde505444adfc0f3d2e5`"
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🚀 إرسال الوصل للمسؤول", url=f"https://t.me/{ADMIN_USER}"))
        markup.add(types.InlineKeyboardButton("🔙 العودة", callback_data="payments_menu"))
        bot.edit_message_text(f"{msg}\n\n💡 **انقر على الرقم لنسخه.**\n⚠️ يرجى إرسال لقطة شاشة للتحويل للمسؤول.", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    # --- العودة ---
    elif call.data == "back_main":
        bot.edit_message_text("📍 اختر القسم المطلوب للبدء:", call.message.chat.id, call.message.message_id, reply_markup=main_menu())

    # --- معالجة طلبات الشراء ---
    elif call.data.startswith("buy_"):
        data = call.data.split("_")
        game_type, service_key = data[1], data[2]
        
        # جلب اسم الخدمة بناءً على اللعبة
        if game_type == "pubg":
            service_name = PUBG_SERVICES[service_key]['label']
        else:
            service_name = FF_SERVICES[service_key]['label']
            
        sent_msg = bot.send_message(call.message.chat.id, f"🎯 لقد اخترت: **{service_name}**\n\n📝 أرسل الآن **(ID اللاعب)** الخاص بك:", parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, process_order, service_name)

    # --- الدعم الفني ---
    elif call.data == "support":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("💬 مراسلة المسؤول", url=f"https://t.me/{ADMIN_USER}"),
                   types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
        bot.edit_message_text(f"💡 لأي استفسار أو مشكلة، تواصل معنا مباشرة عبر الرابط أدناه ✅", call.message.chat.id, call.message.message_id, reply_markup=markup)

def process_order(message, service_name):
    player_id = message.text
    full_name = message.from_user.first_name
    user_name = f"@{message.from_user.username}" if message.from_user.username else "مخفي"

    # تنسيق الرسالة لقناة الإثباتات
    channel_post = (f"🌟 **طلب شحن جديد!**\n"
                    f"━━━━━━━━━━━━━━\n"
                    f"👤 **العميل:** {full_name}\n"
                    f"🆔 **ID اللاعب:** `{player_id}`\n"
                    f"📦 **الطلب:** {service_name}\n"
                    f"🔗 **اليوزر:** {user_name}\n"
                    "━━━━━━━━━━━━━━\n"
                    "⏳ بانتظار تأكيد الدفع من المسؤول...\n"
                    "⚡️ AWM Charge - سرعة وثقة")

    try: 
        bot.send_message(CHANNEL_ID, channel_post, parse_mode="Markdown")
    except: 
        print("خطأ: تأكد أن البوت مرفوع أدمن في القناة.")

    # إشعار للمسؤول
    bot.send_message(ADMIN_ID, f"🔔 **طلب جديد وصلك!**\n\n👤 العميل: {full_name}\n📦 الطلب: {service_name}\n🆔 الآيدي: `{player_id}`\n🔗 اليوزر: {user_name}", parse_mode="Markdown")
    
    # تأكيد للعميل
    bot.send_message(message.chat.id, f"✔️ **تم تسجيل طلبك يا {full_name}!**\n\nالآن ارسل صورة الوصل للمسؤول @{ADMIN_USER} لتنفيذ طلبك بأسرع وقت. 🚀", reply_markup=main_menu(), parse_mode="Markdown")

print("⚡ تم تحديث الواجهة! البوت يعمل الآن بأزرار احترافية.")
bot.infinity_polling()
