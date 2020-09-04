from test1 import *

s = LinkedList()

# Ситуации, которые надо проверить:
# 1) список пустой
# 2) содержит один элемент
# 3) содержит много элементов
# 4) проверить вставку, удаление одного и нескольких элементов, поиск
# 5) уделить внимание head и tail.

# delete 1.1

def empty_delete_1():
    s.delete(25, False)
    if s.len() == 0 and s.head == None and s.tail == None:
        print('Test 1: empty_delete_1_correct')
    s.clean()

empty_delete_1()

def one_delete_2():
    s.add_in_tail(Node(25))
    s.delete(25, False)
    if s.len() == 0 and s.head == None and s.tail == None:
        print('Test 2: one_delete_2 correct')
    s.clean()

one_delete_2()

def three_delete_3(): # удаление в середине
    s.add_in_tail(Node(25))
    s.add_in_tail(Node(35))
    s.add_in_tail(Node(45))
    s.delete(35, False)
    if s.len() == 2 and s.head.value == 25 and s.tail.value == 45:
        print('Test 3: three_delete_3 correct')
    s.clean()

three_delete_3()

def three_delete_4(): # удаление в начале
    s.add_in_tail(Node(25))
    s.add_in_tail(Node(35))
    s.add_in_tail(Node(45))
    s.delete(25, False)
    if s.len() == 2 and s.head.value == 35 and s.tail.value == 45:
        print('Test 4: three_delete_4 correct')
    s.clean()

three_delete_4()

def three_delete_5(): # удаление в конце
    s.add_in_tail(Node(25))
    s.add_in_tail(Node(35))
    s.add_in_tail(Node(45))
    s.delete(45, False)
    if s.len() == 2 and s.head.value == 25 and s.tail.value == 35:
        print('Test 5: three_delete_5 correct')
    s.clean()

three_delete_5()

def two_delete_6(): # удаление в начале
    s.add_in_tail(Node(25))
    s.add_in_tail(Node(35))
    s.delete(25, False)
    if s.len() == 1 and s.head.value == 35 and s.tail.value == 35:
        print('Test 6: two_delete_6 correct')
    s.clean()

two_delete_6()

def two_delete_7(): # удаление в конце
    s.add_in_tail(Node(25))
    s.add_in_tail(Node(35))
    s.delete(35, False)
    if s.len() == 1 and s.head.value == 25 and s.tail.value == 25:
        print('Test 7: two_delete_7 correct')
    s.clean()

two_delete_7()

def many_delete_8(): # удаление в начале
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(30))
    s.add_in_tail(Node(40))
    s.add_in_tail(Node(50))
    s.add_in_tail(Node(60))
    s.delete(10, False)
    if s.len() == 5 and s.head.value == 20 and s.tail.value == 60:
        print('Test 8: many_delete_8 correct')
    s.clean()

many_delete_8()

def many_delete_9(): # удаление в середине
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(30))
    s.add_in_tail(Node(40))
    s.add_in_tail(Node(50))
    s.add_in_tail(Node(60))
    s.delete(30, False)
    if s.len() == 5 and s.head.value == 10 and s.tail.value == 60:
        print('Test 9: many_delete_9 correct')
    s.clean()

many_delete_9()

def many_delete_10(): # удаление в конце
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(30))
    s.add_in_tail(Node(40))
    s.add_in_tail(Node(50))
    s.add_in_tail(Node(60))
    s.delete(60, False)
    if s.len() == 5 and s.head.value == 10 and s.tail.value == 50:
        print('Test 10: many_delete_10 correct')
    s.clean()

many_delete_10()
