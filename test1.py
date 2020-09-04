class Node:

    def __init__(self, v):
        self.value = v
        self.next = None # связь указываем затем при инициализации связного-списка

class LinkedList:

    def __init__(self):
        self.head = None #головной-узел
        self.tail = None #конец-узел

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node != None: #
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        lst = list()
        while node != None:
            if node.value == val:
                lst.append(node) #
            node = node.next
        return lst #


    def clean(self): # 1.3
        self.head = None
        self.tail = None

    def len(self): # 1.5
        node = self.head
        if self.head == None:
            return 0 # empty list
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        node = self.head
        if afterNode == None:
            newNode.next = node
            self.head = newNode
            return


    def delete(self, val, all = True or False):
        node = self.head

        if node == None: # пустой список
            self.head = None
            self.tail = None
            return

        if self.len() == 1: # список с одним элементом
            if node.value == val:
                self.head = None
                self.tail = None
                return

        if all == False:

            if node.value == val: # первый элемент
                self.head = node.next
                return

            lastNode = node
            currentNode = node.next

            while True: # не включая первый и последний
                if currentNode.next == None: # последний элемент
                    if currentNode.value == val:
                        lastNode.next = None
                        self.tail = lastNode
                        return
                    else:
                        self.tail = currentNode
                        currentNode.next = None
                        return
                if currentNode.value == val:
                    lastNode.next = currentNode.next # None or Node
                    return
                lastNode = currentNode
                currentNode = currentNode.next

        elif all == True:

            if node.value == val: # плавающая голова
                while node.value == val:
                    node = node.next
                    self.head = node
                    if self.head == None: # на случай, если голова дошла до конца
                        self.clean()
                        return
            lastNode = node # lastNode != val
            currentNode = node.next

            if currentNode == None: # спислк с двумя элементами обрабатываем
                self.head = node
                self.tail = node
                return

            while True:
                if currentNode.next == None: # последний элемент
                    if currentNode.value == val:
                        lastNode.next = None
                        self.tail = lastNode
                        return
                    else:
                        self.tail = currentNode
                        return
                if currentNode.value == val:
                    lastNode.next = currentNode.next # None or Node
                lastNode = currentNode
                currentNode = currentNode.next
