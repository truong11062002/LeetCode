class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    def __add__(a, b):
        return a.age + b.age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Create an instance of the Person class
person1 = Person("Alice", 30)
# Access and modify instance attributes directly
print(person1.__dict__)  # Output: {'name': 'Alice', 'age': 30}
print(person1 + person1)  # Output: 60
print(person1)
