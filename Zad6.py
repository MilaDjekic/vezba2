nylon  = int(input())
paint  = int(input())
thinner  = int(input())
work_hours  = int(input())
nylon_price = (nylon + 2) * 1.5
paint_price = (paint * 1.1) * 14.5
thinner_price = thinner * 5
material = nylon_price + paint_price + thinner_price + 0.4
labour = material * 0.3
amount_to_pay = material + labour * work_hours
print(amount_to_pay)