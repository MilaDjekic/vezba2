deposited_amount = float(input())
months = int(input())
interest_rate = float(input())/100
amount = deposited_amount + months * ((deposited_amount * interest_rate) / 12)
print(amount)