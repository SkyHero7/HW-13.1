import unittest
from src.item import Item

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item1 = Item("Item 1", 10, 5)
        self.item2 = Item("Item 2", 20, 3)

    def test_get_total_cost(self):
        self.assertEqual(self.item1.get_total_cost(), 50)
        self.assertEqual(self.item2.get_total_cost(), 60)

    def test_apply_discount(self):
        self.item1.apply_discount()
        self.assertEqual(self.item1.price, 8.5)
        self.assertEqual(self.item2.price, 20)

if __name__ == '__main__':
    unittest.main()