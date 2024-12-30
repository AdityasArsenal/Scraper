import json
import matplotlib.pyplot as plt
import numpy as np

with open('y_spider/product_data.json') as file:
    data = json.load(file)

import json

ratings = []
prices = []
brands = []
ranks = []
full_names = []
i = 0

for product in data:

    ratings.append(product.get('Rating'))
    ranks.append(product.get('Rank'))
    brands.append(product.get('brand'))
    prices.append(product.get('Price'))
    full_names.append(product.get('Name'))

def lhbrands():
    print(f"In {len(ranks)} Brands\n")
    most_exp_index = prices.index(max(prices))
    most_chep_index = prices.index(min(prices))

    print(f"Most cheap product is : {full_names[most_chep_index]}; which belongs to the brand : {brands[most_chep_index]}\n")
    print(f"Most expensive brand is : {full_names[most_exp_index]}; which belongs to the brand : {brands[most_exp_index]}")


def rating_vs_price():

    # Data for x and y axes
    sorted_prices = sorted(prices[0:5])
    sorted_ratings = sorted(ratings[0:5])

    x = [np.nan if val is None else val for val in sorted_prices]

    y = [np.nan if val is None else val for val in sorted_ratings]

    print(ratings)
    
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line')

    # Add labels and a title
    plt.xlabel('prices')
    plt.ylabel('Ratings')
    plt.title('Line Graph Example')

    # Add a legend
    plt.legend()

    # Display the graph
    plt.show()

rating_vs_price()