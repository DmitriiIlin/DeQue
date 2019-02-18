"""
Тесты для класса Deque. 
"""
import Two_sides_Queue, unittest, random

def String_generation(N):
    #Создаем строку
    out=[]
    for i in range(0,N):
        letter=str(random.randint(0,100))
        out.append(letter)
    return out 

def Deque_generation(input_string):
    #Инициализация э-та Deque
    Deque_element=Two_sides_Queue.Deque()
    S=len(input_string)
    for i in range(0,S):
        Deque_element.addTail(input_string[i])
    return Deque_element


class Deque_Tests(unittest.TestCase):
#Тесты для методов класса Deque

    def test_removeFront(self):
        #Проверка для удаления из головы
        input_string=String_generation(5)
        Deque_test=Deque_generation(input_string)
        delete_letter=input_string.pop(-len(input_string))
        delete_Deque_element=Deque_test.removeFront()
        self.assertEqual(delete_letter,delete_Deque_element)
        self.assertEqual(len(input_string),Deque_test.size())

    def test_removeTail(self):
        #Проверка удаления из хвоста
        input_string=String_generation(5)
        Deque_test=Deque_generation(input_string)
        delete_letter=input_string.pop()
        delete_Deque_element=Deque_test.removeTail()
        self.assertEqual(delete_letter,delete_Deque_element)
        self.assertEqual(len(input_string),Deque_test.size())

    def test_addFront(self):
        #Проверка для добавления в голову
        input_string=String_generation(5)
        Deque_test=Deque_generation(input_string)
        add_letter=str(random.randint(250,500))
        input_string.insert(0,add_letter)
        Deque_test.addFront(add_letter)
        self.assertEqual(len(input_string),Deque_test.size())
        self.assertEqual(input_string.pop(-len(input_string)),Deque_test.removeFront())
 
    def test_addTail(self):
        #Проверка для добавления в хвост
        input_string=String_generation(5)
        Deque_test=Deque_generation(input_string)
        add_letter=str(random.randint(250,500))
        input_string.append(add_letter)
        Deque_test.addTail(add_letter)
        self.assertEqual(len(input_string),Deque_test.size())
        self.assertEqual(input_string.pop(),Deque_test.removeTail())

if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()






