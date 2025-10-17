class Human():
    def __init__(self, name, age=None, father=None, spouse=None, childs = []):
        self.name = name
        self.age = age
        self.mother = mother
        self.father = father
        self.childs = childs
        self.spouse = spouse
        self.ex_spouses = []

    def __str__(self):
        return f'human named {self.name} aged {self.age}'

    def check_age_difference(self, parent):
        if self.age is not None and parent.age is not None:
            return parent.age - self.age >= 15
        return True
    

    def check_incest(self, relative):
        if relative in (self.mother, self.father) or relative in self.childs:
            return False
        if self.mother and relative in self.mother.childs:
            return False
        if self.father and relative in self.father.childs:
            return False
        return True

    def set_mother(self, mom):
        self.mother = mom
        if not self.check_age_difference(mom):
            print("Mother must be at least 15 years older than child")
            return
        if not self.check_incest(mom):
            print("No incest here!")
            return
        if self not in mom.childs:
            mom.childs.append(self)

    def set_father(self, dad):
        self.father = dad
        if not self.check_age_difference(dad):
            print("Father must be at least 15 years older than child")
            return
        if not self.check_incest(dad):
            print("No incest here!")
            return
        if self not in dad.childs:
            dad.childs.append(self)

    def set_spouse(self, partner):
        partner.spouse = self #❗
        if self.spouse == partner:
            return
        if not self.check_incest(partner):
            print("Incest restriction violated!")
            return
        if self.spouse:
            self.ex_spouses.append(self.spouse)
            self.spouse.spouse = None
        if partner in self.ex_spouses:
            self.ex_spouses.remove(partner)
        self.spouse = partner

    def print_mother(self):
        if self.mother is not None:
            print(self.mother)
        else:
            print('i am an orphan((((')
  
    def set_child(self, child):
        # ❗ incest?? age?? no duplicates??
        self.childs.append(child)
        child.mother = self

    def print_children(self):
        for x in self.childs:
            print(f" {x}")
    
    def print_father(self):
        if self.father is not None:
            print(self.father)
        else:
            print('I have no father(((')

    def print_spouse(self):
        if self.spouse is not None:
            print(self.spouse)
        else:
            print('I am single')

    def print_ex_spouses(self):
        if self.ex_spouses:
            for ex in self.ex_spouses:
                print(ex)
        else:
            print('No ex-spouses')

def get_same_children(human1, human2):
        childs = []
        for child in human1.childs:
            if child in human2.childs:
                    childs.append(child)
        return childs