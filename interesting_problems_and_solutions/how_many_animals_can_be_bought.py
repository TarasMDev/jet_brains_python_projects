# Simple script that shows how many animals you can buy with strict amount of money
# animals and prices
animals = {'sheep': 6769, 'cow': 3848, 'pig': 1296, 'goat': 678, 'chicken': 23}
money = int(input())
result = None
for animal in animals:
    amount = money // animals[animal]
    if amount > 0:
        if amount == 1 or animal == 'sheep':
            result = (amount, animal)
        else:
            result = (amount, animal + 's')
        break
if result is None:
    print('None')
else:
    print(*result)
