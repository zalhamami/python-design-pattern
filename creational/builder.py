class Car:
    def __init__(self) -> None:
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self) -> str:
        return '{} has been constructed with {} and {}'.format(self.model, self.tires, self.engine)


class Builder:
    def __init__(self) -> None:
        self.car = None
    
    def create_new_car(self) -> None:
        self.car = Car()


class TeslaBuilder(Builder):
    def add_model(self):
        self.car.model = 'Tesla X'
    
    def add_tires(self):
        self.car.tires = 'Regular Tires'
    
    def add_engine(self):
        self.car.engine = 'Turbo Engine'


class Director:
    def __init__(self, builder) -> None:
        self._builder = builder
    
    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car

# Create builder instance
builder = TeslaBuilder()

# Create director instance
director = Director(builder)

# Construct car
director.construct_car()

# Get new car
new_car = director.get_car()
print(new_car)
