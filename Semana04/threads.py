import threading
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

# # A função acima chamada duas vezes apenas suspende o código 
# # por 1 segundo [9] cada vez que é chamada e retorna o tempo
# # total [18]


# start = time.perf_counter()


# def do_something():
#     print('Sleeping 1 second...')
#     time.sleep(1)
#     print('Done Sleeping...')


# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')

# # Acima é definida duas threads trabalhando com a mesma função [34-35]
# # e o tempo final é de apenas 1 segundo pois ambas operam praticamente ao mesmo tempo
# # não havendo necessidade de uma terminar para começar a próxima

# start = time.perf_counter()


# def do_something():
#     print('Sleeping 1 second...')
#     time.sleep(1)
#     print('Done Sleeping...')

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something)
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')

# # Desta vez há um loop executando 10 funções em 10 threads [61]
# # e salvando-as em uma lista, o tempo continua de 1 segundo

# start = time.perf_counter()


# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     print('Done Sleeping...')

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')

# O tempo de suspensão agora é definido em [87] como argumento

# import concurrent.futures

# start = time.perf_counter()


# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     return f'Done Sleeping...{seconds}'

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = [executor.submit(do_something, sec) for sec in secs]

#     for f in concurrent.futures.as_completed(results):
#         print(f.result())



# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')

# # O tempo de suspensão agora é de uma lista [111] e a ordem é invertida


import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)
    
    for result in results:
        print(result)


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')

# # Usando map as respostas serão entregues na mesma ordem de leitura
# # mas o resultado só é entregue no fim dos 5 segundos de início da primeira

