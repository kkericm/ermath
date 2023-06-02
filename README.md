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
print(y)            # retorna 45
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
print(x)              # retorna 1.12
```

As funções do `Miscellaneos` é como as do `TheSixOperations`, que recebem os valores das funções nas chamadas.

- `aparar()`: Diminui um número decimal para um tamanho expecificado
  - `Number`: O número decimal que deseja aparar.
  - `Digits`: Quantidade de digitos depois do ponto.
```py
from ermath import aparar

aparar(10.22392, 3)   # Retorna 10.123
```
- `reduzir()`: Caso haja um 0 depois do ponto, a função retira, se só haver 0 ele transforma em `int`.
  - `Number`: O número decimal
```py
from ermath import reduzir

reduzir(10.0)         # Retorna 10
```
- `mmc()`: Recebe numeros, e tira o MMC deles.
  - `Numbers`: Recebe os números para tirar o MMC.
```py
from ermath import mmc

mmc(20, 30, 10)       # Retorna 60
```
- `mdc()`: Recebe numeros, e tira o MDC deles.
  - `Numbers`: Recebe os números para tirar o MDC.
```py
from ermath import mdc

mdc(20, 30, 10)       # Retorna 10
```
- `arred()`: Recebe um número para arredondar.
  - `Number`: Recebe o número que deseja arredondar.
  - `Digits`: Recebe a quantidade de digitos depois da vírgula.
```py
from ermath import arred

arred(10.22392, 3)    # Retorna 10.224
```
- `fat()`: Recebe um número, e retorna o fatorial(!) desse número.
```py
from ermath import fat

fat(5)     # Retorna 120
```
---

## Fração

A classe `frac` é a responsavel por construir a fração.
Ela recebe dois ou um argumento, se tiver dois números, o primeiro é o numerador, e o segundo é o denominador. Se for a string de uma fração (Dois números divididos por uma barra), o numero a direita da barra é o numerador e o a esquerda o denominador. Se for só um número, e o número for decimal, ele transforma esse em fração. Por fim, se só haver um número inteiro, retorna o número sobre 1.
Ex:
```py
frac(1, 2)           # retorna 1/2
frac("1/3")          # retorna 1/3
frac(0.25)           # retorna 1/4
frac(2)              # retorna 2/1
```
As frações são tratadas como números, então é possivel operar com ela.
```py
frac(10,  4) + 12    # retorna 11/2
```
Note que ele sempre simplifica a fração ao máximo.
```py
int(frac(10,  3))    # retorna 3
float(frac(10,  3))  # retorna 3.333
str(frac(10,  3))    # retorna "10/3"
```
---
## Ângulo:

A classe `drag` é a responsavel por construir o ângulo.
Constroi um ângulo, se você solicitar a priedade `val`, é retornado o valor radiano.
Ex:
```py
drag(10)           # retorna 10°
drag(10).val       # retorna 0.17453
```
Você pode converter os valores tambêm, e terá esses resultados:
```py
int(drag(10))      # retorna 10
float(drag(10))    # retorna 0.17453
str(drag(10))      # retorna 10°
```
---

A classe `rad` faz a conversão em radiano.
```py
rad(10)            # retorna 0.17453rad
```
---
A classe `drag` tem as propriedades `cos`, `sin`, `tan`, `cot`, `sec`, `csc`, que retornam repectivamente o Cosseno, Seno, Tangente, Cotangente, Secante, Cossecante.

Saiba que o valor dessas propriedades é aproximado, porem e proximo o bastante para diferença ser despressivel. Por exemplo, ele diz seno de 90° é 0.92483, porém ele é 1.

---