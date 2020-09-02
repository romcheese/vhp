from test1 import *

s = LinkedList()
def test0_1():
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.delete(10)
    # s.print_all_nodes()

    if s.head.value == 20 and s.tail.value == 20:
        print('0.1 correct')
    else:
        print('0.1 not correct')

def test0_2():
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(10))
    s.delete(10)
    # s.print_all_nodes()

    if s.head.value == 20 and s.tail.value == 20:
        print('0.2 correct')
        s.clean()
    else:
        s.clean()
        print('0.2 not correct')




# Tests:
def test1_1():# Удаляем элемент в пустом списке - correct
    s.delete(25, False)
    
    if s.head == None and s.tail == None:
        print('1.1 correct')
        s.clean()
    else:
        print('1.1 not correct')
        s.clean()

# Список из трех элементов, False.

def test1_2(): # удаление первого элемента - correct
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(30))
    s.delete(10, False)

    if s.head.value == 20 and s.tail.value == 30:
        print('1.2 correct')
        s.clean()
    else:
        print('1.2 not correct')
        s.clean()

def test1_3(): # удаление срединного элемента - correct
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(30))
    s.delete(20, False)

    if s.head.value == 10 and s.tail.value == 30:
        print('1.3 correct')
        s.clean()
    else:
        print('1.3 not correct')
        s.clean()

def test1_4(): # удаление последнего элемента
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(30))
    s.delete(30, False)

    if s.head.value == 10 and s.tail.value == 20:
        print('1.4 correct')
        s.clean()
    else:
        print('1.4 not correct')
        s.clean()

def test1_5(): # попытка удаления несуществующего элемента
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(30))
    s.delete(40, False)

    if s.head.value == 10 and s.tail.value == 30:
        print('1.5 correct')
        s.clean()
    else:
        print('1.5 not correct')
        s.clean()









# Список более 3х элементов

def test2_2(): # удаление первого элемента - correct
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(30))
    s.add_in_tail(Node(50))
    s.delete(10, False)

    if s.head.value == 20 and s.tail.value == 50:
        print('2.2 correct')
        s.clean()
    else:
        print('2.2 not correct')
        s.clean()

def test2_3(): # удаление срединного элемента - correct
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(40))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(60))
    s.delete(40, False)

    if s.head.value == 10 and s.tail.value == 60:
        print('2.3 correct')
        s.clean()
    else:
        print('2.3 not correct')
        s.clean()

def test2_4(): # удаление последнего элемента
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(30))
    s.add_in_tail(Node(80))
    s.add_in_tail(Node(70))
    s.delete(70, False)

    if s.head.value == 10 and s.tail.value == 80:
        print('2.4 correct')
        s.clean()
    else:
        print('2.4 not correct')
        s.clean()



def test2_5(): # попытка удаления несуществующего элемента
    s.add_in_tail(Node(5))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(30))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(90))
    s.delete(40, False)

    if s.head.value == 5 and s.tail.value == 90:
        print('2.5 correct')
        s.clean()
    else:
        print('2.5 not correct')
        s.clean()


# Список c одним элементом

def test3_1(): # удаление первого элемента - correct
    s.add_in_tail(Node(10))
    s.delete(10, False)

    if s.head == None and s.tail == None:
        print('3.1 correct')
        s.clean()
    else:
        print('3.1 not correct')
        s.clean()





# Односвязный список из двух элементов (на всякий случай)

def test4_1(): # удаление первого элемента - correct
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.delete(10, False)

    if s.head.value == 20 and s.tail.value == 20:
        print('4.1 correct')
        s.clean()
    else:
        print('4.1 not correct')
        s.clean()



def test4_2(): # удаление последнего элемента
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.delete(20, False)

    if s.head.value == 10 and s.tail.value == 10:
        print('4.2 correct')
        s.clean()
    else:
        print('4.2 not correct')
        s.clean()

def test4_5(): # попытка удаления несуществующего элемента
    s.add_in_tail(Node(5))
    s.add_in_tail(Node(20))
    s.delete(40, False)

    if s.head.value == 5 and s.tail.value == 20:
        print('4.5 correct')
        s.clean()
    else:
        print('4.5 not correct')
        s.clean()



