# ErMath
ErMath, um modulo matemático meu

---

## As 6 operações:

A classe `TheSixOperations` é a responsavel por fazer as 6 operações basicas (+, -, *, /, **, raiz quadrada)
Ex:
```py
from ermath import TheSixOperations
x = TheSixOperations("+")(19, 10)
print(x) # retorna 29
```

A classe é construida apenas com a operação que ela fará, e os numeros que irá operar nas chamadas.

---
As chamadas recebem quantos numeros desejar, incluindo listas, que seram resolvidas antes de operar com os numeros fora dela.
Ex:
```py
from ermath import TheSixOperations
somar = TheSixOperations("+")
y = somar(10, 2, [10, 12, [10, 1]])
print(y) # retorna 45
```

Existem as variaveis `soma`, `subt`, `mult`, `divs`, `raiz`, `potc`, que 
resolvem respectivamente Adição, Subtração, Multiplicação, Divisão, Radiciação
e Potenciacão. Você pode chamar essas variaveis com classes já construidas.

---
As funções `raiz` e `potc` tem sua

Logica da potencia:
```py
w ^ (x ^ (y ^ z)) = potc(w, x, y, z)
```
```
      z
    y
  x
w       =>   potc(w, x, y, z)
```

Logica da radiciação:
```
     _____________
    /    ________
 z /  y /  x ___
´\/  ´\/  ´\/ w   => raiz(w, x, y, z)
```

---

As tirando as funções `raiz` e `potc` as funções costumam seguir uma logica similar as operações comuns do python.
Ex:
```py
soma(2, 3, 4, 5)    # retorna 14
2 + 3 + 4 + 5       # retorna 14
```

---

## Diversos:
A classe `Miscellaneos` é a responsavel por construir diversas funções.
Ex:
```py
from ermath import TheSixOperations
x = Miscellaneos("aparar")( 1.123, 2 )
print(x) # retorna 1.12
```

As funções do `Miscellaneos` é como as do `TheSixOperations`, que recebem os valores das funções nas chamadas.

- `aparar()`: Diminui um número decimal para um tamanho expecificado
  - `Number`: O número decimal que deseja aparar.
  - `Digits`: Quantidade de digitos depois do ponto.
- `reduzir()`: Caso haja um 0 depois do ponto, a função retira, se só haver 0 ele transforma em `int`.
  - `Number`: O número decimal
- `mmc()`: Recebe numeros, e tira o MMC deles.
  - `Numbers`: Recebe os números para tirar o MMC.
- `mdc()`: Recebe numeros, e tira o MDC deles.
  - `Numbers`: Recebe os números para tirar o MDC.
- `arred()`: Recebe um número para arredondar, e a quantidade de digitos finais depois da vírgula.
  - `Number`: Recebe o número que deseja arredondar.
  - `Digits`: Recebe a quantidade de digitos depois da vírgula.
- `fat()`: Recebe um número, e retorna o fatorial(!) desse número.

---
