import sqlite3


def clear_table():
    """Функция выполняет очистку таблицы "weather" от данных"""

    # подключение к базе данных "weather.db"
    conn = sqlite3.connect('weather.db')

    # удаление всех записей из таблицы "weather"
    conn.execute("DELETE FROM weather")

    # сохранение изменений
    conn.commit()

    # закрытие соединения с базой данных
    conn.close()

    # вывод информации в терминал об очистке таблицы от данных
    print("Таблица с данными очищена")
