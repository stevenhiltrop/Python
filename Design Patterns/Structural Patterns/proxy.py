import time


class Producer:
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")


class Proxy:
    def __init__(self):
        self.is_occupied = False
        self.producer = None

    def produce(self):
        print("Artist checking if producer is available...")

        if self.is_occupied:
            time.sleep(2)
            print("Producer is busy")
        else:
            self.is_occupied = True
            producer = Producer()
            time.sleep(2)
            producer.meet()


proxy = Proxy()
proxy.produce()
proxy.produce()