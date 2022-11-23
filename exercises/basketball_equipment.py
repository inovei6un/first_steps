year_tax_for_basketball_training = int(input())

basketball_shoes = year_tax_for_basketball_training - (40 / 100 * year_tax_for_basketball_training)
basketball_outfit = basketball_shoes - (20 / 100 * basketball_shoes)
basket_ball = (1 / 4) * basketball_outfit
basketball_accessories = (1 / 5) * basket_ball

sum_for_all = year_tax_for_basketball_training + basketball_shoes + basketball_outfit + basket_ball + basketball_accessories

print("Разходи за една година", sum_for_all)
