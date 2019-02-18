"""
Реализация двусторонней очереди
"""
class Deque:
    def __init__(self):
        # инициализация внутреннего хранилища
        self.Deque_list=[]

    def addFront(self, item):
        # добавление в голову
        self.Deque_list.insert(0,item)

    def addTail(self, item):
        # добавление в хвост
        self.Deque_list.append(item)

    def removeFront(self):
        # удаление из головы
        if len(self.Deque_list)==0:
            return None
        else:
            Deque_element=self.Deque_list.pop(-len(self.Deque_list))
            return Deque_element


    def removeTail(self):
        # удаление из хвоста
        if len(self.Deque_list)==0:
            return None
        else:
            Deque_element=self.Deque_list.pop()
            return Deque_element

    def size(self):
        if len(self.Deque_list)==0:
            return 0
        else:
            Deque_size=len(self.Deque_list)
            return Deque_size
    
    def print(self):
        #Печать очереди
        s=len(self.Deque_list)
        for i in range(0,s):
            print(self.Deque_list[i],'output print all nodes')
            s+=1

def Polindrom(input_string):
    #Функция проверяет является ли вводимая строка полиндромом
    Deque_string=Deque()
    s=len(input_string)
    if s==0:
        output_messege="It is zero string"
    else:
        for i in range(0,s):
            Deque_string.addTail(input_string[i])
    if s%2==0:
        L=s/2
    else:
        L=(s-1)/2
    while (L>=0) and (s!=0):
            Degue_front=Deque_string.removeFront()
            Degue_back=Deque_string.removeTail()
            if Degue_front!=Degue_back:
                output_messege="This is not polindrom"
                break
            else:
                output_messege="This is pilindrom"
            L-=2
    L=output_messege+" "+input_string
    return L

