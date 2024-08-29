import os

from src.guess_number import random_number, guess_number

if __name__ == "__main__":
    list_input_number = []
    number = random_number()
    count = 14
    while True:
        dict_number = {}
        input_number = input("\nВаше число: ")
        if input_number == "0":
            break
        elif count == 0:
            print(f"ВЫ ПРОИГРАЛИ!!! Загаданное число:{number}")
            break
        elif len(input_number) == 4:
            bull, cow = guess_number(number, input_number)
            dict_number["Число"] = input_number
            dict_number["Быки"] = len(bull)
            dict_number["Коровы"] = len(cow)
            list_input_number.append(dict_number)
            os.system('cls')
            if len(bull) == 4:
                print("Поздравляю с победой")
                print("ВВЕДЕННЫЕ ЧИСЛА: ")
                for i in list_input_number:
                    print(i)
                break
            print(f"Попыток осталось: {count}\n")
            count -= 1
            print("ВВЕДЕННЫЕ ЧИСЛА: ")
            for i in list_input_number:
                print(i)
        else:
            print("Водите 4-х значное число!")


