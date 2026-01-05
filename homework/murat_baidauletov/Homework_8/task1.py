from random import choice, randint

bonus = ['True', 'False']

while True:
    salary = int(input('enter salary: '))
    bonus = choice([True, False])
    if bonus == True:
        salary_bonus = salary + randint(0, 1000)
        print(f"{salary}, {bonus} - '${salary_bonus}'")
    else:
        print(f"{salary}, {bonus} - '${salary}'")
