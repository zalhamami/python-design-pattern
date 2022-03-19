class Borg:
    _shared_data = {}


class Singleton(Borg):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self._shared_data.update(kwargs)

    def __str__(self) -> str:
        return str(self._shared_data)


x = Singleton(Book='Good Economics for Hard Times')
print(x)

y = Singleton(Course='Economics for Managers')
print(y)