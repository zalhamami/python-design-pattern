class House:
    def accept(self, visitor):
        visitor.visit(self)
    
    def work_on_hvac(self, hvac_specialist):
        print(self, 'work on by', hvac_specialist)
    
    def work_on_electricity(self, electrician):
        print(self, 'work on by', electrician)
    
    def __str__(self) -> str:
        return self.__class__.__name__


class Visitor:
    """ Abstract visitor """
    def __str__(self) -> str:
        return self.__class__.__name__

    def visit(self):
        pass


class HvacSpecialist(Visitor):
    def visit(self, house):
        return house.work_on_hvac(self)
    

class Electrician(Visitor):
    def visit(self, house):
        return house.work_on_electricity(self)


hs = HvacSpecialist()
e = Electrician()

home = House()
home.accept(hs)
home.accept(e)
