class Category:
    def __init__(self, name: str):
        self.name = name
        self.subcategories = []  # список подкатегорий
        self.products = []       # список товаров

    def add_subcategory(self, subcategory: 'Category'):
        self.subcategories.append(subcategory)

    def add_product(self, product):
        self.products.append(product)

    def get_all_products(self) -> list:
        all_products = list(self.products)
        for sub in self.subcategories:
            all_products.extend(sub.get_all_products())
        return all_products
