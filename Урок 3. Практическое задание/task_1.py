"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: получения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""


#######################################################################


def speed_timer(func):
    import time

    def wrapper(arg):
        start_st = time.time()
        func(arg)
        end_st = time.time()
        print(f'[*] Время выполнения: {(end_st - start_st):.2f} сек.')

    return wrapper


@speed_timer
def list_crt(n):
    a = [i ** 2 for i in range(n)]


list_crt(10000000)


@speed_timer
def dict_crt(n):
    b = {i: i ** 2 for i in range(n)}


dict_crt(10000000)
