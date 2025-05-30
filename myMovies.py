myMovies = ["Dune", "Spiderman", "Batman", "Star Wars", "Spiderman 2", "Spiderman 3", "Top Gun", "Thor","Thor: Rangorok","Dune 2"]
myPrices = [9.99, 8.99, 7.99, 6.99, 5.99, 8.50, 7.99, 5.99, 6.99, 10.99]
myZips = ["19530", "19604", "19602", "19605", "19565"]
myShipPrices = [2.00, 4.00, 7.00, 10.00, 0]
myDiscount = 0.025
myTax = 0.06

i = 0
print("Available movies:")
for i in range(len(myMovies)):
    print(f"{i+1}: {myMovies[i]} - ${myPrices[i]:.2f}")

mySelectedMovies = []
myRunningTotalPrice = 0.0

while True:

    myPick = input("Select a Movie: ")
    if myPick.lower() == "done":
        break
    if myPick.isdigit():
        myPick = int(myPick)
        if 1 <= myPick <= len(myMovies):
            mySelectedMovie = myMovies[myPick - 1]
            mySelectedPrice = myPrices[myPick - 1]
            mySelectedMovies.append((mySelectedMovies, mySelectedPrice))
            myRunningTotalPrice += mySelectedPrice
            print(f"Added {myPick} for ${mySelectedPrice:.2f} to your shopping cart")
            print(f"Current Total: {myRunningTotalPrice}")
            

        else:
            print("\nInvalid selection, please try again")
    else:
        print("\nInvalid input. Please try again")

myTotalDiscount = myRunningTotalPrice * myDiscount
myMemDiscount = input("Are you a member? (Y/N)")
if myMemDiscount.upper() == "Y":
    myRunningTotalPrice -= myTotalDiscount
else: myTotalDiscount = 0

i = 0
print("Zip Codes:")
for i in range(len(myZips)):
    print(f"{i+1}: {myZips[i]} - ${myShipPrices[i]:.2f}")


myCode = input("What is your Zip Code?")
if myCode.isdigit():
    myCode = int(myCode)
    if 1 <= myCode <= len(myZips):
        mySelectedZip = myZips[myCode - 1]
        mySelectedShipPrice = myShipPrices[myCode - 1]
        myRunningTotalPrice += mySelectedShipPrice
        

    else:
        print("\nInvalid selection, please try again")
else:
    print("\nInvalid input. Please try again")

myTotalTax = myRunningTotalPrice * myTax
myTotalPrice = myRunningTotalPrice + myTotalTax

print(f"Shipping Cost: ${mySelectedShipPrice:.2f}")
print(f"Membership Discount: ${myTotalDiscount:.2f}")
print(f"Subtotal: ${myRunningTotalPrice:.2f}")
print(f"Sales Tax: ${myTotalTax:.2f}")
print(f"Your total is ${myTotalPrice:.2f}")
        