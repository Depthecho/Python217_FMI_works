import random
import multiprocessing
from math import factorial


def fill_file(file_path):
    with open(file_path, 'w') as f:
        for _ in range(100):
            f.write(str(random.randint(1, 100))+'\n')


def find_primes(file_path, result_queue):
    primes = []
    with open(file_path, 'r') as f:
        for num in f:
            n = int(num)
            if n > 1:
                for i in range(2, n):
                    if (n % i) == 0:
                        break
                else:
                    primes.append(n)
    result_queue.put(primes)


def calculate_factorial(file_path, result_queue):
    factorials = []
    with open(file_path, 'r') as f:
        for num in f:
            n = int(num)
            factorials.append(factorial(n))
    result_queue.put(factorials)


if __name__ == '__main__':
    file_path = input('Enter the path to the file: ')

    try:
        with open(file_path):
            pass
    except FileNotFoundError:
        print('File not found')
        exit()

    fill_queue = multiprocessing.Queue()
    find_primes_queue = multiprocessing.Queue()
    calculate_factorial_queue = multiprocessing.Queue()

    fill_process = multiprocessing.Process(target=fill_file, args=(file_path,))
    find_primes_process = multiprocessing.Process(target=find_primes, args=(file_path, find_primes_queue))
    calculate_factorial_process = multiprocessing.Process(target=calculate_factorial, args=(file_path, calculate_factorial_queue))

    fill_process.start()
    print('The process of filling in the file has started')

    fill_process.join()
    print('Filee is full')

    find_primes_process.start()
    calculate_factorial_process.start()

    primes = find_primes_queue.get()
    factorials = calculate_factorial_queue.get()

    find_primes_process.join()
    calculate_factorial_process.join()

    with open('primes.txt', 'w') as f:
        for prime in primes:
            f.write(str(prime)+'\n')

    with open('factorials.txt', 'w') as f:
        for factorial in factorials:
            f.write(str(factorial)+'\n')

    print('Primes found: ', len(primes))
    print('Factorials found: ', len(factorials))