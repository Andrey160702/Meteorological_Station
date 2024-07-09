import Create_db
import Get_data
import Take_data
import Clear_table
import time
import matplotlib.pyplot as plt


def temp_graph():
    """Функция строит график зависимости температуры от времени"""
    plt.figure(figsize=(10, 20))
    plt.plot(times_formatted, temperatures, label='Температура', marker='o', color='b', linestyle='-')
    plt.title('Графики зависимости температуры от времени ({})'.format(times[0][:10]))
    plt.xlabel('Время')
    plt.ylabel('Температура, °C')
    plt.xticks(rotation=45)

    # Преобразуем значения температуры в целые числа
    temperature_values_int = [int(value) for value in temperatures]

    # Устанавливаем нужные значения и шаги на оси y
    plt.yticks(range(min(temperature_values_int) - 2, max(temperature_values_int) + 4, 1))  # Здесь шаг равен 1

    plt.grid(True)
    plt.show()


def humidity_graph():
    """Функция строит график зависимости влажности от времени"""
    plt.figure(figsize=(10, 20))
    plt.plot(times_formatted, humidity_values, label='Влажность', marker='o', color='g', linestyle='-')
    plt.title('Графики зависимости влажности от времени ({})'.format(times[0][:10]))
    plt.xlabel('Время')
    plt.ylabel('Влажность, %')
    plt.xticks(rotation=45)

    # Преобразуем значения влажности в целые числа
    humidity_values_int = [int(value) for value in humidity_values]

    # Устанавливаем нужные значения и шаги на оси y
    plt.yticks(range(min(humidity_values_int) - 2, max(humidity_values_int) + 4, 2))  # Здесь шаг равен 2

    plt.grid(True)
    plt.show()


def pressure_graph():
    """Функция строит график давления от времени"""
    plt.figure(figsize=(10, 20))
    plt.plot(times_formatted, pressure_values, label='Давление', marker='o', color='r', linestyle='-')
    plt.title('Графики зависимости давления от времени ({})'.format(times[0][:10]))
    plt.xlabel('Время')
    plt.ylabel('Давление, ммРтСт')
    plt.xticks(rotation=45)

    # Преобразуем значения давления в целые числа
    pressure_values_int = [int(value) for value in pressure_values]

    # Устанавливаем нужные значения и шаги на оси y
    plt.yticks(range(min(pressure_values_int) - 2, max(pressure_values_int) + 4, 1))  # Здесь шаг равен 1

    plt.grid(True)
    plt.show()


# Вызов функции создания таблицы в базе данных
Create_db.create_table()

# Задаем интервал чтения данных из COM порта и интервал очистки таблицы
write_interval = 5  # 2.5 минуты
clear_interval = 120  # час
last_write_time = time.time()
last_clear_time = time.time()

while True:
    # Пишем текущее время в переменную current_time
    current_time = time.time()

    # Вызов функции write_data() с указанным интервалом
    if current_time - last_write_time >= write_interval:
        Get_data.write_data()
        last_write_time = current_time

    # Если соблюдено условие, то форматируем время в нужный формат, пишем данные из таблицы в переменные,
    # строим графики, выводим среднесуточную температуру и очищаем таблицу
    if current_time - last_clear_time >= clear_interval:
        times = Take_data.get_time()
        times_formatted = [time.strftime("%H:%M:%S",
                                         time.strptime(time_str, "%Y-%m-%d %H:%M:%S")) for time_str in times]
        temperatures = Take_data.get_temperature()
        humidity_values = Take_data.get_humidity()
        pressure_values = Take_data.get_pressure()

        temp_graph()
        humidity_graph()
        pressure_graph()

        print(f"Среднесуточная температура: {round(sum(temperatures) / len(temperatures), 2)} °C")

        Clear_table.clear_table()
        last_clear_time = current_time
