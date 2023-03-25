import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    DB_NAME = 'db.sqlite'
    MAIN_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(MAIN_PATH/DB_NAME)
    cursor = db.cursor()


def create_tables():
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        price INTEGER,
        valuta TEXT,
        photo TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        username TEXT,
        address TEXT,
        product_id     INTEGER,
        FOREIGN KEY (product_id)
            REFERENCES products(id)
            ON DELETE CASCADE
    )
    """)

    db.commit()


def add_products():
    cursor.execute("""INSERT INTO products(name, description, price, valuta, photo) VALUES 
    ('Броюки', 'джынсы', 100 ,'som', 'https://alex.kg/wp-content/uploads/2016/04/taro_earth_1_1024-scaled.jpg'),
    ('Шорты', 'летние', 200 ,'som', 'https://alex.kg/wp-content/uploads/2016/04/crowley_1024-scaled.jpg')
    """)
    db.commit()


def delete_table_products():
    cursor.execute("""DROP TABLE IF EXISTS products""")
    db.commit()



def get_products():
    cursor.execute("""
    SELECT * FROM products;
    """)
    return cursor.fetchall()



def create_clients(data):
    """
        Заполняем таблицу order
    """
    data = data.as_dict()
    cursor.execute(
        '''
        INSERT INTO orders(
        username,
        address,
        product_id
        ) VALUES (:username,:address,:product_id)''',
        {'username': data['name'],
         'address': data['address'],
         'product_id': data['product_id']})
    db.commit()






if __name__ == "__main__":
    init_db()
    delete_table_products()
    create_tables()
    add_products()
