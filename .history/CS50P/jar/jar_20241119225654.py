class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, number):
        if number + self.size > self.capacity:
            raise ValueError
        self.size += number

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self.capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError
        self.capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size > self._capacity:
            raise ValueError
        
def main():
    jar = Jar()
    print(jar)
    jar.deposit(6)
    print(jar)
    jar.withdraw(4)
    print(jar)
    jar.deposit(8)
    print(jar)


if __name__ == "__main__":
    main()
