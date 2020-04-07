cents = int(input('Money in Cents: '))
toonies = 0
loonies = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0
while cents != 0:
    if cents >= 200:
        cents -= 200
        toonies += 1
    elif cents >= 100:
        cents -= 100
        loonies += 1
    elif cents >= 25:
        cents -= 25
        quarters += 1
    elif cents >= 10:
        cents -= 10
        dimes += 1
    elif cents >= 5:
        cents -= 5
        nickels += 1
    elif cents >= 1:
        cents -= 1
        pennies += 1

print(f'Toonies: {toonies}')
print(f'Loonies: {loonies}')
print(f'Quarters: {quarters}')
print(f'Dimes: {dimes}')
print(f'Nickels: {nickels}')
print(f'Pennies: {pennies}')