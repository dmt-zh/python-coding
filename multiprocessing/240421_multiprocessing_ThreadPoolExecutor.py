# Как известно, пул потоков использует не демонические дочерние потоки, а значит даже при использовании методов завершения,
# все равно придется дождаться окончания выполнения уже запущенных задач потоков пула. Это может стать проблемой. Если одна
# или несколько таких задач "зависнут", весь процесс также зависнет, ведь в нем останутся активные потоки. Но этого можно избежать,
# если выполнять пул потоков в отдельном дочернем процессе. Ведь в отличие от потоков, у нас есть методы завершения работы 
# дочернего процесса.

# Есть список функций - запросов и список внешних ресурсов для этих запросов:

# tasks = [функция1, функция2, функция3, ....]
# sources = [ссылка1_для_функции1, ссылка2_для_функции 2, ...]

# Ваша задача написать функцию request_handler, которая:
# Принимает три позиционных аргумента: список задач-запросов, список ссылок, значение уставки таймаута (в секундах).
# Создает дополнительный дочерний процесс, который и выполняет всю работу, а именно:
# создает пул потоков для выполнения запросов: каждая задача - запрос выполняется со своей ссылкой, каждая задача 
# выполняется отдельным потоком пула. Ограничивает работу установленным таймаутом.


from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process


def task_runner(requests, sources):
    with ThreadPoolExecutor() as executor:
        for func, url in zip(requests, sources):
            executor.submit(func, url)

def request_handler(requests, sources, timeout=None):
    minor_process = Process(target=task_runner, args=(requests, sources), daemon=True)
    minor_process.start()
    minor_process.join(timeout=timeout)
    if minor_process.is_alive():
        minor_process.terminate()
        minor_process.join()
        minor_process.close()