import multiprocessing

def process_hello():
    other = multiprocessing.Process(target=process_say_hello, args=())
    other.start()
    process_say_hello()

def process_say_hello():
        print('hello from', multiprocessing.current_process().name)

process_hello()
