class RandomizedSet(object):

    def __init__(self):
        self.l = []
        self.d = {}

    def insert(self, val):
        if val in self.d:
            return False
        self.d[val] = len(self.l)

        self.l.append(val)
        print(self.l, self.d)
        return True

    def remove(self, val):
        if val not in self.d:
            return False
        i, newVal = self.d[val], self.l[-1]
        self.l[i], self.d[newVal] = newVal, i
        del self.d[val]
        self.l.pop()
        print(self.l,self.d)
        return True


obj = RandomizedSet()

print(obj.insert(1))
print(obj.insert(5))
print(obj.insert(4))
print(obj.insert(6))
print(obj.remove(5))
print(obj.insert(9))

