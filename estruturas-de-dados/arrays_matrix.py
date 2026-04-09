"""
Arquivo de estudo: Arrays e Matrizes em Python

Este arquivo contém:
- Explicações em comentários
- Exemplos práticos
- Funções úteis
- Exercícios resolvidos
"""

# ======================================================
# 1. INTRODUÇÃO A ARRAYS
# ======================================================

# Em Python, usamos principalmente LISTAS como arrays dinâmicos
# Também existe o módulo 'array' para arrays mais eficientes

from array import array

# Exemplo de array (tipo inteiro)
arr = array('i', [10, 20, 30, 40])
print("Array inicial:", arr)

# ======================================================
# 2. ACESSO A ELEMENTOS
# ======================================================

print("Primeiro elemento:", arr[0])
print("Último elemento:", arr[-1])

# ======================================================
# 3. INSERÇÃO DE ELEMENTOS
# ======================================================

# insert(posição, valor)
arr.insert(1, 15)
print("Após insert:", arr)

# append(valor)
arr.append(50)
print("Após append:", arr)

# ======================================================
# 4. REMOÇÃO DE ELEMENTOS
# ======================================================

# pop(index)
arr.pop(2)
print("Após pop(2):", arr)

# remove(valor)
arr.remove(15)
print("Após remove(15):", arr)

# ======================================================
# 5. PERCORRENDO UM ARRAY
# ======================================================

print("Percorrendo array:")
for elemento in arr:
    print(elemento)

print("Percorrendo com índice:")
for i in range(len(arr)):
    print(f"Índice {i}: {arr[i]}")

# ======================================================
# 6. OPERAÇÕES IMPORTANTES
# ======================================================

print("Tamanho do array:", len(arr))
print("Maior valor:", max(arr))
print("Menor valor:", min(arr))
print("Soma:", sum(arr))

# ======================================================
# 7. REVERSO
# ======================================================

# Forma 1
print("Reverso com slicing:", arr[::-1])

# Forma 2 (altera o original)
arr.reverse()
print("Array invertido:", arr)

# ======================================================
# 8. MATRIZES (ARRAY 2D COM LISTAS)
# ======================================================

# Python não suporta array 2D nativo com 'array', usamos listas

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz:")
for linha in matriz:
    print(linha)

# Acessando elemento
print("Elemento [1][2]:", matriz[1][2])

# ======================================================
# 9. FUNÇÕES IMPORTANTES (EXERCÍCIOS)
# ======================================================

# 1. Reverso
def inverter_array(arr):
    return arr[::-1]

# 2. Maior elemento
def maior_elemento(arr):
    return max(arr)

# 3. Menor elemento
def menor_elemento(arr):
    return min(arr)

# 4. Soma dos elementos
def soma_elementos(arr):
    return sum(arr)

# Testando funções
lista = [5, 2, 9, 1, 7]
print("\nLista:", lista)
print("Reverso:", inverter_array(lista))
print("Maior:", maior_elemento(lista))
print("Menor:", menor_elemento(lista))
print("Soma:", soma_elementos(lista))

# ======================================================
# 10. DESAFIOS EXTRAS
# ======================================================

# Buscar elemento

def buscar_elemento(arr, valor):
    if valor in arr:
        return arr.index(valor)
    return -1

print("Buscar 9:", buscar_elemento(lista, 9))

# Inserir manualmente (simulando deslocamento)

def inserir_manual(arr, index, valor):
    return arr[:index] + [valor] + arr[index:]

print("Inserção manual:", inserir_manual(lista, 2, 99))

# Remover manualmente

def remover_manual(arr, index):
    return arr[:index] + arr[index+1:]

print("Remoção manual:", remover_manual(lista, 2))

# ======================================================
# FIM
# ======================================================

print("\nArquivo de estudo concluído!")
