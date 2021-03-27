import multiprocessing
import time

# start = time.perf_counter()


# def do_something():
#     print('Sleeping 1 second...')
#     time.sleep(1)
#     print('Done Sleeping...')


# do_something()
# do_something()

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')

# # Aqui acima a função é repetida duas vezes de forma síncrona e o tempo total
# # é a soma do tempo de cada execução

# start = time.perf_counter()


# def do_something():
#     print('Sleeping 1 second...')
#     time.sleep(1)
#     print('Done Sleeping...')


# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')

# # Aqui com join é garatido que assim que o processo tiver sido completo
# # ele entra nos parâmetros abaixo do código. Nesse caso a função é chamada
# # duas vezes mas é executada em multiprocessamento levando apenas o tempo de uma execução

# start = time.perf_counter()


# def do_something():
#     print('Sleeping 1 second...')
#     time.sleep(1)
#     print('Done Sleeping...')

# processes = []

# for _ in range(10):
#     p = multiprocessing.Process(target=do_something)
#     p.start()
#     processes.append(p)
    
# for process in processes:
#     process.join()

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')

# # Uma lista de processos é criada e a cada vez que passa pelo laço é criado um processo
# # Para cada passo no laço utilizado, aloca-se o processo ao final da lista, desse modo garante-se que quando chegar
# # no último parametro dessa lista, a função implementada garante que o fim do processo foi atingido 

# start = time.perf_counter()


# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     print('Done Sleeping...')

# processes = []

# for _ in range(10):
#     p = multiprocessing.Process(target=do_something, args=[1.5])
#     p.start()
#     processes.append(p)
    
# for process in processes:
#     process.join()

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')

# # O tempo de suspensão agora é definido como argumento em [86]

import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')

# # O tempo de suspensão agora é de uma lista [110] e a ordem é invertida