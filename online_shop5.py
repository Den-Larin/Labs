class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Назва магазину: {self.shop_name}")
        print(f"Тип магазину: {self.store_type}")

    def open_shop(self):
        print(f"Магазин {self.shop_name} відкритий")

    def set_number_of_units(self, num):
        self.number_of_units = num

    def increment_number_of_units(self, num):
        self.number_of_units += num

class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products):
        super().__init__(shop_name, store_type)
        self.discount_products = discount_products

    def get_discount_products(self):
        print(f"Продукти зі знижкою: {self.discount_products}")

store1 = Shop("Сільпо", "Продукти")
store2 = Shop("Sinsay", "Одяг")
store3 = Shop("Золотий Вік", "Ювелірні вироби")

print("Завдання а:")
print(store1.shop_name)
print(store1.store_type)
store1.describe_shop()
store1.open_shop()

print("Завдання b:")
store1.describe_shop()
store2.describe_shop()
store3.describe_shop()

print("Завдання c:")
store = Shop("Тайстра", "Продукти")
print(store.number_of_units)
store.number_of_units = 10
print(store.number_of_units)

print("Завдання d:")
store.set_number_of_units(15)
print(store.number_of_units)
store.increment_number_of_units(5)
print(store.number_of_units)

print("Завдання e:")
store_discount = Discount("Puma", "Аксесуари", ["Кросівки", "Футболки", "Костюми"])
store_discount.get_discount_products()


