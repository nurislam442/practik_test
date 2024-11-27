# queries
CREATE_TABLE_products = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    category TEXT,
    size TEXT,
    price TEXT,
    art TEXT,
    photo
)
"""
INSERT_PRODUCTS = """
    INSERT INTO products (product_name, category, size, price, art, photo)
    VALUES (?, ?, ?, ?, ?, ?)
"""
