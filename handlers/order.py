# order.py
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from config import staff
class OrderStates(StatesGroup):
    art = State()
    size = State()
    quantity = State()
    contact = State()

async def start_order(message: types.Message):
    await message.answer("Введите артикул товара, который хотите купить:")
    await OrderStates.art.set()

async def load_art(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['art'] = message.text
    await OrderStates.next()
    await message.answer("Введите размер товара:")

async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await OrderStates.next()
    await message.answer("Введите количество товара:")

async def load_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text
    await OrderStates.next()
    await message.answer("Введите свои контактные данные (например, номер телефона):")
async def load_contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact'] = message.text
        await message.answer(
            f"Ваш заказ оформлен!\n\n"
            f"Артикул товара: {data['art']}\n"
            f"Размер: {data['size']}\n"
            f"Количество: {data['quantity']}\n"
            f"Контактные данные: {data['contact']}\n"
            f"Спасибо за ваш заказ!"
        )
    for i in staff:
        await message.answer(
            f"поступил новый заказ:\n"
            f"Артикул товара: {data['art']}\n"
            f"Размер: {data['size']}\n"
            f"Количество: {data['quantity']}\n"
            f"Контактные данные: {data['contact']}\n")

    await state.finish()

def register_order_handlers(dp: Dispatcher):
    dp.register_message_handler(start_order, commands=['order'], state=None)
    dp.register_message_handler(load_art, state=OrderStates.art)
    dp.register_message_handler(load_size, state=OrderStates.size)
    dp.register_message_handler(load_quantity, state=OrderStates.quantity)
    dp.register_message_handler(load_contact, state=OrderStates.contact)
