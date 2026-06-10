class Flower:
    def __init__(self, name, color, stem_length, price, freshness, life_time):
        self.name = name
        self.color = color
        self.stem_length = stem_length  # длина стебля
        self.price = price  # стоимость
        self.freshness = freshness  # свежесть от 1 до 10
        self.life_time = life_time  # сколько дней живёт цветок

    def __str__(self):
        return (
            f"{self.name}, цвет: {self.color}, цена: {self.price}, "
            f"свежесть: {self.freshness}, жизнь: {self.life_time} дней"
        )


class Rose(Flower):
    def __init__(self, color, stem_length, price, freshness, life_time):
        super().__init__(
            "Роза",
            color,
            stem_length,
            price,
            freshness,
            life_time,
        )


class Tulip(Flower):
    def __init__(self, color, stem_length, price, freshness, life_time):
        super().__init__(
            "Тюльпан",
            color,
            stem_length,
            price,
            freshness,
            life_time,
        )


rose = Rose("красный", 40, 900, 7, 4)
rose2 = Rose("белый", 100, 1000, 3, 3)
tulip = Tulip("жёлтый", 30, 500, 8, 6)


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_total_price(self):
        total_price = 0

        for flower in self.flowers:
            total_price += flower.price

        return total_price

    def get_wilting_time(self):
        total_life_time = 0

        for flower in self.flowers:
            total_life_time += flower.life_time

        return total_life_time / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.freshness, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def find_by_life_time(self, min_life_time, max_life_time):
        found_flowers = []

        for flower in self.flowers:
            if min_life_time <= flower.life_time <= max_life_time:
                found_flowers.append(flower)

        return found_flowers

    def show_flowers(self):
        for flower in self.flowers:
            print(flower)


bouquet = Bouquet([rose, rose2, tulip])

print("Стоимость букета:", bouquet.get_total_price())
print("Среднее время увядания:", bouquet.get_wilting_time())

print("Сортировка по свежести:")
bouquet.sort_by_freshness()
bouquet.show_flowers()

print("Поиск цветов по времени жизни от 3 до 4 дней:")
found_flowers = bouquet.find_by_life_time(3, 4)

for flower in found_flowers:
    print(flower)
