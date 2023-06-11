import random
import multiprocessing


def fill_list(result_queue):
    result_queue.put([random.randint(1, 100) for _ in range(10)])


def sum_list(numbers, result_queue):
    result_queue.put(sum(numbers))


def avg_list(numbers, result_queue):
    result_queue.put(sum(numbers) / len(numbers))


if __name__ == "__main__":
    numbers_queue = multiprocessing.Queue()
    sum_queue = multiprocessing.Queue()
    avg_queue = multiprocessing.Queue()

    fill_process = multiprocessing.Process(target=fill_list, args=(numbers_queue,))
    sum_process = multiprocessing.Process(target=sum_list, args=(numbers_queue.get(), sum_queue))
    avg_process = multiprocessing.Process(target=avg_list, args=(numbers_queue.get(), avg_queue))

    fill_process.start()
    sum_process.start()
    avg_process.start()

    numbers = numbers_queue.get()
    total_sum = sum_queue.get()
    avg_value = avg_queue.get()

    fill_process.join()
    sum_process.join()
    avg_process.join()

    print("Numbers: ", numbers)
    print("Sum of numbers: ", total_sum)
    print("Average of numbers: ", avg_value)

