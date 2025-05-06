class BikeShop:
    def __init__(self, stock):
        self.stock = stock

    def display_bike(self):
        print("Total bikes available:", self.stock)

    def rent_for_bike(self, q):
        if q <= 0:
            print("Enter a positive value greater than zero.")
        elif q > self.stock:
            print("Enter a value less than or equal to current stock.")
        else:
            print("Total price:", q * 100)
            self.stock -= q
            print("Bikes remaining:", self.stock)

# Create an object of BikeShop with an initial stock
obj = BikeShop(100)

while True:
    uc = int(input('''
1. Display stock
2. Rent a bike
3. Exit
Enter your choice: '''))

    if uc == 1:
        obj.display_bike()
    elif uc == 2:
        n = int(input("Enter the quantity: "))
        obj.rent_for_bike(n)
    elif uc == 3:
        print("Thank you for visiting the Bike Shop!")
        break
    else:
        print("Invalid input. Please choose 1, 2, or 3.")
