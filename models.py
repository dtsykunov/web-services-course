from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float

    def __init__(self, name: str, price: float):
        super().__init__(name=name, price=price)


class Category(BaseModel):
    name: str
    stock: list[Item]

    def __init__(self, name, stock=None):
        if stock is None:
            stock = []
        super().__init__(name=name, stock=stock)

    def get_items(self, item_name: str) -> list[Item]:
        response = []
        for item in self.stock:
            if item.name == item_name:
                response.append(item)
        return response

    def contains(self, item_name: str):
        return bool(self.get_items(item_name))

    def add(self, item: Item):
        self.stock.append(item)


class Store(BaseModel):
    categories: dict[str, Category]

    def __init__(self, categories=None):
        if categories is None:
            categories = {}
        super().__init__(categories=categories)

    def get_or_create_category(self, category_name) -> Category:
        if category_name not in self.categories:
            self.categories[category_name] = Category(category_name)
        return self.categories[category_name]

    def add_to_stock(self, category_name: str, item: Item) -> Item:
        self.get_or_create_category(category_name).add(item)

    def get_items(self, category_name: str, item_name: str) -> list[Item]:
        return self.categories[category_name].get_items(item_name)

    def contains(self, category_name: str, item_name: str) -> bool:
        if category_name in self.categories:
            return self.categories[category_name].contains(item_name)
        return False
