"""
Arquivo de estudo
Listas, Pilhas, Filas e Deques em Python

Estruturas:
1) Lista (List)
2) Pilha (Stack - LIFO)
3) Fila (Queue - FIFO)
4) Deque (Double-ended queue)

Legenda:
- O(1): tempo constante
- O(n): tempo linear
"""

# ======================================================
# 1. LISTA (LIST)
# ======================================================

# Ideia:
# Estrutura dinâmica, indexada, permite tipos mistos
# Implementada como array dinâmico (redimensionável)

lista = [10, 20, 30]
print("Lista inicial:", lista)

# ---------- OPERAÇÕES ----------

# Inserções
lista.append(40)        # O(1) amortizado
lista.insert(1, 15)     # O(n)
print("Após inserções:", lista)

# Remoções
lista.remove(20)        # O(n)
ultimo = lista.pop()    # O(1)
print("Após remoções:", lista)
print("Removido com pop:", ultimo)

# Acesso
print("Primeiro:", lista[0])     # O(1)
print("Último:", lista[-1])      # O(1)

# Percurso
for i, v in enumerate(lista):
    print(f"Index {i} -> {v}")

# Observação importante:
# Inserir/remover no meio desloca elementos → custo O(n)

# ======================================================
# 2. PILHA (STACK - LIFO)
# ======================================================

# LIFO = Last In, First Out
# Exemplo real: desfazer (Ctrl+Z)

pilha = []

# Push (empilhar)
pilha.append(10)
pilha.append(20)
pilha.append(30)
print("\nPilha:", pilha)

# Pop (desempilhar)
print("Saiu:", pilha.pop())
print("Após pop:", pilha)

# Topo (peek)
print("Topo:", pilha[-1])

# Complexidade:
# push: O(1)
# pop: O(1)

# ---------- IMPLEMENTAÇÃO ----------

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack vazia")
        return self.items.pop()

    def peek(self):
        return None if self.is_empty() else self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)

# Exemplo
s = Stack()
s.push(1); s.push(2); s.push(3)
s.display()
print("Pop:", s.pop())
s.display()

# ======================================================
# 3. FILA (QUEUE - FIFO)
# ======================================================

# FIFO = First In, First Out
# Exemplo real: fila de banco

from collections import deque

fila = deque()

# Enqueue
fila.append(10)
fila.append(20)
fila.append(30)
print("\nFila:", fila)

# Dequeue
print("Saiu:", fila.popleft())
print("Após dequeue:", fila)

# Primeiro elemento
print("Primeiro:", fila[0])

# Complexidade com deque:
# enqueue: O(1)
# dequeue: O(1)

# ---------- IMPLEMENTAÇÃO (INEFICIENTE COM LIST) ----------

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)      # O(1)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Fila vazia")
        return self.items.pop(0)      # O(n) ⚠️

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)

q = Queue()
q.enqueue(1); q.enqueue(2); q.enqueue(3)
q.display()
print("Dequeue:", q.dequeue())
q.display()

# IMPORTANTE:
# Em prova: fale que lista não é ideal para fila por causa do pop(0)

# ======================================================
# 4. DEQUE
# ======================================================

# Double-ended queue (duas pontas)
# Permite inserir/remover dos dois lados em O(1)

from collections import deque

d = deque()

# Inserções
d.append(10)        # direita
d.appendleft(5)     # esquerda
print("\nDeque:", d)

# Remoções
print("Remove direita:", d.pop())
print("Remove esquerda:", d.popleft())

# Casos de uso:
# - fila eficiente
# - pilha eficiente
# - sliding window

# ======================================================
# 5. COMPARAÇÃO
# ======================================================

"""
Estrutura | Inserir | Remover | Acesso | Observação
--------------------------------------------------
Lista     | O(n)    | O(n)    | O(1)   | boa geral
Pilha     | O(1)    | O(1)    | O(1)   | LIFO
Fila      | O(1)    | O(1)*   | O(1)   | FIFO (*com deque)
Deque     | O(1)    | O(1)    | O(1)   | mais flexível
"""

# ======================================================
# 6. EXERCÍCIOS IMPORTANTES
# ======================================================

# 1. Inverter string (pilha)

def inverter_string(txt):
    s = []
    for c in txt:
        s.append(c)

    res = ''
    while s:
        res += s.pop()

    return res

print("\nInverter 'estrutura':", inverter_string("estrutura"))

# 2. Palíndromo (deque)

def eh_palindromo(txt):
    d = deque(txt)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

print("'arara'?", eh_palindromo("arara"))

# 3. Simulação fila

def simular():
    f = deque(["A", "B", "C"])
    while f:
        print("Atendendo:", f.popleft())

simular()

# 4. Balanceamento de parênteses (pilha)

def balanceado(expr):
    s = []
    pares = {')':'(', ']':'[', '}':'{'}

    for c in expr:
        if c in '([{':
            s.append(c)
        elif c in ')]}':
            if not s or s.pop() != pares[c]:
                return False

    return len(s) == 0

print("Balanceado?", balanceado("(a+b)*[c-d]"))

# ======================================================
# 7. RESUMO FINAL (PROVA)
# ======================================================

"""
- Lista: estrutura base (array dinâmico)
- Pilha: LIFO (append/pop)
- Fila: FIFO (deque)
- Deque: melhor geral para inserções nas pontas

DICA DE PROVA:
Se falar de desempenho → use deque para fila
Se falar de recursão/desfazer → pilha
"""

print("\nArquivo FINALIZADO - versão avançada")
