if __name__ == '__main__':

    product_number = int(input("Enter number one to five to access product price\n"))
    quantity_sold = int(input("Enter quantity\n"))

    product_number1 = 2.98
    product_number2 = 4.50
    product_number3 = 9.98
    product_number4 = 4.49
    product_number5 = 6.87


    def product(product_number):
        if product_number == 1:
            retail_value = product_number1 * quantity_sold
            product_number += retail_value

        elif product_number == 2:
            retail_value = product_number2 * quantity_sold
            return retail_value
        elif product_number == 3:
            retail_value = product_number3 * quantity_sold
            return retail_value
        elif product_number == 4:
            retail_value = product_number4 * quantity_sold
            return product_number4
        elif product_number == product_number5:
            retail_value = product_number5 * quantity_sold
            return product_number5


