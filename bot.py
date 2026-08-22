import telebot
import requests

TOKEN = "8369874856:AAE412WE2psv5tRzCxEe50LK9Z2C9TT22Y8"
ADMIN_ID = 5070261597

# Eski webhookni tozalash
requests.get(f"https://api.telegram.org/bot{TOKEN}/deleteWebhook?drop_pending_updates=true")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'javob'])
def send_welcome(message):
    user = message.from_user
    
    javob_matni = (
        "💡 **Zakovat savolining to'g'ri javobi:**\n\n"
        "Suzuvchi ko'prik (Ponton ko'prigi)"
    )
    bot.reply_to(message, javob_matni, parse_mode="Markdown")
    
    admin_xabari = (
        f"🔔 **Yangi foydalanuvchi javobni ko'rdi!**\n\n"
        f"👤 Ismi: {user.first_name}\n"
        f"🔗 Username: @{user.username if user.username else 'Kiritmagan'}\n"
        f"🆔 ID raqami: {user.id}"
    )
    bot.send_message(ADMIN_ID, admin_xabari, parse_mode="Markdown")

print("Bot muvaffaqiyatli ishga tushdi!")
bot.polling()
