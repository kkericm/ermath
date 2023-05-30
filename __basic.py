from typing import List

class TheSixOperations():
    def __init__(self, op) -> None:
        self.o = op
        
    def __call__(self, *Numbers: int | float | List[int | float] ) -> (int | float):
        if (len(Numbers) == 1) and (type(Numbers[0]) is list):
            self.nums = Numbers[0]
        else:
            self.nums = list(Numbers)
            
        match self.o:
            case "+":
                
                # Define uma Variavel de controle, nela a soma fica armazenada
                x = 0
                
                # Se inicia um loop por todos os numero da lista
                for i in self.nums:
                    
                    # Se o tipo do numero for inteiro ou real, soma ele a X
                    if type(i) is (int or float):
                        x += i
                        
                    # Se o tipo do numero for uma lista, se inicia a função atual, porem usando a tal lista como argumento
                    elif type(i) is list:
                        x += TheSixOperations("+")(i)
                
                # Retorna o valor da soma de todos os números
                return x
            
            case "-":
                
                # Se o primeiro termo da lista for outra lista, essa é resolvida previamente, e jogada em X
                if type(self.nums[0]) is list:
                    x = TheSixOperations("-")(self.nums[0])
                    
                # Se for um numero, o mesmo é jogado em X
                else:
                    x = self.nums[0]
                
                # Se inicia um loop de repetição a partir do segundo item da lista
                for i in self.nums[1:]:
                    
                    # Se o tipo do numero for inteiro ou real, soma ele a X
                    if type(i) is (int or float):
                        x -= i
                        
                    # Se o tipo do numero for uma lista, se inicia a função atual, porem usando a tal lista como argumento
                    elif type(i) is list:
                        x -= TheSixOperations("-")(i)
                
                # Retorna o valor da subtração de todos os números na ordem dada
                return x
            
            case "*":
                
                # Define uma Variavel de controle, nela a soma fica armazenada
                x = 1
                
                # Se inicia um loop por todos os numero da lista
                for i in self.nums:
                    
                    # Se o tipo do numero for inteiro ou real, soma ele a X
                    if type(i) is (int or float):
                        x *= i

                    # Se o tipo do numero for uma lista, se inicia a função atual, porem usando a tal lista como     
                    elif type(i) is list:
                        x *= TheSixOperations("*")(i)

                # Retorna o valor da soma de todos os números        
                return x
            
            case "/":
                
                # Se o primeiro termo da lista for outra lista, essa é resolvida previamente, e jogada em X
                if type(self.nums[0]) is list:
                    x = TheSixOperations("/")(self.nums[0])
                    
                # Se for um numero, o mesmo é jogado em X
                else:
                    x = self.nums[0]
                    
                # Se inicia um loop de repetição a partir do segundo item da lista
                for i in self.nums[1:]:
                    
                    # Se o tipo do numero for inteiro ou real, soma ele a X
                    if type(i) is (int or float):
                        x /= i
                        
                    # Se o tipo do numero for uma lista, se inicia a função atual, porem usando a tal lista como  argumento   
                    elif type(i) is list:
                        x /= TheSixOperations("/")(i)
                        
                # Retorna o valor da subtração de todos os números na ordem dada        
                return x

            case "**":
                _t = self.nums
                while len(_t) != 1:
                    _t[_t.index(_t[-2:-1][0])] = _t[-2:-1][0] ** _t[-1:][0]
                    _t = _t[:-1]
                return _t[0]
            
            case "*/":
                _t = self.nums
                while len(_t) != 1:
                    _t[0] = _t[0] ** (1 / _t[1])
                    _t.pop(1)
                return _t[0]
                
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
