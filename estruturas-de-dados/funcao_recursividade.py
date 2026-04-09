"""
===========================================
FUNÇÕES E RECURSIVIDADE EM PYTHON
===========================================

Este arquivo contém:
✔ Explicações teóricas (em comentários)
✔ Exemplos práticos
✔ Comparações (iterativo vs recursivo)
✔ Tipos de recursão
✔ Exercícios implementados

-------------------------------------------
1. O QUE É UMA FUNÇÃO?
-------------------------------------------
Uma função é um bloco de código reutilizável que executa uma tarefa específica.

Estrutura básica:
def nome_funcao(parametros):
    instruções
    return resultado
"""

# Exemplo simples de função
def soma(a, b):
    return a + b


"""
-------------------------------------------
2. O QUE É RECURSIVIDADE?
-------------------------------------------
Recursividade acontece quando uma função chama a si mesma.

Segundo o material:
"Um procedimento recursivo faz referência a si próprio."

IMPORTANTE:
Toda função recursiva precisa de:
1. Caso base (condição de parada)
2. Caso recursivo (chamada da própria função)

Sem isso → LOOP INFINITO (ou stack overflow)
"""

# Exemplo clássico: fatorial

"""
Definição matemática:
n! = 1              se n = 0   (caso base)
n! = n * (n-1)!     se n > 0   (caso recursivo)
"""

def fatorial_recursivo(n):
    # CASO BASE
    if n == 0:
        return 1
    
    # CASO RECURSIVO
    return n * fatorial_recursivo(n - 1)


"""
-------------------------------------------
3. COMPARAÇÃO: ITERATIVO vs RECURSIVO
-------------------------------------------
"""

def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


"""
-------------------------------------------
4. AS 3 LEIS DA RECURSÃO (DO PDF)
-------------------------------------------
1. Deve ter caso base
2. Deve se aproximar do caso base
3. Deve chamar a si mesma

Exemplo acima respeita todas ✔
"""


"""
-------------------------------------------
5. COMO A RECURSÃO FUNCIONA (PILHA)
-------------------------------------------
Cada chamada é guardada na memória (pilha).

Exemplo: fatorial(3)

f(3)
 -> f(2)
   -> f(1)
     -> f(0)
       -> retorna 1

Depois "desempilha":
f(1) = 1*1
f(2) = 2*1
f(3) = 3*2 = 6
"""


"""
-------------------------------------------
6. TIPOS DE RECURSÃO
-------------------------------------------
"""

# ---------------------------
# 6.1 RECURSÃO LINEAR
# (uma chamada por vez)
# ---------------------------

def soma_n(n):
    if n == 0:
        return 0
    return n + soma_n(n - 1)


# ---------------------------
# 6.2 RECURSÃO BINÁRIA
# (duas chamadas)
# Ex: Fibonacci
# ---------------------------

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)


# ---------------------------
# 6.3 RECURSÃO MÚLTIPLA
# (várias chamadas)
# ---------------------------

def exemplo_multiplo(n):
    if n <= 0:
        return 1
    
    return (
        exemplo_multiplo(n - 1) +
        exemplo_multiplo(n - 2) +
        exemplo_multiplo(n - 3)
    )


# ---------------------------
# 6.4 RECURSÃO INDIRETA
# (uma função chama outra)
# ---------------------------

def par(n):
    if n == 0:
        return True
    return impar(n - 1)

def impar(n):
    if n == 0:
        return False
    return par(n - 1)


"""
-------------------------------------------
7. EXEMPLO IMPORTANTE: MDC (Máximo Divisor Comum)
-------------------------------------------
Baseado no PDF
"""

def mdc(x, y):
    if x == y:
        return x
    elif x > y:
        return mdc(x - y, y)
    else:
        return mdc(y, x)


"""
-------------------------------------------
8. RECURSÃO COM CAUDA (TAIL RECURSION)
-------------------------------------------
O objetivo é evitar uso excessivo de memória.

Passamos o resultado acumulado como parâmetro.
"""

def fatorial_cauda(n, acumulador=1):
    if n == 0:
        return acumulador
    
    return fatorial_cauda(n - 1, acumulador * n)


"""
-------------------------------------------
9. PROBLEMAS CLÁSSICOS (DO PDF)
-------------------------------------------
"""

# Contar zeros em um número
def contar_zeros(n):
    if n < 10:
        return 1 if n == 0 else 0
    
    ultimo = n % 10
    
    if ultimo == 0:
        return 1 + contar_zeros(n // 10)
    else:
        return contar_zeros(n // 10)


# Soma dos dígitos
def soma_digitos(n):
    if n < 10:
        return n
    
    return (n % 10) + soma_digitos(n // 10)


# Potência recursiva
def potencia(b, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / potencia(b, -n)
    else:
        return b * potencia(b, n - 1)


"""
-------------------------------------------
10. VANTAGENS E DESVANTAGENS
-------------------------------------------

VANTAGENS:
✔ Código mais simples
✔ Elegante
✔ Natural para problemas matemáticos

DESVANTAGENS:
✖ Mais lento
✖ Usa mais memória (pilha)
✖ Pode dar stack overflow

-------------------------------------------
11. QUANDO USAR RECURSÃO?
-------------------------------------------

Use quando:
✔ O problema é naturalmente recursivo
✔ Estrutura de árvore (ex: Fibonacci)
✔ Divisão de problemas (divide and conquer)

Evite quando:
✖ Pode ser resolvido facilmente com loop
✖ Performance é crítica
"""


"""
-------------------------------------------
12. TESTES
-------------------------------------------
"""

if __name__ == "__main__":
    print("Fatorial recursivo:", fatorial_recursivo(5))
    print("Fatorial iterativo:", fatorial_iterativo(5))
    print("Fibonacci:", fibonacci(6))
    print("MDC:", mdc(6, 3))
    print("Par(4):", par(4))
    print("Zeros em 10101:", contar_zeros(10101))
    print("Soma dos dígitos:", soma_digitos(1234))
    print("Potência:", potencia(2, 3))