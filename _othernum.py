# Other Numbers (#003)

from typing import overload
from _alias import Number
from _bsc import arred, mmc, mdc, reduzir, rad, fat

class frac():
    @overload
    def __init__(self, Number: float): ...
    @overload
    def __init__(self, Fraction: str): ...
    @overload
    def __init__(self, Numerator: Number, Denominator: Number = None): ...
        
    def __init__(self, Numerator: Number, Denominator: Number = None):
        if (type(Numerator) and type(Denominator) is (int or float)):
            c = mdc(Numerator, Denominator)
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
        
        self.value = reduzir(self.n / self.d)
        self.n = reduzir(self.n)
        self.d = reduzir(self.d)
        
    # Funções internas ====================
    def convert(self, f):
        r = str(f).split(".")
        s = [int(r[0] + r[1]),
            int("1" + (len(r[1]) * "0"))] 
        c = mdc(s[0], s[1])
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
        z = frac(
            self.n + x.n,
            mmc(self.n, x.n),
        )
        if z.d == 1:
            return z.n
        return z
    def __radd__(self, other): return self.__add__(other)
    def __iadd__(self, other): return self.__add__(other)
    
    
    def __sub__(self, other):
        x = frac(other)
        z = frac(
            self.n - x.n,
            mmc(self.d, x.d),
        )
        if z.d == 1:
            return z.n
        return z
    def __rsub__(self, other): return -frac(self.n, self.d) + other
    def __isub__(self, other): return self.__sub__(other)

    
    def __mul__(self, other):
        x = frac(other)
        z = frac(
            self.n * x.n,
            self.d * x.d
        )
        if z.d == 1:
            return z.n
        return z
    def __rmul__(self, other): return self.__mul__(other)
    def __imul__(self, other): return self.__mul__(other)
    
    def __truediv__(self, other):
        x = frac(other)
        z = frac(
            self.n * x.d,
            self.d * x.n
        )
        if z.d == 1:
            return z.n
        return z
    def __rtruediv__(self, other):
        x = frac(other)
        z = frac(
            x.d * self.n,
            x.n * self.d
        )
        if z.d == 1:
            return z.n
        return z
    def __itruediv__(self, other): return self.__truediv__(other)
    
    def __pow__(self, other):
        x = frac(other)
        if x.n < 0:
            self.invert()
        z = frac(
            self.n ** x.value,
            self.d ** x.value
        )
        if z.d == 1:
            return z.n
        return z
    def __rpow__(self, other):
        x = frac(other)
        if x.n < 0:
            self.invert()
        z = frac(
            x.n ** self.value,
            x.d ** self.value
        )
        if z.d == 1:
            return z.n
        return z
    def __ipow__(self, other): return self.__pow__(other)
    
    # Operadores logicos =============================

pi = 3.1415926535897932


class deg():
    def __init__(self, valor: Number):
        self.__ang__ = valor
        self.__val__ = None
        self.__cos0__ = None
        self.__sin0__ = None
        self.__tan0__ = None
        self.__cot0__ = None
        self.__sec0__ = None
        self.__csc0__ = None
        
    @property 
    def cos(self):
        if self.__cos0__ == None:
            self.__cos0__ = arred(self.__cos__(), 5)
        return self.__cos0__
    @property 
    def sin(self):
        if self.__sin0__ == None:
            self.__sin0__ = arred(self.__sin__(), 5)
        return self.__sin0__
    @property 
    def tan(self):
        if self.__tan0__ == None:
            self.__tan0__ = arred(self.__tan__(), 5)
        return self.__tan0__
    @property 
    def cot(self):
        if self.__cot0__ == None:
            self.__cot0__ = arred(self.__cot__(), 5)
        return self.__cot0__
    @property 
    def sec(self):
        if self.__sec0__ == None:
            self.__sec0__ = arred(self.__sec__(), 5)
        return self.__sec0__
    @property 
    def csc(self):
        if self.__csc0__ == None:
            self.__csc0__ = arred(self.__csc__(), 5)
        return self.__csc0__
    @property
    def val(self):
        if self.__val__ == None: 
            self.__val__ = rad(self.__ang__)
        return self.__val__

    def __cos__(self):
        return 1 - (self.val ** 2 / fat(2)) 
    
    def __sin__(self):
        return self.val - (self.val ** 3 / fat(3))
    
    def __tan__(self):
        return self.sin / self.cos 
    
    def __cot__(self):
        return self.cos / self.sin
    
    def __sec__(self):
        return 1 / self.cos 
    
    def __csc__(self):
        return 1 / self.sin

    def __str__(self):
        return str(self.__ang__) + "°"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __float__(self):
        return arred(self.val, 5)

    def __int__(self):
        return self.__ang__

# print(int(deg(10)))
# print(deg(10).val)
# print(str(deg(10)))
# print(frac(1, 2) + 2)           #   3/2
# print(2 + frac(1, 2))           #   3/2
# print(frac(1, 2) - 2)           #  -1/2
# print(2 - frac(1, 2))           #   1/2
# print(frac(1, 2) * 2)           #   1/1
# print(2 * frac(1, 2))           #   1/1
# print(frac(1, 2) / 2)           #   1/4
# print(2 / frac(1, 2))           #   1/4
# print(frac(1, 2) ** 3)          #   1/8
# print(float(3 ** frac(1, 2)))   #   1.7320

deg(10).sin