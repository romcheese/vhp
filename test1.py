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
        while node != None: # Почему не '!='? Даже подчеркнуто
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        lst = list()
        while node != None:
            if node.value == val:
                lst.append(node) # возвращаем value или Node(value)?
            node = node.next
        return lst # print(lst)?


    def clean(self): # 1.3
        self.head = None
        self.tail = None

    def len(self): # 1.5
        node = self.head
        if self.head == None:
            return None # empty list
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count # print(count)?

    def insert(self, afterNode, newNode): # Node() or value?
        node = self.head
        if afterNode == None:
            newNode.next = node
            self.head = newNode
            return
        while node != None:
            if node.value == afterNode.value:
                newNode.next = node.next
                node.next = newNode
                return
            node = node.next




    def delete(self, val, all = True or False):
        node = self.head
        if node == None: # empty linked list
            return None
        if all == False:
            if node.value == val:
                self.head = node.next # correct
                return
            while True:
                lastnode = node
                if node.next == None:
                    break
                else:
                    currentnode = node.next
                if currentnode.value == val:
                    lastnode.next = currentnode.next
                    return
                else:
                    node = node.next
        elif all == True:
            if node.value == val:
                self.head = node.next
            while True:
                lastnode = node
                if node.next == None:
                    break
                else:
                    currentnode = node.next
                if currentnode.value == val:
                    lastnode.next = currentnode.next
                else:
                    node = node.next

# s_list = LinkedList()
# s_list.add_in_tail(Node(12))
# s_list.add_in_tail(Node(22))
# s_list.add_in_tail(Node(32))
# s_list.add_in_tail(Node(42))
# s_list.add_in_tail(Node(12))
# TESTS:

# 1.1: correct
# s_list.delete(12, False)
# s_list.print_all_nodes()

# 1.2: correct
# s_list.delete(12, True)
# s_list.print_all_nodes()

# 1.3: correct
# s_list.clean()
# s_list.print_all_nodes()

# 1.4: correct
# s_list.find_all(12)

# 1.5: correct
# s_list.clean()
# s_list.len()

# # 1.7:
# s_list.insert(None, Node(25))
# s_list.print_all_nodes()
