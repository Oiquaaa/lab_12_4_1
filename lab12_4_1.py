class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
            if current == self.head:
                break

    def sum_even(self):
        current = self.head
        sum = 0
        while current:
            if current.data % 2 == 0:
                sum += current.data
            current = current.next
            if current == self.head:
                break
        return sum

# Створюємо кільцевий однонаправлений список
c_list = CircularLinkedList()
c_list.insert(1)
c_list.insert(2)
c_list.insert(3)
c_list.insert(4)
c_list.insert(5)
c_list.insert(6)

# Виводимо список на екран
print('Список:')
c_list.display()

# Обчислюємо суму елементів із парними значеннями інформаційного поля
sum_even = c_list.sum_even()
print('\nСума елементів із парними значеннями:', sum_even,sep='\n',end=' ')
