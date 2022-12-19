class Cat:
    name = ""
    age = 0   #properties
    fur_color = ""
    breed = ""
    
    def eat (self):
        print("Cat is eating!")
                                     # function
    def sleep(self): 
        print("Cat is sleeping!")
        
        
# creating objects from
tom = Cat()
snow = Cat()
tom.name = "Tom"
tom.age = 3
tom.fur_color = 'grey'
tom.breed = 'City Cat'
snow.name = 'Snowbell'
snow.age = 5
snow.fur_color = 'white'
snow.breed = 'Persian'
 # calling methods from
 
tom.eat()
snow.sleep()
tom.sleep()

# displaying attributes

print(tom.name, tom.age, tom.fur_color, tom.breed)
print(snow.name, snow.age, snow.fur_color, snow.breed)
    