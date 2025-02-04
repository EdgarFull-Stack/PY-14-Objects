# Example
class House:
    country = "LT"

    def __init__(self, price, year):
        self.price = price
        self.year = year

house1 = House(199000,2025)
house2 = House(165000,2008)

house1.country = ("LV")

print(house1.country, house1.price, house1.year)
print(house2.country, house2.price, house2.year)
print('-------------------------------')
# Example
house_instance_1 = House(10_000, 1990)
house_instance_2 = House(12_000, 1920)
print(house_instance_1)
print(house_instance_2)
print('-------------------------------')
# Example
from datetime import datetime

class House:
    country = "LT"

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        now = datetime.today()
        current_year = now.year
        return current_year - self.year

house_instance_1 = House(10_000, 1990)
age = house_instance_1.get_age()
print(age)

house_instance_2 = House(12_000, 1900)
print(house_instance_2.get_age())
