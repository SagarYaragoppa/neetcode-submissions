class MyHashSet:

    def __init__(self):
        self.list1 = list()

    def add(self, key: int) -> None:
        if key not in self.list1:
            self.list1.append(key)

    def remove(self, key: int) -> None:
        if key in self.list1:
            self.list1.remove(key)


    def contains(self, key: int) -> bool:
        if key in self.list1:
            return True
        else :
            return False 

