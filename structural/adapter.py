""" Adapter is used to generalize the function name in different classes """

class Russian:
    def __init__(self) -> None:
        self.name = 'Russian Language'
    
    def speak_russian(self) -> str:
        return 'Privet'
    

class English:
    def __init__(self) -> None:
        self.name = 'English Language'

    def speak_english(self) -> str:
        return 'Hello'
    

class Adapter:
    def __init__(self, obj, **adapted_method) -> None:
        self._object = obj
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)


russian = Russian()
english = English()

objects = [
    Adapter(russian, speak=russian.speak_russian),
    Adapter(english, speak=english.speak_english)
]

for item in objects:
    print('{} says {}'.format(item.name, item.speak()))
