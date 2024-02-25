chicken_menu = int(input())
fish_menu = int(input())
vegeterian_menu = int(input())

total_bill = chicken_menu * 10.35 + fish_menu * 12.40 + vegeterian_menu * 8.15

dessert = total_bill * 0.2

final_charge = total_bill + dessert + 2.50
print(final_charge)