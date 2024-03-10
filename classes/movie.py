class Movie:
    class_attribute = 10

    def __init__(self, name : str, age: int , address: str):
        self.name = name
        self.age = age
        self.address = address

    @staticmethod
    def say_hello():
        print("Hello there!")

    def hello(self):
        print(f"Hello {self.name}")

    def __str__(self):
        return f'{self.name} {self.age} {self.address}**'
    
    def __repr__(self):
        return f'{self.name} {self.age} {self.address}++'

