# commands.py
from aiogram import types, Dispatcher
from config import bot, dp
from db import db_main
import aiosqlite


async def info(message: types.Message):
    await message.answer(text="это бот для заказа товаров:\n"
                              "команды:\n"
                              "/start\n"
                              "/info\n"
                              "/tovar_reg - только для сотрудников\n"
                              "/products\n"
                              "/order")
async def start(message: types.Message):
    await message.answer(text=f"привет {message.from_user.first_name} \nдля получения информации и комманд напишите команду /info")

async def products(message: types.Message):
    async with aiosqlite.connect('db/products_tovars.sqlite3.db') as db:
        async with db.execute("SELECT * FROM products") as cursor:
            rows = await cursor.fetchall()
            if rows:
                for row in rows:

                    product_id, name, category, size, price, art, photo = row
                    await message.answer_photo(
                        photo=photo,
                        caption=(
                            f"Товар {product_id}:\n"
                            f"Название: {name}\n"
                            f"Категория: {category}\n"
                            f"Размер: {size}\n"
                            f"Цена: {price}\n"
                            f"Артикул: {art}"
                        )
                    )
            else:
                await message.answer("В базе данных пока нет товаров.")


def register_commands(dp: Dispatcher):
    dp.register_message_handler(info, commands=["info"])
    dp.register_message_handler(start,commands=["start"])
    dp.register_message_handler(products, commands=["products"])
