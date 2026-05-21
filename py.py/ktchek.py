class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def get_info(self):
        return f"Товар: {self.__name}, цена: {self.__price} руб."


class Vegetable(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.__weight = weight

    def get_info(self):
        return f"Овощ: {self._Product__name}, цена: {self.get_price()} руб., вес: {self.__weight} кг"


class Grocery(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price)
        self.__quantity = quantity

    def get_info(self):
        return f"Продукт: {self._Product__name}, цена: {self.get_price()} руб., кол-во: {self.__quantity} шт"


class Household(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.__brand = brand

    def get_info(self):
        return f"Хоз. товар: {self._Product__name}, цена: {self.get_price()} руб., бренд: {self.__brand}"


def main():
    products = []

    for i in range(1, 11):
        products.append(Vegetable(f"Картошка {i}", 50 + i * 2, round(0.5 + i * 0.1, 1)))

    for i in range(1, 11):
        products.append(Grocery(f"Рис {i}", 80 + i * 5, i))

    for i in range(1, 11):
        products.append(Household(f"Мыло {i}", 150 + i * 10, f"Бренд{i}"))

    print("Чек")
    total = 0
    for product in products:
        print(product.get_info())
        total += product.get_price()

    print(f"К оплате: {total} руб.")
    print("Спасибо за покупку!")


if __name__ == "__main__":
    main()