# Basics (#003)

from typing import List, overload
from _alias import *
# Classes ==================================================

class TheSixOperations():
    def __init__(self, op: Operate) -> None:
        self.o = op
        
    def __call__(self, *Numbers: int | float | List[int | float] ) -> (int | float):
        if (len(Numbers) == 1) and (type(Numbers[0]) is list):
            self.nums = Numbers[0]
        else:
            self.nums = list(Numbers)
        
        if self.o == ("*/" or "**"):
            return self.operate_plus()
        else:
            return self.operate()
    
    def oo(self, x, y):
        match self.o:
            case "+":
                return x + y
            case "-":
                return x - y
            case "*":
                return x * y
            case "/":
                return x / y
    
    def operate(self):
        # Se o primeiro termo da lista for outra lista, essa é resolvida previamente, e jogada em X
        if type(self.nums[0]) is list:
            x = TheSixOperations(self.o)(self.nums[0])
            
        # Se for um numero, o mesmo é jogado em X
        else:
            x = self.nums[0]
        
        # Se inicia um loop de repetição a partir do segundo item da lista
        for i in self.nums[1:]:
            
            # Se o tipo do numero for inteiro ou real, opera ele com X. A operação está em 'self.o'.
            if type(i) is (int or float):
                x = self.oo(x, i)
                
            # Se o tipo do numero for uma lista, se inicia a função atual, porem usando a tal lista como argumento
            elif type(i) is list:
                x = self.oo(x, TheSixOperations(self.o)(i))
        
        # Retorna o valor da operação de todos os números na ordem dada
        return x

    def operate_plus(self):
        match self.o:
            case "**":
                # 'self.nums' é atribuido a '_t'
                _t = self.nums
                
                # se inicia um loop até que só reste 1 numero em '_t'
                while len(_t) != 1:
                    # o termo de '_t' que está na penultima posição, é definido como a potencia do penultimo numero pelo ultimo.
                    _t[_t.index(_t[-2:-1][0])] = _t[-2:-1][0] ** _t[-1:][0]
                    
                    # a lista perde o ultimo numero.
                    _t = _t[:-1]
                    
                # Quando só resta um numero, ele tira o mesmo da lista, e retorna o resultado.
                return _t[0]
            
            case "*/":
                # 'self.nums' é atribuido a '_t'
                _t = self.nums
                
                # se inicia um loop até que só reste 1 numero em '_t'
                while len(_t) != 1:
                    # O primeiro termo de '_t' é elevado ao inverso do segundo termo.
                    _t[0] = _t[0] ** (1 / _t[1])
                    
                    # O segundo termo é eliminado.
                    _t.pop(1)
                
                # Quando só resta um numero, ele tira o mesmo da lista, e retorna o resultado.
                return _t[0]

