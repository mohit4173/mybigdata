# create iterator using oops that return numbers and starting with one and each sequence will increase by one

class num:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a +=1
        return x

seq=num()
myiter=iter(seq)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
