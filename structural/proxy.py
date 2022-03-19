""" Proxy is used to postpone the creation of object """

import time


class Producer:
    def meet(self):
        print('Producer has time to meet you now!')


class Proxy:
    def __init__(self) -> None:
        self.busy = 0
        self.producer = None
    
    def meet_producer(self):        
        print("Checking if the producer is availabole..")

            # Delay for 2 seconds
        time.sleep(2)

        if self.busy == 0:
            self.producer = Producer()
            return self.producer.meet()
        
        print('Producer is busy!')

p = Proxy()
# p.meet_producer()

# Change the state of proxy
p.busy = 1
p.meet_producer()
