class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies")
        self.size = self.size + n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies")
        self.size - n

    @property
    def capacity(self):
        return self.capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Not enough cookies")
        self.capacity = capacity

    @property
    def size(self):
        return self.size
    
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Too many cookies")
        
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
