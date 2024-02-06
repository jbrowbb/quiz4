from dataclasses import dataclass

@ dataclass
class Product:
    name: str
    price: float
    category: str
    in_stock: bool = True

    def info_display(self) -> None:
        print("Product Information:")
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Category: ", self.category)
        print("In Stock", self.in_stock)


def main():
    product1 = Product("Laptop", 169.99, "Electronics")
    product2 = Product("Shorts", 10.99, "Clothing", in_stock=False)

    product1.info_display()
    print()
    product2.info_display()


if __name__=="__main__":
    main()