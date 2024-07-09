import sqlite3


def create_table():
    """Функция создает таблицу weather в базе данных weather.db, если она еще не создана"""

    # подключение к базе данных "weather.db"
    conn = sqlite3.connect('weather.db')

    # генерация таблицы "weather" в базе данных, если она еще не сгенерирована
    conn.execute('''CREATE TABLE IF NOT EXISTS weather
             (time TEXT, temperature REAL, humidity REAL, pressure REAL)''')

    # сохранение изменений
    conn.commit()

    # закрытие соединения
    conn.close()
