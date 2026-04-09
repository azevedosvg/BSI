# Author: Luiz Thadeu Grizendi
# UniAcademia - Juiz de Fora
# Minas Gerais - Brasil
from array import *

class Array:
    """Implementa um Array com alocação estática *."""
    """    TYPECODE
            'b'	signed char	int	1
            'B'	unsigned char	int	1
            'u' Py_UNICODE           character unicod     2
            'h'	signed short	int	2
            'H'	unsigned short	int	2
            'i'	signed                       int	2 (size varies by platform)
            'I'	unsigned int	int	2 (size varies by platform)
            'l'	signed long	int	4
            'L'	unsigned long	int	4
            'q'	signed long long	int	8
            'Q'	unsigned long long	int	8
            'f'	float	                 float	4
            'd' double                      float	4
    """
    TYPE_MAP = {
            'b': int,
            'B': int,
            'u': str,
            'h': int,
            'H': int,
            'i':   int,
            'I': int,
            'l': int,
            'L': int,
            'q': int,
            'Q': int,
            'f': float,
            'd': float
    }
    def __init__(self, typecode, initialize=None):
        if typecode not in self.TYPE_MAP:
            raise ValueError(': bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)')
        self.typecode = typecode
        self.dtype = self.TYPE_MAP[typecode]
        self._data = []  # Inicializa como uma lista linear
        if initialize is not None:
            for item in initialize:
                self.append(item)
                
    def _check_type(self, value):
        """Verifica se o valor respeita o typecode."""
        if not isinstance(value, self.dtype):
            raise TypeError(
                f"'{type(value).__name__}' object cannot be interpreted as an {self.dtype.__name__}"
            )
        
    def _check_index(self, index):
        if index < 0:
             index+= len(self)
        if index < 0 or index >= len(self):
            raise IndexError(" array index out of range")
        return index
   
    def append(self, value):
        self._check_type(value)
        self._data.append(value) # aloca mais uma célula

    def insert(self, index, value):
        self._check_type(value)
        if index < 0:
             index+= len(self)
        if index < 0:
             index=0
        if index >= len(self):
             index=len(self)
        self._data.append(value) # aloca mais uma célula
        # deslocamento para a direita
        for i in range(len(self._data)-1, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value

    def pop(self, index=-1):
        if len(self._data)==0:
            raise IndexError("pop from empty array")      
        index=self._check_index(index)
        value = self._data[index]
        # deslocamento para a esquerda
        for i in range(index, len(self._data) - 1):
            self._data[i] = self._data[i + 1]
        self._data.pop(-1) # libera a última célula
        return value

    def remove(self,v):
        index = 0 
        for i in range(index, len(self)):
            if self._data[i] == v:
                break
            index+=1
        if index >= len(self):
            raise ValueError(': array.remove(x): x not in array')
        for i in range(index, len(self) - 1):
            self._data[i] = self._data[i + 1]
        self._data.pop(-1) # libera a última célula
        return v

    def reverse(self):
        """Inverte o array in-place."""
        left = 0
        right = len(self) - 1
        while left < right:
            # troca os elementos
            self._data[left], self._data[right] = self._data[right],self._data[left]
            left += 1
            right -= 1

    """native python functions""" 
    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        for i in range(len(self._data)):
            yield self._data[i]
    
    def __repr__(self):
         return repr(str(self))
     
    def __str__(self):
         return "Array('"+str(self.typecode)+"',"+str(self._data)+")"

    def index(self, value, start=0, stop=9223372936854775807):
         """Return first index of value."""
         index = 0
         if index < start:
              index = start
         if stop > len(self):
             stop = len(self)
         while index < stop:
              if self._data[index] == value:
                   return index
              index += 1
         raise ValueError(': array.index(x): x not in array')

    def __contains__(self,key):
              for item in self:
                  if item == key:
                      return True
              return False
            
class stack:                                                                                                                                       
     def __init__(self,iterable=None):
         self.__items = []
         if iterable:
              for item in iterable:
                   self.push(item)
                   
     def push(self, item):
         self.__items.append(item)

     def pop(self):
         if len(self) == 0:
              raise IndexError('pop from empty stack')
         return self.__items.pop()
         #return self.__items.pop(-1)
         #return self.__items.pop(len(self)-1)
     
     def peek(self):
         if len(self) == 0:
              raise IndexError('peek/top from empty stack')
         return self.__items[-1]
         #return self.__items[len(self)-1]

     def top(self):
         """the same as peek"""
         return self.peek()

     def clear(self):
         self.__init__()
         #self.__items = []
         
     def isEmpty(self):
         return len(self) == 0

     def extend(self,iterable):
         for element in iterable:
              self.push(element)              

     def copy(self):        
          """ returns a copy of the Collection"""
          #return self.__class__(reversed([element for element in self]))
          return stack(reversed([element for element in self]))
     
     """native python functions"""
     def __contains__(self,key):
        return key in self.__items

     def __str__(self):
        return '['+', '.join([str(item) for item in self]) +']'

     def __repr__(self):
        return 'stack ->'+str(self)

     def __eq__(self, iterable):
        "Test self == iterable"
        return list(self) == list(iterable)

     def __len__(self):
        return len(self.__items)

     def __iter__(self):
          self.__current = len(self)-1
          return self          

     def __next__(self):
          if self.__current < 0:
               raise StopIteration
          else:
               self.__current -= 1
               return self.__items[self.__current + 1]     

class queue:
     def __init__(self,iterable=None):
         self.__items = []
         if iterable:
              for item in iterable:
                   self.enqueue(item)

     def clear(self):
          self.__init__()
          ##self.__items = []
         
     def copy(self):        
          """ returns a copy of the Collection"""
          return self.__class__([element for element in self])
     
     def isEmpty(self):
          return len(self) == 0

     def enqueue(self, item): 
          self.__items.append(item)
          
     def offer(self, item):  
          """the same as enqueue"""
          self.enqueue(item)
	  
     def dequeue(self):  
          if len(self) == 0:
              raise IndexError('dequeue/poll from empty queue')
          return self.__items.pop(0)
     
     def poll(self):
          """the same as dequeue"""
          return self.dequeue()

     def peek(self):  
          if len(self) == 0:
              raise IndexError('peek/front from empty queue')
          return self.__items[0]

     def front(self):
          """the same as peek"""
          return self.peek()
     
     def extend(self,iterable):
          for element in iterable:
               self.enqueue(element)
               
     """native python functions"""
     def __contains__(self,key):
          return key in self.__items
     
     def __len__(self):
          return len(self.__items)

     def __str__(self):
          return str(self.__items) 
 
     def __repr__(self):
          return 'Queue->'+repr(self.__items)

     def __iter__(self):
          self.__current = 0
          return self          

     def __next__(self):
          if self.__current >=len(self):
               raise StopIteration
          else:
               self.__current += 1
               return self.__items[self.__current - 1]     

     def __eq__(self, iterable):
        "Test self==iterable"
        return list(self) == list(iterable)

class Node(object):
     """Represents a singly linked node."""
     def __init__(self, value, next = None):
          """Instantiates a Node with a default next of None."""
          self.value = value
          self.next = next
          
     """native python functions"""
     def __str__(self):
          return str(self.value)

     def __repr__(self):
          return str(self)+"\u2192"+str(self.next)
     
class abstractList(object):
     def __init__(self):
          """Instantiates a linked list with a default
             head of None and size zeroe"""
          self._size = 0
          self._head = None
          
     """native python functions"""
     def __str__(self):
          """ The string representation of the linkedList"""
          return str([e for e in self])

     def __len__(self):
          """ Length of the list"""
          return self._size

     def __repr__(self):
          """ The representation of the linkedList"""
          return "{0} {1}".format(self.__class__.__name__, self)
     
     def __iter__(self):
            """ Supports traversal with a for loop"""
            current = self._head
            while current is not None:
                yield current.value
                current = current.next
  
class linkedList(abstractList):
     """Represents a singly linked list."""
     def __init__(self,iterable=None):
          """Instantiates a linked list with a default
             head of None and size zeroe"""
          super().__init__()
          if iterable:
               for value in iterable:
                    self.append(value)

     def index(self, value, start=0, stop=9223372936854775807):
         """Return first index of value."""
         currNode = self._head
         # search current and prev node for k equal i
         index = 0
         while currNode:
              if index < start:
                   index += 1
                   currNode = currNode.next
                   continue
              if currNode.value == value:
                   return index
              currNode = currNode.next
              index += 1
              if index == stop:
                   break
         raise IndexError('index(x): x not in '+str(self.__class__.__name__))
     
     def clear(self):
          """ clear data"""
          self.__init__()

     def _insert_First(self, object):
          self._head = Node(object, self._head)

     def _insert_After(self, object, current):
          current.next = Node(object, current.next)

     def _insert_Before(self, object, previous):
          previous.next = Node(object, previous.next)
          
     def insert(self, index, object):
          """add object in to position index"""
          if index < 0:
               index+=len(self)         
          if self._head is None or index <= 0: # insert unique/first
               self._insert_First(object)
          else:
               # Search for node at position index - 1 or the last position
               current = self._head
               while index > 1 and current.next != None:
                    current = current.next
                    index -= 1
               # Insert new node after node at position index - 1
               # or last position
               self._insert_After(object, current)
               #current.next = Node(object, current.next)
          self._size += 1

     def append(self, object):
          """add object Last position"""
          self.insert(len(self),object)
     
     def __removeFirst(self):
          removedItem = self._head.value
          self._head = self._head.next
          self._size -= 1
          return removedItem
     
     def pop(self, index=-1):
          """remove object in to position index"""
          if len(self) == 0:
               raise IndexError('pop from empty list')
          if index < 0:
               index+=len(self)          
          if index < 0 or index >= len(self):
               raise IndexError('pop index out of range')          
          if index == 0: # remove fisrt
               return self.__removeFirst()
          # Search for node at position index - 1 or
          # the next to last position
          current  = self._head
          while index > 1 and current.next.next != None:
               current  = current.next
               index -= 1
          removedItem = current.next.value
          current.next = current.next.next
          self._size -= 1
          return removedItem

     def remove(self,value):
          """remove object equal value"""
          if len(self) == 0:
               raise IndexError('pop from empty list')
          if self._head.value == value: # remove first
               return self.__removeFirst()
          current = self._head
          previous = None
          while current.next != None:
               if current.value == value:
                    previous = current.next
                    self._size -= 1
                    return
               previous = current
               current = current.next
          raise ValueError('list.remove(x): x not in list')
          
     def extend(self,iterable=None):
          """append a iterable"""
          if not iterable:
               raise TypeError('list.extend() takes exactly one argument (0 given)')
          for value in iterable:
               self.append(value)

     def reverse(self):  
          # Initialize three pointers: curr, prev and next
          curr = self._head
          prev = None
          while curr:
               # Store next
               nextNode = curr.next
               # Reverse current node's next pointer
               curr.next = prev
               # Move pointers one position ahead
               prev = curr
               curr = nextNode
          self._head=prev
          
     def _slice(self,s):
          """"""
          if not self._head:
               return []
          toRet=[]
          index = 0
          current  = self._head
          while index < s.start and current.next != None:
               value = current.value
               current  = current.next
               index+=1
          if index < s.start:
               return []
          gap = 1
          toRet.append(value)
          stop=len(self)
          if s.stop < stop:
               stop = s.stop
          while index < stop and current.next != None:
               value = current.value
               current  = current.next
               if gap < s.step:
                    gap+=1
               else:
                    toRet.append(value)
                    gap=1
               index+=1
          if index + s.step-gap< stop and current:
               toRet.append(current.value)
          return toRet

     """native python functions"""
     def __str__(self):
          """ The string representation of the linkedList"""
          return str([e for e in self])

     def __len__(self):
          """ Length of the list"""
          return self._size

     def __repr__(self):
          """ The representation of the linkedList"""
          return "{0} {1}".format(self.__class__.__name__, self)

     def __iter__(self):
            """ Supports traversal with a for loop"""
            current = self._head
            while current is not None:
                yield current.value
                current = current.next
     
     def __getitem__(self, index=-1):
          """ Subscript operator for access at index"""
          if isinstance(index,slice):
               return list(self)[index]
          if index < 0:
               index+=len(self)          
          if index < 0 or index >= len(self):
               raise IndexError('list index out of range')
          probe = self._head
          while index > 0 and probe.next != None:
               probe = probe.next
               index -= 1
          return probe.value
     
     def __setitem__(self, index, value):
          """ Subscript operator for replacement at index"""
          if index < 0:
               index+=len(self)          
          if index < 0 or index >= len(self):
               raise IndexError('list assignment index out of range')
          probe = self._head
          while index > 0 and probe.next != None:
               probe = probe.next
               index -= 1
          probe.value = value

     def __contains__(self, value):
          current  = self._head
          while current != None:
               if current.value==value:
                    return True
               current  = current.next
          return False

def __reversed__(self,iterable):
      head = Node(self._head.value)
      curr=self._head.value
      prev=head
      while curr.next:
           prev = curr.next
           curr.next = prev
      return prev

class dNode(object):
     """Represents a doubled linked node."""
     def __init__(self, value, next = None, prev = None):
          """Instantiates a Node with a default next and prev of None."""
          self.value = value
          self.next = next
          self.prev= prev
          
     """native python functions"""     
     def __str__(self):
          return str(self.value)+'-->'+str(self.next)

     def __repr__(self):
          return str(self)
     
class Deque(abstractList):
     """Represents a Doubly Linked List"""
     def __init__(self, iterable = None, maxlen=0): 
          """Instantiates a linked list with a default
             head of None and size zeroe"""
          self._head=None
          self._tail=None
          self._size=0
          if maxlen==0:
               self._maxlen=999999999
          else:
               self._maxlen=maxlen 
          if iterable:
               for value in iterable:
                    self.append(value)

     def append(self, value):
        if self._size >= self._maxlen:
            raise Exception("Deque cheia")

        newNode = dNode(value)

        # Caso 1: deque vazia
        if self._head is None:
            self._head = newNode
            self._tail = newNode

        # Caso 2: deque não vazia
        else:
            newNode.prev = self._tail
            self._tail.next = newNode
            self._tail = newNode

        self._size += 1

     def appendleft(self, value):
        if self._size >= self._maxlen:
            raise Exception("Deque cheia")

        newNode = dNode(value)

        # Caso 1: deque vazia
        if self._head is None:
            self._head = newNode
            self._tail = newNode

        # Caso 2: deque não vazia
        else:
            newNode.next = self._head
            self._head.prev = newNode
            self._head = newNode

        self._size += 1

     def pop(self):
        if self._size == 0:
            raise Exception("Deque vazia")

        removedNode = self._tail
        value = removedNode.value

        # Caso 1: apenas um elemento
        if self._head == self._tail:
            self._head = None
            self._tail = None

        # Caso 2: mais de um elemento
        else:
            self._tail = self._tail.prev
            self._tail.next = None

        self._size -= 1
        return value

     def popleft(self):
        if self._size == 0:
            raise Exception("Deque vazia")

        value = self._head.value

        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None

        self._size -= 1
        return value
     
     def reverse(self):
          # Initialize three pointers: curr, prev and next
          curr = self._head
          prev = None
          while curr:
               # Store next
               nextNode = curr.next
               # Reverse current node's next pointer
               curr.next = prev
               # Move pointers one position ahead
               prev = curr
               curr = nextNode
          self._tail.prev = self._head.next
          self._head=prev

class PriorityQueue(abstractList):
    """Represents a PriorityQueue with Doubly Linked List"""
    def __init__(self, iterable = None, maxlen=0):
          """Instantiates a linked list with a default
             head of None and size zeroe"""
          self._head=None
          self._tail=None
          self._size=0
          if maxlen==0:
               self._maxlen=999999999
          else:
               self._maxlen=maxlen 
          if iterable:
               for value in iterable:
                    self.put(value)
                    
    def put(self, value):
         if self._size >= self._maxlen:
              raise Exception("PriorityQueue cheia")

         newNode = dNode(value)

         # Caso 1: fila vazia
         if self._head is None:
              self._head = self._tail = newNode

         # Caso 2: inserir no início
         elif value < self._head.value:
              newNode.next = self._head
              self._head.prev = newNode
              self._head = newNode

         else:
              current = self._head

              # Avança até achar posição correta
              while current.next and current.next.value <= value:
                   current = current.next

              newNode.next = current.next
              newNode.prev = current

              if current.next:
                   current.next.prev = newNode
              else:
                   self._tail = newNode

              current.next = newNode

         self._size += 1

    def get(self):
         if self._size == 0:
              raise Exception("PriorityQueue vazia")

         value = self._head.value

         # Caso 1: apenas um elemento
         if self._head == self._tail:
              self._head = self._tail = None
         else:
              self._head = self._head.next
              self._head.prev = None

         self._size -= 1
         return value

class PriorityQueue1(abstractList):
     def __init__(self, iterable=None, maxlen=0, cmp=None):
          self._head = None
          self._tail = None
          self._size = 0
          self._maxlen = maxlen if maxlen > 0 else 999999999
          # Comparador padrão: max-priority numérica
          if cmp is None:
               self._cmp = lambda a, b: a > b
          else:
               self._cmp = cmp

          if iterable:
               for value in iterable:
                    self.put(value)
                    
     def put(self, value):
         if self._size >= self._maxlen:
              raise Exception("PriorityQueue cheia")

         newNode = dNode(value)

         # Caso 1: fila vazia
         if self._head is None:
              self._head = self._tail = newNode

         # Caso 2: inserir no início
         elif self._cmp(value, self._head.value):
              newNode.next = self._head
              self._head.prev = newNode
              self._head = newNode

         else:
              current = self._head

              # Avança enquanto o próximo tiver prioridade
              # MAIOR ou IGUAL (fila estável)
              while (current.next and
                     not self._cmp(value, current.next.value)):
                   current = current.next

              newNode.next = current.next
              newNode.prev = current

              if current.next:
                   current.next.prev = newNode
              else:
                   self._tail = newNode

              current.next = newNode

         self._size += 1

     def get(self):
         if self._size == 0:
              raise Exception("PriorityQueue vazia")

         value = self._head.value

         if self._head == self._tail:
              self._head = self._tail = None
         else:
              self._head = self._head.next
              self._head.prev = None

         self._size -= 1
         return value

     def peek(self):
         """Retorna o elemento de maior prioridade sem remover"""
         if self._size == 0:
              raise Exception("PriorityQueue vazia")
         return self._head.value

if __name__ == '__main__':
     """
     s=stack()
     q=queue()
     l=linkedList()
     d=Deque()
     print('Min-priority ')
     pq=PriorityQueue([30,20,10],3)
     print(pq)
     print('Max-priority numérica')
     pq = PriorityQueue1(cmp=lambda a, b: a > b)
     pq.put(3)
     pq.put(10)
     pq.put(1)

     print(list(pq))   # [10, 3, 1]
     print("Min-priority numérica")
     pq = PriorityQueue1(cmp=lambda a, b: a < b)
     pq.put(3)
     pq.put(10)
     pq.put(1)

     print(list(pq))   # [1, 3, 10]
     pq = PriorityQueue1(cmp=lambda a, b: a[0] > b[0])

     pq.put((2, "baixo"))
     pq.put((10, "alto"))
     pq.put((5, "medio"))
     print('Prioridade explícita (tupla) Max')
     print(list(pq)) # [(10, 'alto'), (5, 'medio'), (2, 'baixo')]
     """
     Arr=Array('i',[0,1,2,3,5])
     arr=array('i',[0,1,2,3,5])
     letras=array('u',['a','b','c','e'])
     id(arr);id(arr[0]);id(arr[1]);id(arr[2]);id(arr[3]);id(arr[4])
     id(letras);id(letras[0]);id(letras[1]);id(letras[2]);id(letras[3])


         
         

