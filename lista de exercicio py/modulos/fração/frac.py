class fraction:
    def __init__(self, top, bottom):
        if not isinstance(bottom, int):
            raise AssertionError("numerador deve ser inteiro")
        else:
            a = top
            b = bottom
            while b:
                a, b = b, a % b

            self.den = bottom / a
            self.num = top / a

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(f"          {int(self.num)}")
        print("fração:  ---")
        print(f"          {int(self.den)}")

    def get_num(self):
        print(f"numerador é {self.num}")

    def get_den(self):
        print(f"denominador é {self.den}")

    def __sub__(self, otherfraction):

        new_num = self.num * otherfraction.den - self.den * otherfraction.num
        new_den = self.den * otherfraction.den
        return fraction(new_num, new_den)

    def __add__(self, otherfraction):

        new_num = self.num * otherfraction.den + self.den * otherfraction.num
        new_den = self.den * otherfraction.den
        return fraction(new_num, new_den)

    def __mul__(self, otherfraction):

        new_num = self.num * otherfraction.num
        new_den = self.den * otherfraction.den
        return fraction(new_num, new_den)

    def __truediv__(self, otherfraction):

        new_num = self.num * otherfraction.den
        new_den = self.den * otherfraction.num
        return fraction(new_num, new_den)

    def __gt__(self, otherfraction):

        return self.num * otherfraction.den > otherfraction.num * self.den

    def __ge__(self, otherfraction):

        return self.num * otherfraction.den >= otherfraction.num * self.den

    def __lt__(self, otherfraction):

        return self.num * otherfraction.den < otherfraction.num * self.den

    def __le__(self, otherfraction):

        return self.num * otherfraction.den <= otherfraction.num * self.den

    def __ne__(self, otherfraction):

        return self.num * otherfraction.den != otherfraction.num * self.den


minha_frac = fraction(4, 8.2)
minha_frac2 = fraction(6, 2)
print(minha_frac <= minha_frac2)
