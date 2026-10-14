
class MyHashMap:

    def __init__(self):
        self.list1 = []

    def put(self, key: int, value: int) -> None:
        for i in self.list1:
            if key == i[0]:
                i[1] = value
                return

        self.list1.append([key, value])

    def get(self, key: int) -> int:
        for i in self.list1:
            if key == i[0]:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        for i in self.list1:
            if key == i[0]:
                self.list1.remove(i)
                return
