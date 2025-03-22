#using *args we can pass any number of arguments to a function
#any number means infinite number of arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(1, 2, 3, 4, 5))  # 15

    
def calculate(n,**kwargs):
    # print(kwargs) # {'add': 3, 'multiply': 5}
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs)
    n += kwargs['add']#2+3= 5 = n
    n *= kwargs['multiply']#5*5=25
    print(n)


# calculate(add=3, multiply=5)  # {'add': 3, 'multiply': 5}
calculate(2,add=3, multiply=5) 


class Car:
    def __init__(self,**kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        self.color = kwargs["color"]
        
my_car = Car(make="Nissan", model="GT-R", color="Black")
print(my_car.make)  # Nissan
print(my_car.model)  # GT-R
# The **kwargs parameter allows you to pass any number of keyword arguments to the Car class.