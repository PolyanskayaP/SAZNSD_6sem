lab1
================
ppolina353@yandex.ru

Создание примера отчета в RStudio

## Цель

1.  Ознакомиться с Quarto
2.  Написать пример отчета
3.  Найти сведения о компьютере, на котором выполняется работа

## Исходные данные

1.  Ноутбук с ОС Windows 10
2.  Приложение Ubuntu on Windows
3.  bash
4.  RStudio
5.  Quarto

## Варианты решения задачи

1.  Набирать команды в консоли, делать скрины и вставлять их в отчет в
    Word
2.  Делать чанки со скриптом bash используя Quarto, создавая readme-файл
    с отчетом

## План

1.  Создать файл Quarto (qmd)
2.  Написать bash-скрипты
3.  Проверить их выполнение

## Описание шагов

### Шаг 1

Создание файла:

![alt text](./1.png)

### Шаг 2

Написание скриптов: Т.к. установлено приложение “Ubuntu on windows”,
можно писать на bash-е

``` bash
uname -r
```

    4.4.0-19041-Microsoft

``` bash
uname -a
```

    Linux polyanskaya 4.4.0-19041-Microsoft #2311-Microsoft Tue Nov 08 17:09:00 PST 2022 x86_64 x86_64 x86_64 GNU/Linux

``` bash
lsb_release -a
```

    No LSB modules are available.
    Distributor ID: Ubuntu
    Description:    Ubuntu 20.04 LTS
    Release:    20.04
    Codename:   focal

``` bash
cat /proc/cpuinfo | grep "model name"
```

    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         

``` bash
dmesg | tail -n 30
```

    [    0.020301]  Microsoft 4.4.0-19041.2311-Microsoft 4.4.35
    [    0.158390] <3>init: (1) ERROR: ConfigInitializeCommon:665: Failed to mount /usr/lib/wsl/drive
    [    0.158394] : 19
    [    0.158703] <3>init: (1) ERROR: ConfigInitializeCommon:665: Failed to mount /usr/lib/wsl/lib
    [    0.158707] 19

### Шаг 3

Проверка работы скриптов:

![alt text](./3.png)

## Оценка результатов

Задача решена с помощью Quarto. Я научилась добавлять запуск скриптов в
отчет(readme-файл)

## Вывод

В данной работе был написан пример отчета, который в дальнейшем будет
использоваться как образец
