import json

with open('y_spider/product_data.json') as file:
    data = json.load(file)

import json

prices = []
brands = []
ranks = []
full_names = []
i = 0

for product in data:

    ranks.append(product.get('Rank'))
    brands.append(product.get('brand'))
    prices.append(product.get('Price'))
    full_names.append(product.get('Name'))

print(f"In {len(ranks)} Brands\n")
most_exp_index = prices.index(max(prices))
most_chep_index = prices.index(min(prices))

print(f"Most cheap product is : {full_names[most_chep_index]}; which belongs to the brand : {brands[most_chep_index]}\n")
print(f"Most expensive brand is : {full_names[most_exp_index]}; which belongs to the brand : {brands[most_exp_index]}")
