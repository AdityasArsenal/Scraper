import json
import matplotlib.pyplot as plt
import numpy as np

with open('y_spider/product_data.json') as file:
    data = json.load(file)

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
    most_exp_index = prices.index(max(prices))
    most_chep_index = prices.index(min(prices))

    print("🟢🟢🟢🟢🟢\n")
    print(f"In {len(ranks)} Brands\n")
    print(f"Most cheap product is : {full_names[most_chep_index]}; which belongs to the brand : {brands[most_chep_index]}\n")
    print(f"Most expensive brand is : {full_names[most_exp_index]}; which belongs to the brand : {brands[most_exp_index]}\n")
    print("🟢🟢🟢🟢🟢")


def rating_vs_price_graph():

    # Data for x and y axes
    sorted_prices = sorted(prices[0:5])
    sorted_ratings = sorted(ratings[0:5])

    x = [np.nan if val is None else val for val in sorted_prices]
    y = [np.nan if val is None else val for val in sorted_ratings]
    
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line')

    plt.xlabel('prices')
    plt.ylabel('Ratings')
    plt.title('Line Graph Example')

    # Display the graph
    plt.show()

def repeated_brand_indexes():
    brand_repeat_indexes = {}
    i = 0
    for brand in brands:
        if brand not in brand_repeat_indexes:
            brand_repeat_indexes[brand] = []
        brand_repeat_indexes[brand].append(i)
        i += 1

    return brand_repeat_indexes

def total_num_of_prds_from_each_brand():
    brand_indexes_dir = repeated_brand_indexes()
    i = 0
    unique_brands = list(set(brands))
    total_prds_of_each_brand = []
    for brand in unique_brands:
        total_prds_of_each_brand.append(len(brand_indexes_dir[brand]))
            
    return total_prds_of_each_brand


def brands_vs_num_of_prds_graph():
    unique_brands = list(set(brands))
    x = unique_brands
    y = total_num_of_prds_from_each_brand()
    plt.bar(x, y)

    plt.xlabel('Brands')
    plt.ylabel('Number of Products')
    plt.xticks(rotation=90)
    plt.show()

rating_vs_price_graph()
brands_vs_num_of_prds_graph()
lhbrands()
