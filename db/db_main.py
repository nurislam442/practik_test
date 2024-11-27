# db_main.py
import sqlite3
from db import queries
import aiosqlite

db = sqlite3.connect('db/products_tovars.sqlite3.db')
cursor = db.cursor()

cursor.execute(queries.CREATE_TABLE_products)

async def product_insert(product_name, category, size, price, art, photo):
    async with aiosqlite.connect('db/products_tovars.sqlite3.db') as db:
        await db.execute(queries.INSERT_PRODUCTS, (product_name, category, size, price, art, photo))
        await db.commit()

