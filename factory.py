class Car:
    def __str__(self) -> str:
        return 'This is a car'

class Plane:
    def __str__(self) -> str:
        return 'This is a plane'

def get_vehicle(name):
    vehicles = dict(
        car = Car(),
        plane = Plane()
    )
    return vehicles[name]

get_vehicle('plane')