import sqlite3


def get_time():
    """Функция извлекает данные из столбца "time" таблицы "weather" в базе данных "weather.db" и возвращает их"""

    # подключение к базе данных "weather.db"
    conn = sqlite3.connect('weather.db')

    # генерация объекта "курсор" для работы с данными в базе данных
    cursor = conn.cursor()

    # выборка всех данных из столбца "time"
    cursor.execute("SELECT time FROM weather")

    # извлечение значений времени из таблицы
    times = [time[0] for time in cursor.fetchall()]

    # закрытие соединения с базой данных
    conn.close()

    # возврат значения "time"
    return times


def get_temperature():
    """Функция извлекает данные из столбца "temperature" таблицы "weather" в базе данных "weather.db" и возвращает их"""

    # подключение к базе данных "weather.db"
    conn = sqlite3.connect('weather.db')

    # генерация объекта "курсор" для работы с данными в базе данных
    cursor = conn.cursor()

    # выборка всех данных из столбца "temperature"
    cursor.execute("SELECT temperature FROM weather")

    # извлечение значений температуры из таблицы
    temperatures = [temp[0] for temp in cursor.fetchall()]

    # закрытие соединения с базой данных
    conn.close()

    # возврат значения "temperatures"
    return temperatures


def get_humidity():
    """Функция извлекает данные из столбца "humidity" таблицы "weather" в базе данных "weather.db" и возвращает их"""

    # подключение к базе данных "weather.db"
    conn = sqlite3.connect('weather.db')

    # генерация объекта "курсор" для работы с данными в базе данных
    cursor = conn.cursor()

    # выборка всех данных из столбца "humidity"
    cursor.execute("SELECT humidity FROM weather")

    # извлечение значений влажности из таблицы
    humidity_values = [humidity[0] for humidity in cursor.fetchall()]

    # закрытие соединения с базой данных
    conn.close()

    # возврат значения "humidity_values"
    return humidity_values


def get_pressure():
    """Функция извлекает данные из столбца "pressure" таблицы "weather" в базе данных "weather.db" и возвращает их"""

    # подключение к базе данных "weather.db"
    conn = sqlite3.connect('weather.db')

    # генерация объекта "курсор" для работы с данными в базе данных
    cursor = conn.cursor()

    # выборка всех данных из столбца "pressure"
    cursor.execute("SELECT pressure FROM weather")

    # извлечение значений давления из таблицы
    pressure_values = [pressure[0] for pressure in cursor.fetchall()]

    # закрытие соединения с базой данных
    conn.close()

    # возврат значения "pressure_values"
    return pressure_values
