import time
import multiprocessing


#  def get_max(my_list, my_locker):
#      my_locker.acquire()  # метод блокировки процесса
#      time.sleep(2)
#      print(max(my_list))
#      print(f"Process '{multiprocessing.current_process().name}' was been ended")
#      my_locker.release()  # метод разблокировки процесса
#
#
#  def get_min(my_list):
#      time.sleep(2)
#      print(min(my_list))
#      print(f"Process '{multiprocessing.current_process().name}' was been ended")
#
#
#  if __name__ == '__main__':
#      numbers = list(map(int, input('Enter numbers over space: ').split()))
#      locker = multiprocessing.Lock()
#      pr = multiprocessing.Process(target=get_max, name='Max', args=(numbers, locker))
#      pr2 = multiprocessing.Process(target=get_min, name='Min', args=(numbers, ))
#      start = time.time()
#      pr.start()
#      pr.join()
#      pr2.start()
#      print(f'Here main process {multiprocessing.current_process().name} had been ended'
#            f'Time of process: {time.time() - start}')


# def get_max(my_list):
#     summ = sum(my_list)
#     print(summ)
#     print(f"Process '{multiprocessing.current_process().name}' was been ended")
#
#
# def get_avg(my_list):
#     avg = (sum(my_list) / len(my_list))
#     print(avg)
#     print(f"Process '{multiprocessing.current_process().name}' was been ended")
#
#
# if __name__ == '__main__':
#     numbers = list(map(int, input('Enter numbers over space: ').split()))
#     pr = multiprocessing.Process(target=get_max, name='Max', args=(numbers, ))
#     pr2 = multiprocessing.Process(target=get_avg, name='Avg', args=(numbers, ))
#     pr.start()
#     pr2.start()
#     pr.join()
def func(i):
    name = multiprocessing.current_process().name
    print(f'Process {name} i had been ended')
    time.sleep(2)
    print('123')


if __name__ == '__main__':
    count = multiprocessing.cpu_count()
    print(count)
    with multiprocessing.Pool(2) as p:
        p.map(func, [1, 2, 3])