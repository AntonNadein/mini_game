# Быки и коровы

## Описание:

Логическая игра "Быки и коровы". В ходе которой за 10 попыток игрок должен угадать, какое число 
загадал компьютер.

## Использование:
* Клонируем репозитроий *git@github.com:AntonNadein/mini_game.git*
* Устанавливаем зависимоти **pyproject.toml**
* Запускаем функционал при помощи файлов **main.py,**

## Правила игры:
Программа загадывает 4-значное число с повторяющимися цифрами. Игрок, должен угадать данное число за 10 попыток.
Программа дает подсказки для игрока в виде положения и правилости отдельной цифры числа. Дает ответ в быках и коровах.
Например:
Задумано тайное число «3219».
Попытка: «2310».
Результат: две «коровы» (две цифры: «2» и «3» — угаданы на НЕверных позициях) и один «бык» 
(одна цифра «1» угадана вплоть до позиции).
Задумано тайное число «1119».
Попытка: «2189».
Результат: две «коровы» (две цифры: «1» — угаданы на НЕверных позициях) и два «быка» 
(одна цифра «1» и «9» угадана вплоть до позиции).
Попытка: «1456».
Результат: две «коровы» (цифра: «1» — угадана на НЕверных позициях) и один «бык» 
(одна цифра «1» угадана вплоть до позиции).



## Документация:
Вся логика игры находится в модуле **[program_shell.py](src%2Fprogram_shell.py)** оболочка создана
при помощи графического фреймворка Qt, набора расширений PyQt6. И программы Qt Designer.



## Лицензия:

Этот проект не имеет лицензий.