class MyClass:
    count = 0  # Class attribute

    def __init__(self):
        MyClass.count += 1  # Increment the 'count' class attribute by 1

    @classmethod
    def get_count(cls):
        return cls.count  # Return the 'count' class attribute
    

    
    def get_count1(self):
        return self.count  # Return the 'count' class attribute
