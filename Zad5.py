package_of_pens = int(input())
package_of_markers = int(input())
liter_of_detergent = int(input())
percentage = int(input())/100
total_price = package_of_pens * 5.8 + package_of_markers * 7.2 + liter_of_detergent * 1.2
discounted_price = total_price * (1-percentage)
print(discounted_price)