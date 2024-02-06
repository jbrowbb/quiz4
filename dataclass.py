from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    category: str
    in_stock: bool = True

def main():
    # creating products
    product1 = Product("Laptop", 169.99, "Electronics")
    product2 = Product("Shorts", 10.99, "Clothing", in_stock=False)

    # printing product information
    print("Product 1:")
    print("Product Name: ", product1.name)
    print("Product Price: ", product1.price)
    print("Category: ", product1.category)
    print("In Stock: ", product1.in_stock)

    print("Product 2:")
    print("Product Name: ", product2.name)
    print("Product Price: ", product2.price)
    print("Category: ", product2.category)
    print("In Stock: ", product2.in_stock)


if __name__=="__main__":
    main()