class Miscellaneos():
    def __init__(self, modo: MiscMode):
        self.mode = modo
    
    @overload
    def __call__(self, *Numbers: Number) -> int: ...
    @overload
    def __call__(self, Number: float, Digits: int) -> int: ...
    @overload
    def __call__(self, Number: float) -> int: ...
    
    def __call__(self, *Numbers: Number):
        if len(Numbers) == 0:
            raise TypeError(
                "No parameters."
            )
        if type(Numbers[0]) is list:
            n = Numbers[0]
        else:
            n = []
            for i in Numbers:
                n.append(i)
        match self.mode:
            case "aparar":
                if (len(n) == 2) and (type(n[0]) is float) and (type(n[1]) is int):
                    x = str(n[0]).split(".")[0]
                    y = str(n[0]).split(".")[1]
                    if len(y) < n[1]:
                        return float(x + '.' + y + ('0' * (len(y) - n[1])))
                    else:
                        return float(x + '.' + y[:n[1]])
                elif type(n[0]) is not float:
                    raise TypeError(
                        f"'N1' receives 'float', and {n[0]} is {n[0].__class__.__name__}."
                    )
                elif len(n) != 2:
                    match len(n):
                        case 1:
                            raise TypeError(
                                "'N2' is empty."
                            )
                        case _:
                            raise TypeError(
                                f"There are only 2 parameters."
                            )
                elif len(n) == 1 or type(n[1]) is not int:
                    raise TypeError(
                        f"'N2' receives 'int', and '{n[1]}' is '{n[1].__class__.__name__}'."
                    )
            case "reduzir":
                if (len(n) == 1) and (type(n[0]) is float):
                    s = str(n[0]).split(".")
                    if s[1] == "0":
                        return int(s[0])
                    else:
                        while s[1][-1:] == '0':
                            s[1] = s[1][:-1]
                        return float('.'.join(s))
                elif type(n[0]) is int:
                    return n[0]
                elif not (type(n[0]) is float):
                    raise TypeError(
                        f"'N' receives 'float', and {n[0]} is {n[0].__class__.__name__}."
                    )
                else:
                    raise TypeError(
                        f"There are only 2 parameters."
                    )
            case "mmc":
                # define o maior valor de 'n' como 'm', e 'x' como o valor do teste(1).
                m, x = max(n), 1                
                
                # Inicia um loop até q o resultado seja encontrado.
                while True:
                    
                    # 'y' recebe a multiplicação do maior numero, pelo valor do teste
                    y = m * x
                    
                    # Inicia um teste por todos os numeros de 'n'.
                    for i in n:
                        
                        # Se o numero(i) não for divisivel pelo número, o loop para.
                        if y % i != 0:
                            break
                    
                    # Se o for não for quebrado, significa que todos os numeros são divisiveis
                    # por y, então ele é o mmc desse conjunto.
                    #     ex-1     |      ex-2     |      ex-3 
                    # mmc ( 3, 7 ) |  mmc ( 3, 6 ) |  mmc ( 7, 2 )     Pode haver mais que 2
                    # ------------ |  ------------ |  ------------     numeros, eu não fiz
                    # y = 6        |  y = 6        |  y = 7            porque ia ocupar muito   
                    # 7%3 = 0 não  |  6%3 = 0 sim  |  7%2 = 0 não      espaço.
                    # 7%7 = 0 sim  |  6%6 = 0 sim  |  7%7 = 0 sim      
                    # ------------ |       |       |  ------------     Note, que o precesso 
                    # y = 14       |       |       |  y = 14           repete varias vezes.
                    # 14%3 = 0 não |       |       |  14%2 = 0 sim     então, em certos casos,
                    # 14%7 = 0 sim |       |       |  14%7 = 0 sim     é melhor não usar.
                    # ------------ |       |       |       |
                    # y = 21       |       |       |       |        
                    # 21%3 = 0     |       |       |       |        
                    # 21%7 = 0 sim |       |       |       |      
                    # ------------ |       V       |       V
                    # mmc = 21...  |  mmc = 6...   |  mmc = 14...                  
                    else:
                        return y
                    
                    # Adiciona um 1 ao valor do teste
                    x += 1
            case "mdc":
                # Define uma função que vai calcular o mdc de dois números.
                def _mdc(x, y):
                    
                    # Inicia um loop até X ser igual a Y.
                    while x != y:
                        
                        # Se X menor que Y, então Y é igual a X - Y, e X é igual a Y.
                        if x > y:
                            y, x = x - y, y
                            
                        # Se não, então Y é igual a Y - X, e X é igual a Y.
                        else:
                            y, x = y - x, y
                    
                    # Retorna quando os valores forem iguais.
                    return x
                
                # Se só haver 2 números, usa a função só nos 2.
                if len(n) == 2:
                    return _mdc(n[0], n[1])
                
                # Se não, roda a função até que só reste 1 número.
                else:
                    n[0] = _mdc(n[0], n[1])
                    n.pop(1)
                    return Miscellaneos("mdc")(n)
                # MDC( 20, 30 )
                # X = -10 |  X = 40  |  X = 10  |  X = 30  |  X = 20  |  X = 10
                # Y = 30  |  Y = 30  |  Y = 30  |  Y = 10  |  Y = 10  |  Y = 10
                # Logo, o MDC é 10...

# Variaveis ==================================================

aparar = Miscellaneos("aparar")
"""---
Aparar
======
---
- Number: Recebe o número decimal que deseja aparar.
- Digits: Recebe um número inteiro com a quantidade de digitos depois do ponto.

>>> INPUT
    print(aparar(10.229, 2))
    
>>> OUTPUT
    10.2"""
