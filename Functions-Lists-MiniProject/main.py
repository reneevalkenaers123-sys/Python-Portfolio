products = ["Bike", "Shoes", "Surfboard", "Helmet", "Backpack"]

def show_products():
    print("Available Products:\n")

    for item in products:
        print("-", item)

def count_products():
    print("\nTotal Products:", len(products))

show_products()
count_products()
