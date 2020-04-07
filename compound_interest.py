money_deposited = float(input('Money Deposited: '))
year1 = money_deposited * (1.04)
year2 = money_deposited * (1.04 ** 2)
year3 = money_deposited * (1.04 ** 3)

print(f'Year 1: ${round(year1, 2)}')
print(f'Year 2: ${round(year2, 2)}')
print(f'Year 3: ${round(year3, 2)}')