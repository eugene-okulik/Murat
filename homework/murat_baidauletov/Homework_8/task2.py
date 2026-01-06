# Ограничили количество шагов до 100,чтобы случайно не запустить бесконечный цикл.

def fibonachi(limit=100):
    start_num1 = 0
    start_num2 = 1
    count = 1
    while count < limit:
        yield start_num1
        start_num1, start_num2 = start_num2, start_num1 + start_num2
        count += 1


num = 0
for number in fibonachi(1000000):
    num += 1
    if num == 5 or num == 200 or num == 1000 or num == 100000:
        print(number)
        if num == 100000:
            break
