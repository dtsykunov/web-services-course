import unittest
from models import Item, Category, Store


class TestCategorySanity(unittest.TestCase):
    def setUp(self):
        self.category = Category("clothing")

    def test_add(self):
        item = Item("dress", 50.0)
        self.category.add(item)
        self.assertIn(item, self.category.stock)

    def test_name(self):
        self.assertEqual("clothing", self.category.name)


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category = Category("clothing")
        self.category.add(Item("dress", 50.0))
        self.category.add(Item("dress", 55.0))
        self.category.add(Item("skirt", 150.0))
        self.category.add(Item("shirt", 35.0))

    def test_contains(self):
        self.assertTrue(self.category.contains("dress"))
        self.assertTrue(self.category.contains("skirt"))
        self.assertTrue(self.category.contains("shirt"))
        self.assertFalse(self.category.contains("pants"))

    def test_get_items(self):
        items = self.category.get_items("dress")
        self.assertEqual(2, len(items))
        self.assertEqual(50.0, items[0].price)
        self.assertEqual(55.0, items[1].price)

        items2 = self.category.get_items("pants")
        self.assertEqual(0, len(items2))


class TestStore(unittest.TestCase):
    def setUp(self):
        self.clothing = Category("clothing")
        self.clothing.add(Item("dress", 50.0))
        self.clothing.add(Item("dress", 55.0))
        self.clothing.add(Item("skirt", 150.0))
        self.clothing.add(Item("shirt", 35.0))

        self.foods = Category("foods")
        self.foods.add(Item("potato", 5.0))
        self.foods.add(Item("banana", 15.0))

        self.store = Store({"clothing": self.clothing, "foods": self.foods})

    def test_get_or_create_category(self):
        self.assertEqual(self.clothing,
                         self.store.get_or_create_category("clothing"))
        self.assertNotIn("construction", self.store.categories)
        self.store.get_or_create_category("construction")
        self.assertIn("construction", self.store.categories)

    def test_contains(self):
        self.assertTrue(self.store.contains("clothing", "dress"))
        self.assertFalse(self.store.contains("clothing", "pants"))
        self.assertFalse(self.store.contains("foods", "dress"))

    def test_get_items(self):
        dresses = self.store.get_items("clothing", "dress")
        self.assertEqual(2, len(dresses))
        self.assertEqual(50.0, dresses[0].price)
        self.assertEqual(55.0, dresses[1].price)

        pants = self.store.get_items("clothing", "pants")
        self.assertEqual(0, len(pants))

    def test_add_to_stock(self):
        self.assertFalse(self.store.contains("clothing", "pants"))
        self.store.add_to_stock("clothing", Item("pants", 123.0))
        self.assertTrue(self.store.contains("clothing", "pants"))


if __name__ == '__main__':
    unittest.main()
