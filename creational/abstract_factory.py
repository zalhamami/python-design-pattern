class Dog:
    def __str__(self) -> str:
        return 'Dog'

    def speak(self) -> str:
        return 'Woof!'

# Concrete factory
class DogFactory:
    def get_pet(self) -> Dog:
        return Dog()
    
    def get_food(self) -> str:
        return 'Dog Food'


# Abtract factory
class PetStore:
    def __init__(self, factory=None) -> None:
        self._factory = factory

    def show_pet(self):
        pet = self._factory.get_pet()
        pet_food = self._factory.get_food()

        print("Pet: {}".format(pet))
        print("Speak: {}".format(pet.speak()))
        print("Food: {}".format(pet_food))


# Create concrete factor instance
factory = DogFactory()

# Create abstract factory instance
store = PetStore(factory)

# Showing pet
store.show_pet()
