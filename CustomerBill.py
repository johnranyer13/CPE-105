def Restaurant_bill():

# Get the value of the bill from the user.
# This is the total amount, including tax, and tip.
    print ("What was the total amount of the bill?")
    bill = int(input("Amount: "))
    
# Get the value of how much did you recieved.
    print ("How much did the customer gave?")
    Pamount = int(input("Amount: "))

# Calculate and display the change.
    change = Pamount - bill

# Calculate and display the tax.  The tax here is based
# on the whole bill
    tax = 10 * bill / 100

# Calculate and display the tip.  The tip here is based
# on the whole bill
    tip = 15 * bill / 100

# Calculate the product/service without tax and tip
    Oprice = bill - (tax + tip)
    
    print ("Net bill:   ",(Oprice))
    print ("tax:        ",(tax))
    print ("tip:        ",(tip))
    print ("Gross bill: ",(bill))
    print ("change:     ",(change))

Restaurant_bill()
