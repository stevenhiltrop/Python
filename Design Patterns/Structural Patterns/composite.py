class Component:
    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

    def component_function(self):
        print(f"{self.name}")


class Composite(Component):
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]
        self.children = list()

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        print(f"{self.name}")

        for child in self.children:
            child.component_function()


sub1 = Composite("Submenu 1")
sub2 = Child("Submenu 2")

sub11 = Child("Sub_submenu 11")
sub12 = Child("Sub_submenu 12")

sub1.append_child(sub11)
sub1.append_child(sub12)

top = Composite("Top menu")

top.append_child(sub1)
top.append_child(sub2)

top.component_function()
