# Class Program

class Greet:

    # Class attribute, protected with the underscore before the attribut/method
    _course = "Python for beginners"

    # Instance method, made private with double underscore
    def __greet_user(self):
        print("Hello User")

    def hello(self):
        print("I am Greet")


# Creating a local object and instantiating a class object
wish = Greet()
# Accessing the private method using name mangling
wish._Greet__greet_user()
wish.hello()

# Accessing the protected class attribute
print(wish._course)
