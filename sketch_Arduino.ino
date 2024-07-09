//подключаем библиотеки
#include <Wire.h>        // используется для работы с шиной I2C
#include <SFE_BMP180.h>  // используется для работы с датчиком давления BMP180
#include <DHT.h>         // используется для работы с датчиком температуры и влажности DHT22

// определем константы
#define DHTPIN 2       // используем пин 2 для работы с датчиком DHT22
#define DHTTYPE DHT22  // устанавливаем тип используемого датчика

// создаем объекты dht и bmp для взаимодействия с датчиками
DHT dht(DHTPIN, DHTTYPE);
SFE_BMP180 bmp;

// инициализируем и настраиваем устройства
void setup() {
  Serial.begin(9600);  // инициализация последовательной связи с компьютером через порт URAT на скорости 9600 бод
  bmp.begin();         // инициализация датчика BMP180

  /* если инициализация прошла успешно - ничего не выводим,
  иначе выводим "BMP180 init failed" и программа останавливается на бесконечном цикле*/
  if (bmp.begin()) {} 
  else {
    Serial.println("BMP180 init failed");
    while (1) {}
  }
  dht.begin(); // инициализация датчика DHT22
}

void loop() {
  // объявляем переменные
  char status;
  double T, P, PmmHg;

  status = bmp.startTemperature(); // запуск измерения температуры

  /* если переменная status не равна нулю, то происходит задержка на указанное значение
  и затем вызов функции bmp.getTemperature(T), которая получает значение измереннной температуры и записывает его в переменную T.
  Далее, вызывается функция bmp.startPressure(3).
  Процесс повторяется и для этой функции */
  if (status != 0) {
    delay(status);
    status = bmp.getTemperature(T);
    if (status != 0) {
      status = bmp.startPressure(3);
      if (status != 0) {
        delay(status);
        status = bmp.getPressure(P, T);
        PmmHg = P * 0.750062 - 6; // переводим давление из гПа в МмРтСт и корректируем его значение
      } else {
        Serial.println("Error starting pressure measurement");
      }
    } else {
      Serial.println("Error reading temperature value");
    }
  } else {
    Serial.println("Error starting temperature measurement");
  }

  // запись измерения влажности и температуры с датчика DHT22
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  /* если в указанном участке кода происходит проверка на наличие NaN (Not-a-Number) значений в переменных humidity и temperature, 
  и если хотя бы одна из переменных содержит NaN, 
  то выводится сообщение "Error reading DHT sensor!".
  В случае, если обе переменные humidity и temperature содержат валидные числовые значения, то создается строка dataString, 
  в которой содержится значение PmmHg, humidity и temperature, разделенные запятой */
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Error reading DHT sensor!");
  } else {
    String dataString = String(PmmHg) + ',' + String(humidity) + ',' + String(temperature);
    Serial.println(dataString); // выводим в последовательный порт
    delay(2000); // ожидаем 2 секунды
  }
}
