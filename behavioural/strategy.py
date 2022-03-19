""" Strategy pattern is used to override the default function in the abstract class """
import types

class Strategy:
    def __init__(self, function=None) -> None:
        self.name = 'Default Strategy'

        if function:
            self.execute = types.MethodType(function, self)
    
    def execute(self):
        print('{} is used!'.format(self.name))

def strategy_one(self):
    print('{} is used in the method 1'.format(self.name))

def strategy_two(self):
    print('{} is used in the method 2'.format(self.name))

# Executing the default strategy
s0 = Strategy()
s0.execute()

# Strategy one to override the default strategy
s1 = Strategy(strategy_one)
s1.execute()

# Strategy two to override the default strategy
s2 = Strategy(strategy_two)
s2.execute()
