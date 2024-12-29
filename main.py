import json

with open('y_spider/product_data.json') as file:
    data = json.load(file)

import json

prices = []
brands = []
ranks = []
i = 0

for product in data:

    ranks.append(product.get('Rank'))
    brands.append(product.get('brand'))
    prices.append(product.get('Price'))

print(len(ranks))
most_exp_index = prices.index(max(prices))

print(most_exp_index)
most_exp_brand = brands[most_exp_index]

print(brands[8])