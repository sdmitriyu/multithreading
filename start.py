import time
import threading

def num():
    for z in range(1, 11):
        print(z)
        time.sleep(1)

def letters():
    for letter in 'abcdefghij':
        print(letter)
        time.sleep(1)

if __name__ == "__main__":
    thread1 = threading.Thread(target=num)
    thread2 = threading.Thread(target=letters)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()