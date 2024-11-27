# main.py
from handlers import commands, product_reg, order
from config import bot, dp, staff
from aiogram import executor
import logging

async def on_startup(_):
    for i in  staff:
        await bot.send_message(chat_id=i, text="бот активирован")

commands.register_commands(dp)
product_reg.reg_handler_fsm_registration(dp)
order.register_order_handlers(dp)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)