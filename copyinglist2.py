import copy

dairyed = ['milk','eggs','cheese']
cleaning_products = ['domestos', 'washing up liquid']

april_to_buy = [dairyed,cleaning_products]
print("april: ", april_to_buy)

may_to_buy = april_to_buy.copy()
print("may: ", may_to_buy)

june_to_buy = [x for x in april_to_buy]
print("june: ", june_to_buy)

july_to_buy = copy.deepcopy(april_to_buy)

april_to_buy[1].append('sponge')
print("april: ", april_to_buy)
print("may: ", may_to_buy)
print("june: ", june_to_buy)
print("july: ", july_to_buy)