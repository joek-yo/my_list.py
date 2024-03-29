class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender =gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Create an instance of the person class
person1 = Person("Joseph", 30, "Male")
# Call the introduce method to display the personn's information
person1.introduce()