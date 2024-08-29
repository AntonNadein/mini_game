import random


def random_number():
    """Рандомное четырехзначное число"""
    return random.randint(1000, 9999)


def guess_number(number, input_number):
    """Логика подсказок"""
    bull = []
    cow = []
    number = str(number)
    for i in range(4):
        if input_number[i] == number[i]:
            bull.append(input_number[i])
        elif number[i] in input_number:
            cow.append(number[i])
    return bull, cow
