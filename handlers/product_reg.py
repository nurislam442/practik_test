#product_reg.py
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from db import db_main
import config

class products(StatesGroup):
    product_name = State()
    category = State()
    size = State()
    price = State()
    photo = State()
    art = State()

async def start_fsm(message: types.Message):
    if message.from_user.id in config.staff:
        await message.answer("введите название товара:")
        await products.product_name.set()
    else:
        print("этой коммандой могут пользоваться лишь сотрудники")

async def load_product_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_name'] = message.text
    await products.next()
    await message.answer("ведите категорию товара")
async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await products.next()
    await message.answer("введите размер товара")

async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await products.next()
    await message.answer("введите цену товара:")

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await products.next()
    await message.answer("отправьте фото товара")

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_photo'] = message.photo[-1].file_id
    await products.next()

    await message.answer('введите айди продукта:')
async def load_productid(message: types.Message, state : FSMContext):
    async with state.proxy() as data:
        data["art"] = message.text
        await message.answer_photo(photo=data['product_photo'], caption=f"имя товара - {data['product_name']}\n"
                                                                        f"категория товара - {data['category']}\n"
                                                                        f"размер товра - {data['size']}\n"
                                                                        f"цена товара - {data['price']}\n"
                                                                        f"айди продукта - {data['art']}\n"
                                                                        f"данные записаны в базу данных")
        await db_main.product_insert(
            product_name=data["product_name"],
            category=data["category"],
            size=data['size'],
            price=data["price"],
            photo = data["product_photo"],
            art = data["art"]
        )
        await state.finish()

def reg_handler_fsm_registration(dp: Dispatcher):
    dp.register_message_handler(start_fsm, commands=['tovar_reg'])
    dp.register_message_handler(load_product_name, state=products.product_name)
    dp.register_message_handler(load_size, state=products.size)
    dp.register_message_handler(load_price, state=products.price)
    dp.register_message_handler(load_category, state=products.category)
    dp.register_message_handler(load_productid, state=products.art)
    dp.register_message_handler(load_photo,state=products.photo, content_types=["photo"])

