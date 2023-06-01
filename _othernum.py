from typing import overload
from _alias import *
import _bsc as b

class frac():
    @overload
    def __init__(self, Number: float): ...
    @overload
    def __init__(self, Fraction: str): ...
    @overload
    def __init__(self, Numerator: Number, Denominator: Number = None): ...
        
    def __init__(self, Numerator: Number, Denominator: Number = None):
        if (type(Numerator) and type(Denominator) is (int or float)):
            c = b.mdc(Numerator, Denominator)
            self.n, self.d = Numerator // c, Denominator // c
        elif type(Numerator) is int:
            self.n, self.d = Numerator, 1
        elif type(Numerator) is frac:
            self.n, self.d = Numerator.n, Numerator.d
        elif type(Numerator) is float:
            c = self.convert(Numerator)
            self.n, self.d = c[0], c[1]
        elif type(Numerator) is str:
            c = Numerator.split("/")
            self.n, self.d = float(c[0]), float(c[1])
        
        if self.n < 0 and self.d < 0:
            self.n, self.d = abs(self.n), abs(self.d)
        elif self.d < 0:
            self.n -= self.n
        
        self.value = b.reduzir(self.n / self.d)
        self.n = b.reduzir(self.n)
        self.d = b.reduzir(self.d)
        
    # Funções internas ====================
    def convert(self, f):
        r = str(f).split(".")
        s = [int(r[0] + r[1]),
            int("1" + (len(r[1]) * "0"))] 
        c = b.mdc(s[0], s[1])
        return [s[0] // c, s[1] // c]
    
    def invert(self):
        self.n, self.d = self.d, self.n
    
    # Tratamento do objeto ====================
    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return f"{self.n}/{self.d}"
    def __int__(self) -> int:
        return self.n // self.d
    def __float__(self) -> float:
        return self.value
    def __neg__(self):
        return frac(-self.n, self.d)
    def __getitem__(self, key):
        match key:
            case 0:
                return self.n
            case 1:
                return self.d
    def __setitem__(self, key, value):
        match key:
            case 0:
                self.n = value
            case 1:
                self.d = value
    
    # Operações Matematicas ====================
    
    def __add__(self, other):
        x = frac(other)
        return frac(
            self.n + x.n,
            b.mmc(self.n, x.n),
        )
    def __radd__(self, other): return self.__add__(other)
    def __iadd__(self, other): return self.__add__(other)
    
    
    def __sub__(self, other):
        x = frac(other)
        return frac(
            self.n - x.n,
            b.mmc(self.d, x.d),
        )
    def __rsub__(self, other): return -frac(self.n, self.d) + other
    def __isub__(self, other): return self.__sub__(other)

    
    def __mul__(self, other):
        x = frac(other)
        return frac(
            self.n * x.n,
            self.d * x.d
        )
    def __rmul__(self, other): return self.__mul__(other)
    def __imul__(self, other): return self.__mul__(other)
    
    def __truediv__(self, other):
        x = frac(other)
        return frac(
            self.n * x.d,
            self.d * x.n
        )
    def __rtruediv__(self, other):
        x = frac(other)
        return frac(
            x.d * self.n,
            x.n * self.d
        )
    def __itruediv__(self, other): return self.__truediv__(other)
    
    def __pow__(self, other):
        x = frac(other)
        if x.n < 0:
            self.invert()
        return frac(
            self.n ** x.value,
            self.d ** x.value
        )
    def __rpow__(self, other):
        x = frac(other)
        if x.n < 0:
            self.invert()
        return frac(
            x.n ** self.value,
            x.d ** self.value
        )
    def __ipow__(self, other): return self.__pow__(other)
    
    # Operadores logicos =============================
    

# print(frac(1, 2) + 2)           #   3/2
# print(2 + frac(1, 2))           #   3/2
# print(frac(1, 2) - 2)           #  -1/2
# print(2 - frac(1, 2))           #   1/2
# print(frac(1, 2) * 2)           #   1/1
# print(2 * frac(1, 2))           #   1/1
# print(frac(1, 2) / 2)           #   1/4
# print(2 / frac(1, 2))           #   1/4
# print(frac(1, 2) ** 3)          #   1/8
# print(3 ** frac(1, 2).value)    #   1.7320

# 3/2
# 3/2
# -1/2
# 1/2
# 1/1
# 1/1
# 1/4
# 1/4
# 1/8
# 4330127018922193/2500000000000000