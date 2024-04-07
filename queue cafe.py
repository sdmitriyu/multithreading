import threading
import time
import queue

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue()

    def client_come_in(self):
        for i in range(1, 21):
            time.sleep(1)
            print(f"Посетитель номер {i} прибыл")
            customer = Customer(i)
            self.service(customer)

    def service(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.id} сел за стол {table.number} (начало обслуживания)")
                time.sleep(5)
                print(f"Посетитель номер {customer.id} покушал и ушёл (конец обслуживания)")
                table.is_busy = False
                return
        print(f"Посетитель номер {customer.id} ожидает свободный стол (помещение в очередь)")
        self.queue.put(customer)

class Customer(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        time.sleep(5)

table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.client_come_in)
customer_arrival_thread.start()

customer_arrival_thread.join()