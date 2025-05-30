myFName = input("First Name?")
myLName = input("Last Name?")
myZip = input("Zip Code?")
myAddress = input("Address?")
myCity = input("City?")
myState = input("State?")
myContact = myFName + "\t" + myLName + "\t" + myAddress + "\t" + myCity + "\t" + myState + "\t" + myZip
print(myContact)
user = input("Is this correct? [y/n]")
if user == "Y" or "y":
    myfile = open("myContactList.txt", "a")
    myfile.write("\n" + myContact)
    myfile.close
if user == "N" or "n":
    print("Please try again")
    import time
    time.sleep(3)
    import myAddContacts