reduzir = Miscellaneos("reduzir")
"""---
Reduzir
=======
---
- Numero: Recebe o número decimal e tira os zeros a esquerda.

>>> INPUT
    print(reduzir(10.0))
    
>>> OUTPUT
    10"""
mmc = Miscellaneos("mmc")
"""---
MMC
===
---
- Numbers: Recebe numeros, e retorna o Mínimo Multiplo Comum entre eles.

>>> INPUT
    print(mmc(3, 10, 2))
    
>>> OUTPUT
    30"""
mdc = Miscellaneos("mdc")
"""---
MDC
===
---
- Numbers: Recebe numeros, e retorna o Máximo Divisor Comum entre eles.

>>> INPUT
    print(mdc(20, 16, 40))
    
>>> OUTPUT
    4"""

soma = TheSixOperations("+")
"""---
Soma
====
---
- Numbers: Digite qualquer número real ou inteiro, e retornará soma, pode-se usar couchetes para definir expressões dentro a soma raiz.

>>> INPUT
    print(soma([9, 7], 1, 3, [9, 2], [1, 4, 0], 4))
    print((9 + 7) + 1 + 3 + (9 + 2) + (1 + 4 + 0) + 4))
    
>>> OUTPUT
    40
    40"""
subt = TheSixOperations("-")
"""---
Subt
====
---
- Numbers: Digite qualquer número real ou inteiro, e retornará subtração na ordem, pode-se usar couchetes para definir expressões dentro a soma raiz.

>>> INPUT
    print(subt([9, 7], 1, 3, [9, 2], [1, 4, 0], 4))
    print((9 - 7) - 1 - 3 - (9 - 2) - (1 - 4 - 0) - 4)
    
>>> OUTPUT
    -10
    -10"""
mult = TheSixOperations("*")
"""---
Mult
====
---
- Numbers: Digite qualquer número real ou inteiro, e retornará multiplicação, pode-se usar couchetes para definir expressões dentro a soma raiz.

>>> INPUT
    print(mult([9, 7], 1, 3, [9, 2], [1, 4, 0], 4))
    print((9 * 7) * 1 * 3 * (9 * 2) * (1 * 4 * 1) * 4)
    
>>> OUTPUT
    54432
    54432"""
divs = TheSixOperations("/")
"""---
Divs
====
---
- Numbers: Digite qualquer número real ou inteiro, e retornará divisão na ordem, pode-se usar couchetes para definir expressões dentro a soma raiz.

>>> INPUT
    print(divs([9, 7], 1, 3, [9, 2], [1, 4, 0], 4))
    print((9 / 7) / 1 / 3 / (9 / 2) / (1 / 4 / 1) / 4)
    
>>> OUTPUT
    0.09523809523809525
    0.09523809523809525"""
potc = TheSixOperations("**")
"""---
Potc
====
---
- Numbers: Digite qualquer número real ou inteiro, e retornará a potencia de uma logica não sequencial.

>>> Seguindo a logica:
    w ^ (x ^ (y ^ z)) = potc(w, x, y, z)
    = = = = = = = =
    #       z
    #     y
    #   x
    # w       =>   potc(w, x, y, z)
    = = = = = = = =
    considera essa lógica ao usar
.
>>> INPUT
    print(potc(3, 2, 2))
    print(3 ** (2 ** 2))
    
>>> OUTPUT
    81
    81"""
raiz = TheSixOperations("*/")
"""---
Raiz
====
---
- Numbers: Digite qualquer número real ou inteiro, e retornará a raiz de uma logica sequencial.

O primeiro numero é a base, e os outros são os indices da raiz aninhada.

>>> Seguindo a logica:
    = = = = = = = =
    #    z _________
    #     /  y ______
    #    /    /  x ___
    # ´\/  ´\/  ´\/ w  => raiz(w, x, y, z)
    = = = = = = = =
    considera essa lógica ao usar
.
>>> INPUT
    print(raiz(3, 2, 2))
    print((3 ** (1/2)) ** (1/2))
    
>>> OUTPUT
    1.3160740129524924
    1.3160740129524924"""
