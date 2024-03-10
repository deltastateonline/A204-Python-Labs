from classes.movie import Movie
from classes.myclass import MyClass

def main():

    a : Movie = Movie("Damsel", 23, 'lawnton qld')
    print(a)
    print(a.__dict__)
    print(a.__repr__())
    print(a.__str__())


    a = MyClass()
    b = MyClass()
    c = MyClass()
    d = MyClass()

    # Call the class method
    print(MyClass.get_count())  # Output: 3
    print(d.get_count1())


if __name__ == "__main__":
    main()