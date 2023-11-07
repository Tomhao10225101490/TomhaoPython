class Complex:
    def __init__(self, real = 0, image = 0):
        self.real = real
        self.image = image
    @classmethod
    def add(cls,c1, c2):
        c = Complex()
        c.real = c1.real + c2.real
        c.image = c1.image + c2.image
        return c
if __name__ == "__main__":
    c1 = Complex(13,14)
    c2 = Complex(5,2)
    c = Complex.add(c1,c2)
    print('the result of c1 and c2 is:',c.real,c.image)