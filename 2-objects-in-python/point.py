class Point:
    pass

p1 = Point()
p2 = Point()

p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6

print(p1.x, p1.y)
print(p2.x, p2.y)

'''
class Pair(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second

pair = Pair(1, 2)
print(pair.sum())

class Counter(object):
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count = self.count + 1
'''
