
import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    DB_NAME = 'db.sqlite'
    MAIN_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(MAIN_PATH/DB_NAME)
    cursor = db.cursor()


def create_tables():
    """ делаем таблицу продуктов и таблицу заказов """
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
        age INTEGER,
        address TEXT,
        delivery_day TEXT,
        product_id INTEGER,
        FOREIGN KEY (product_id)
            REFERENCES products(id)
            ON DELETE CASCADE
    )
    """)

    db.commit()


def add_products():
    """добавляем данные в таблицу product"""
    cursor.execute("""INSERT INTO products(name, description, price, valuta, photo) VALUES 
    ('Броюки', 'джынсовые', 100 ,'som', 'https://alex.kg/wp-content/uploads/2016/04/taro_earth_1_1024-scaled.jpg'),
    ('Шорты', 'летние', 200 ,'som', 'https://alex.kg/wp-content/uploads/2016/04/crowley_1024-scaled.jpg')
    """)
    db.commit()


def delete_table_products():
    """ удаляем лишнее обновленные данные из таблицы product" """
    cursor.execute("""DROP TABLE IF EXISTS products""")
    db.commit()



def get_products():
    """ получаем данные из таблицы product"""
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
        age,
        address,
        delivery_day,
        product_id
        ) VALUES (:username,:age,:address,:delivery_day,:product_id)''',
        {'username': data['name'],
         'age': data['age'],
         'address': data['address'],
         'delivery_day': data['delivery_day'],
         'product_id': data['product_id']})
    db.commit()






if __name__ == "__main__":
    init_db()
    delete_table_products()
    create_tables()
    add_products()












