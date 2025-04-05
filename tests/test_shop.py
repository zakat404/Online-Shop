import unittest
from online_shop.models import SimpleProduct, ProductGroup
from online_shop.pricing import DiscountPricingRule, EveryNthFreePricingRule
from online_shop.category import Category


class TestOnlineShop(unittest.TestCase):

    def setUp(self):
#Инициализация базовых товаров для тестов
        self.p1 = SimpleProduct("Товар 1", 100)
        self.p2 = SimpleProduct("Товар 2", 200)
        self.p3 = SimpleProduct("Товар 3", 300)
        self.p4 = SimpleProduct("Товар 4", 50)
        self.p5 = SimpleProduct("Товар 5", 150)

    def test_simple_product_price(self):
#Проверка что цена обычного товара возвращается корректно
        self.assertEqual(self.p1.get_price(), 100)
        self.assertEqual(self.p2.get_price(), 200)

    def test_discount_pricing_rule(self):
#Проверка расчета цены с использованием скидки
        discount_rule = DiscountPricingRule(10)
        group = ProductGroup("Группа со скидкой", [self.p1, self.p2, self.p3], discount_rule)

        self.assertAlmostEqual(group.get_price(), 540.0)

    def test_every_nth_free_pricing_rule(self):
#Проверка расчета цены с правилом 'каждый N-й бесплатный'
        every5_free_rule = EveryNthFreePricingRule(5)
        group = ProductGroup("Группа: каждый 5-й бесплатный", [self.p1, self.p2, self.p3, self.p4, self.p5],
                             every5_free_rule)

        self.assertEqual(group.get_price(), 750)

    def test_empty_group(self):
#Проверка расчета цены для пустой группы товаров
        discount_rule = DiscountPricingRule(10)
        group = ProductGroup("Пустая группа", [], discount_rule)
        self.assertEqual(group.get_price(), 0)

    def test_category_nested(self):
#Проверка рекурсивного сбора товаров из вложенных категорий
        cat_root = Category("Корневая категория")
        cat_level1 = Category("Уровень 1")
        cat_level2 = Category("Уровень 2")
        cat_level3 = Category("Уровень 3")
        cat_root.add_subcategory(cat_level1)
        cat_level1.add_subcategory(cat_level2)
        cat_level2.add_subcategory(cat_level3)

# Добавляем товары на разных уровнях
        cat_root.add_product(self.p1)
        cat_level1.add_product(self.p2)
        cat_level2.add_product(self.p3)
        cat_level3.add_product(self.p4)

        all_products = cat_root.get_all_products()
        self.assertEqual(len(all_products), 4)
        self.assertIn(self.p1, all_products)
        self.assertIn(self.p2, all_products)
        self.assertIn(self.p3, all_products)
        self.assertIn(self.p4, all_products)


if __name__ == '__main__':
    unittest.main()