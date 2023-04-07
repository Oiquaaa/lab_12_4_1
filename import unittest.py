import unittest
from lab12_4_1 import CircularLinkedList
class TestCircularLinkedList(unittest.TestCase):

    def setUp(self):
        self.c_list = CircularLinkedList()
        self.c_list.insert(1)
        self.c_list.insert(2)
        self.c_list.insert(3)
        self.c_list.insert(4)
        self.c_list.insert(5)
        self.c_list.insert(6)

    def test_sum_even(self):
        result = self.c_list.sum_even()
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()
