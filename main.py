class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует')
House1 = House('ЖК Горский', 18)
House2 = House('Домик в деревне', 2)
House1.go_to(5)
House2.go_to(10)
