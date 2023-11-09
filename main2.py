import time
from multiprocessing import  Pool, cpu_count

def sync_factorize(*numbers):  #  Синхронный запуск
    start = time.time()
    intermediate_result = []
    for num in numbers:
        print(f'Для числа: {num}')
        for i in range(1, num+1):
            if num % i == 0:
                intermediate_result.append(i)
        print(f'Список чисел на котороые делится без остатка {intermediate_result}')
        intermediate_result = []
    print(f'Время работы функции {time.time() - start}')



def factorize(number):
    nunber_list = []
    for num in range(1, number+1):
        if number % num == 0:
            nunber_list.append(num)
    print(f'Список чисел на котороые делится без остатка {nunber_list}')

def factorize_pool(*numbers):  # запуск в многопоцессорнои пуле
    start = time.time()
    print(f'Start process {cpu_count()}')
    with Pool(cpu_count()) as pool:
        for i in numbers:
            print(f'Для числа: {i}')
            pool.apply_async(factorize(i))

    pool.close()
    pool.join()
    print(f'Время работы функции {time.time() - start}')


if __name__ == '__main__':
    print('_______________________________')
    print('Многопроцессорное:')
    factorize_pool(128, 255, 99999, 10651060)
    print('_______________________________')
    print('Синхронное выполнение:')
    sync_factorize(128, 255, 99999, 10651060)