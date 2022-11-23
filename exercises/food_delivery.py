chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15

num_chicken_menus = int(input())
num_fish_menus = int(input())
num_vegan_menus = int(input())

price_chicken_menus = num_chicken_menus * chicken_menu
price_fish_menus = num_fish_menus * fish_menu
price_vegan_menus = num_vegan_menus * vegan_menu

price_for_all_menus = price_chicken_menus + price_fish_menus + price_vegan_menus

price_for_dessert = (20 / 100) * price_for_all_menus
price_for_delivery = 2.50

sum_for_order = price_for_all_menus + price_for_dessert + price_for_delivery

print("цена на поръчката", sum_for_order)