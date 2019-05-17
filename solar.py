class System:
    def __init__(self, name):
        self.name = name
        self.bodies = []

    def add(self, celestial_body):
        self.bodies.append(celestial_body)

    def add_multiple(self, *bodies):
        for body in bodies:
            self.add(body)

    def total_mass(self):
        total_mass = 0

        for body in self.bodies:
            total_mass += body.mass

            return total_mass

class Body(System):
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __repr__(self):
        return f'{self.name}'

    @classmethod
    def all(cls, system):
        all_list = []
        for body in system.bodies:
            if isinstance(body, cls):
                all_list.append(body)
        return all_list
    
class Planets(Body):
    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year

class Stars(Body):
    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type
    
class Moons(Body):
    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet


solar = System("Solar")

jupiter = Planets("Jupiter", 3.2, 22, 70)
mercury = Planets("Mercury", 6.2, 10, 200)
earth = Planets("Earth", 2.9, 27, 365)
mars = Planets("Mars", 6.5, 4, 55)
sun = Stars("Sun", 2, "G-Type")
northstar = Stars("North Star", 3, "G-Type")
moon1 = Moons("Europa", 4.2, "January", "Jupiter")
moon2 = Moons("Titan", 5.2, "February", "Mercury")

solar.add(mercury)

solar.add_multiple(earth, mars, sun, moon1, moon2, jupiter)

print(solar.bodies)
print(solar.total_mass())  

print(Planets.all(solar))
print(Stars.all(solar))
print(Moons.all(solar))