# ___________________________________________________
# TRUE.


# Список из трех элементов, True.

def test5_2(): # удаление первого элемента - correct
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(30))
    s.delete(10, True)

    if s.head.value == 20 and s.tail.value == 30:
        print('5.2 correct')
        s.clean()
    else:
        print('5.2 not correct')
        s.clean()

def test5_3(): # удаление срединного элемента - correct
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(30))
    s.delete(20, True)

    if s.head.value == 10 and s.tail.value == 30:
        print('5.3 correct')
        s.clean()
    else:
        print('5.3 not correct')
        s.clean()

def test5_4(): # удаление последнего элемента
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(30))
    s.delete(30, True)

    if s.head.value == 10 and s.tail.value == 20:
        print('5.4 correct')
        s.clean()
    else:
        print('5.4 not correct')
        s.clean()

def test5_5(): # попытка удаления несуществующего элемента
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(30))
    s.delete(40, True)

    if s.head.value == 10 and s.tail.value == 30:
        print('5.5 correct')
        s.clean()
    else:
        print('5.5 not correct')
        s.clean()


# Список более 3х элементов

def test6_2(): # удаление всего списка
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(10))
    s.delete(10, True)
    # s.print_all_nodes()

    if s.head == None and s.tail == None:
        print('6.2 correct')
        s.clean()
    else:
        print('6.2 not correct')
        s.clean()

def test6_3(): # удаление срединного элемента - correct
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(10))
    s.delete(10, True)
    # s.print_all_nodes()

    if s.head == None and s.tail == None:
        print('6.3 correct')
        s.clean()
    else:
        print('6.3 not correct')
        s.clean()

def test6_4(): # удаление последнего элемента
    s.add_in_tail(Node(70))
    s.add_in_tail(Node(20))
    s.delete(70, True)

    if s.head.value == 20 and s.tail.value == 20:
        print('6.4 correct')
        s.clean()
    else:
        print('6.4 not correct')
        s.clean()

def test6_5(): # попытка удаления несуществующего элемента
    s.add_in_tail(Node(5))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(30))
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.add_in_tail(Node(90))
    s.delete(40, True)
    # s.print_all_nodes()

    if s.head.value == 5 and s.tail.value == 90:
        print('6.5 correct')
        s.clean()
    else:
        print('6.5 not correct')
        s.clean()



# Список c одним элементом

def test3_1(): # удаление первого элемента - correct
    s.add_in_tail(Node(10))
    s.delete(10, False)

    if s.head == None and s.tail == None:
        print('3.1 correct')
        s.clean()
    else:
        print('3.1 not correct')
        s.clean()

# Односвязный список из двух элементов (на всякий случай)

def test4_1(): # удаление первого элемента - correct
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.delete(10, False)

    if s.head.value == 20 and s.tail.value == 20:
        print('4.1 correct')
        s.clean()
    else:
        print('4.1 not correct')
        s.clean()

def test4_2(): # удаление последнего элемента
    s.add_in_tail(Node(10))
    s.add_in_tail(Node(20))
    s.delete(20, False)

    if s.head.value == 10 and s.tail.value == 10:
        print('4.2 correct')
        s.clean()
    else:
        print('4.2 not correct')
        s.clean()

def test4_5(): # попытка удаления несуществующего элемента
    s.add_in_tail(Node(5))
    s.add_in_tail(Node(20))
    s.delete(40, False)

    if s.head.value == 5 and s.tail.value == 20:
        print('4.5 correct')
        s.clean()
    else:
        print('4.5 not correct')
        s.clean()
test0_1()
test0_2()
test1_1()
test1_2()
test1_3()
test1_4()
test1_5()
test2_2()
test2_3()
test2_4()
test2_5()
test3_1()
test4_1()
test4_2()
test4_5()
test5_2()
test5_3()
test5_4()
test5_5()
test6_2()
test6_3()
test6_4()
test6_5()
