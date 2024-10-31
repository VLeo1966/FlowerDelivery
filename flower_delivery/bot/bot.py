import telebot
from django.conf import settings
from orders.models import Order
from flower_catalog.models import Flower

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.reply_to(message, "Добро пожаловать в сервис доставки цветов! Мы сообщим о вашем заказе здесь.")

def send_order_notification(order_id):
    order = Order.objects.get(id=order_id)
    flower = order.flower
    message = (
        f"Новый заказ:\n"
        f"Покупатель: {order.user.username}\n"
        f"Букет: {flower.name}\n"
        f"Количество: {order.quantity}\n"
        f"Адрес доставки: {order.delivery_address}\n"
        f"Дата доставки: {order.delivery_date}"
    )
    bot.send_message(settings.TELEGRAM_CHANNEL_ID, message)

bot.polling()
