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
    
    if (name in vehicles):
        return vehicles[name]

    return 'No vechile found'

print(get_vehicle('cars'))
