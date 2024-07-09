import sqlite3
import time
import serial


def write_data():
    """Функция записывает данные, полученные из COM3 порта, а также время, в которое были получены данные,
    в таблицу weather базы данных"""

    # подключение к COM3 порту
    ser = serial.Serial('COM3', 9600)

    # подключение к базе данных "weather.db"
    conn = sqlite3.connect('weather.db')

    # генерация объекта "курсор" для работы с данными в базе данных
    cursor = conn.cursor()

    try:
        while True:
            if ser.in_waiting > 0:  # Проверяем, появились ли новые данные в COM порту
                # считывание строки данных из последовательного порта, декодирование и удаление лишних пробелов
                ser_data = ser.readline().decode().strip()

                # разделение строки данных на отдельные значения
                pressure, humidity, temperature = ser_data.split(',')

                # формирование строки с текущим временем
                current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

                # вставка текущего времени, температуры, влажности и давления в таблицу weather
                cursor.execute("INSERT INTO weather (time, temperature, humidity, pressure) VALUES (?, ?, ?, ?)",
                               (current_time, float(temperature), float(humidity), float(pressure)))

                # сохранение изменений
                conn.commit()

                # вывод информации в терминал о записи данных в базу данных weather.db
                print(
                    f"Данные записаны в базу данных: {current_time}, Температура: {temperature} °C, "
                    f"Влажность: {humidity} %, Давление: {pressure} ммРтСт")

    except KeyboardInterrupt:
        # Обработка прерывания с клавиатуры
        print("Программа завершена по запросу пользователя")

    finally:
        # закрытие соединения с базой данных при выходе из цикла
        conn.close()
