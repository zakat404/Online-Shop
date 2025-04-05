# main.py
from online_shop.models import SimpleProduct, ProductGroup
from online_shop.pricing import DiscountPricingRule, EveryNthFreePricingRule
from online_shop.category import Category

def main():
    # Создание простых товаров
    p1 = SimpleProduct("Товар 1", 100)
    p2 = SimpleProduct("Товар 2", 200)
    p3 = SimpleProduct("Товар 3", 300)
    p4 = SimpleProduct("Товар 4", 50)
    p5 = SimpleProduct("Товар 5", 150)

# Группа товаров со скидкой 10%
    discount_rule = DiscountPricingRule(10)
    group1 = ProductGroup("Группа с 10% скидкой", [p1, p2, p3], discount_rule)
    print(f"Цена группы '{group1.name}' (10% скидка): {group1.get_price()}")


# Группа товаров: каждый 5-й товар бесплатный
    every5_free_rule = EveryNthFreePricingRule(5)
# Сумма цен = 100+200+300+50+150 = 800, бесплатным должен быть самый дешёвый (50)
    group2 = ProductGroup("Группа: каждый 5‑й бесплатный", [p1, p2, p3, p4, p5], every5_free_rule)
    print(f"Цена группы '{group2.name}' (каждый 5‑й бесплатный): {group2.get_price()}")  # Ожидается: 750

# Создание категорий с подкатегориями
    cat_main = Category("Электроника")
    cat_sub = Category("Мобильные телефоны")
    cat_sub2 = Category("Аксессуары")
    cat_main.add_subcategory(cat_sub)
    cat_main.add_subcategory(cat_sub2)

# Добавление товаров в категории
    cat_main.add_product(p1)        # товар в главной категории
    cat_sub.add_product(p2)         # товар в подкатегории "
    cat_sub2.add_product(group1)    # группа товаров в подкатегории
    cat_sub2.add_product(p3)        # товар в подкатегории

    all_products = cat_main.get_all_products()
    print("\nВсе товары в категории 'Электроника' (с учетом подкатегорий):")
    for product in all_products:
        print(f" - {product.name}: цена = {product.get_price()}")

if __name__ == "__main__":
    main()
