"""
Arquivo de estudo: Alocação Dinâmica de Memória (Listas Encadeadas)

Conteúdo:
- Explicação completa
- Implementação passo a passo
- Métodos clássicos
- Exemplos
"""

# ======================================================
# 1. INTRODUÇÃO
# ======================================================

# Diferente dos arrays (memória contígua),
# listas encadeadas usam nós ligados por ponteiros.

# Cada nó possui:
# - valor
# - referência para o próximo nó

# ======================================================
# 2. CLASSE NODE
# ======================================================

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"

# ======================================================
# 3. CLASSE LINKED LIST
# ======================================================

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # ==========================
    # Inserir no início
    # ==========================
    def insert_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # ==========================
    # Inserir no final
    # ==========================
    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        self.size += 1

    # ==========================
    # Inserir após um valor
    # ==========================
    def insert_after(self, target, value):
        current = self.head

        while current:
            if current.value == target:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                self.size += 1
                return
            current = current.next

    # ==========================
    # Remover primeiro
    # ==========================
    def remove_first(self):
        if self.head:
            self.head = self.head.next
            self.size -= 1

    # ==========================
    # Remover por valor
    # ==========================
    def remove(self, value):
        current = self.head
        previous = None

        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

    # ==========================
    # Reverter lista
    # ==========================
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # ==========================
    # Mostrar lista
    # ==========================
    def display(self):
        current = self.head
        elements = []

        while current:
            elements.append(current.value)
            current = current.next

        print(elements)

# ======================================================
# 4. EXEMPLOS DE USO
# ======================================================

ll = LinkedList()

ll.insert_first(10)
ll.insert_first(5)
ll.append(20)
ll.append(30)

print("Lista inicial:")
ll.display()

ll.insert_after(20, 25)
print("Após inserir 25 depois de 20:")
ll.display()

ll.remove(5)
print("Após remover 5:")
ll.display()

ll.remove_first()
print("Após remover primeiro:")
ll.display()

ll.reverse()
print("Lista invertida:")
ll.display()

# ======================================================
# 5. DESAFIOS
# ======================================================

# Buscar elemento

def buscar(ll, value):
    current = ll.head
    index = 0

    while current:
        if current.value == value:
            return index
        current = current.next
        index += 1

    return -1

print("Buscar 25:", buscar(ll, 25))

# Contar elementos manualmente

def contar(ll):
    count = 0
    current = ll.head

    while current:
        count += 1
        current = current.next

    return count

print("Tamanho calculado:", contar(ll))

# ======================================================
# FIM
# ======================================================

print("\nEstudo de lista encadeada concluído!")
