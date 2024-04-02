import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill

    def run(self):
        print(f'{self.name}, на нас напали!')
        vragi = 100
        days = 0
        while vragi > 0:
            days += 1
            print(f'{self.name} сражается {days} дней, осталось {vragi} войнов')
            vragi -= self.skill
            time.sleep(1)

        print(f'{self.name} победил за {days} дней')


knight1 = Knight('Artur', 10)
knight2 = Knight('Makar', 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
