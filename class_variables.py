class Car:
    type = 'Sedan'  # this is a class variable

    def __init__(self, make):
        self.make = make  # this is an instance variable


car1 = Car('Ford')  # a new instance of Car class
car2 = Car('Toyota')  # a new instance of Car class

print('type: '+ car1.type+','+'\t'+'make: '+car2.make)
print('type: '+ car1.type+','+'\t'+'make: '+car2.make)
