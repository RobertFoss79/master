class Jar:
    def __init__(self, capacity: int = 12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, number: int):
        if number > self.capacity or number + self.size > self.capacity:
            raise ValueError
        self._size += number

    def withdraw(self, number: int):
        if number > self.size:
            raise ValueError
        self._size -= number

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    
def main():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(4)
    jar.deposit(8)
    print(jar.capacity)
    print(jar.size)


if __name__ == "__main__":
    main()
