class Observer:
    def __init__(self) -> None:
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
    

class Core(Observer):
    def __init__(self, name) -> None:
        super().__init__()
        self._name = name
        self._temp = 0
    
    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, val):
        self._temp = val
        # Notify using observer
        self.notify()


class TempViewer:
    def update(self, core):
        print('Temperature {} has changed to {}'.format(core._name, core._temp))


# Init core system
c1 = Core('Core 1')
c2 = Core('Core 2')

# Attach observer to core system
obs = TempViewer()
c1.attach(obs)
c2.attach(obs)

# Change core temperature
c1.temp = 10
c2.temp = 30
