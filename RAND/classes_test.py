class Human():
    def __init__(self, name, age=None, mother = None, childs = []):
        self.name = name
        self.age = age
        self.mother = mother
        self.childs = childs

    def __str__(self):
        return f'human named {self.name} aged {self.age}'

    def set_mother(self, mom):
        self.mother = mom
        mom.childs.append(self)

    def print_mother(self):
        if self.mother is not None:
            print(self.mother)
        else:
            print('i am an orphan((((')

    def set_child(self, child):
        self.childs.append(child)
        child.mother = self

    def print_children(self):
        for x in self.childs:
            print(f" {x}")


# class John(Human):

#     def __init__(self, mood=None, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.mood = mood


def hi():
    print('hi')