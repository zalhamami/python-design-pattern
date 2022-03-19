""" Composite is used to create a tree data structure """

class Component:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def component_function(self):
        pass


class Child(Component):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.name = args[0]

    def component_function(self):
        print(self.name)


class Composite(Component):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.name = args[0]

        # Create a variable to collect children
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        print(self.name)

        for item in self.children:
            item.component_function()


sub = Composite(' - Sub Menu 1')

sub_child_1 = Child('  -- Sub 1.1')
sub.append_child(sub_child_1)

sub_child_2 = Child('  -- Sub 1.2')
sub.append_child(sub_child_2)

top = Composite('Top Menu')
top.append_child(sub)
top.component_function()
