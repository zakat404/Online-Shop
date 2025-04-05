# Онлайн Магазин

Проект представляет собой информационную систему "Онлайн Магазин", реализованную на Python. В системе реализована модель категорий и товаров, где товары бывают двух типов – обычные и группы товаров с динамическим расчетом цены.

## Основные возможности

- **Категории**  
  Товары распределяются по категориям, каждая из которых может содержать до 10 уровней вложенности. При просмотре категории выводятся товары из неё и всех подкатегорий.

- **Товары**  
  - **Обычный товар:** имеет имя и фиксированную цену.  
  - **Группа товаров:** имеет имя, список входящих товаров и правило расчёта цены.

- **Правила расчёта цены групп товаров:**  
  - **Скидка N%** от суммы цен товаров в группе.  
  - **Каждый N‑й товар бесплатный:** из группы бесплатно становится самый дешевый товар.

## Структура проекта
````
online_shop/
├── online_shop/
│   ├── __init__.py
│   ├── category.py
│   ├── models.py
│   └── pricing.py
├── tests/
│   ├── __init__.py
│   └── test_shop.py
├── main.py
└── README.md
````

```mermaid
classDiagram
    class Category {
        -string name
        -list products
        -list subcategories
        +add_product()
        +add_subcategory()
        +get_all_products()
    }
    class Product {
        <<abstract>>
        -string name
        +get_price(): float
    }
    class SimpleProduct {
        -float price
        +get_price(): float
    }
    class ProductGroup {
        -list products
        -PricingRule pricing_rule
        +get_price(): float
    }
    Product <|-- SimpleProduct
    Product <|-- ProductGroup

    class PricingRule {
        <<abstract>>
        +calculate(products: list): float
    }
    class DiscountPricingRule {
        -float discount_percentage
        +calculate(products: list): float
    }
    class EveryNthFreePricingRule {
        -int n
        +calculate(products: list): float
    }
    PricingRule <|-- DiscountPricingRule
    PricingRule <|-- EveryNthFreePricingRule

