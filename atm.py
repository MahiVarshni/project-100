class Atm(object):
    
    

    def __init__(self,card_number,pin_number):
        self.card_number=card_number
        self.pin_number=pin_number
        self.balance =75000
    
    def balanceEnquiry(self):
        print("Your balance is "+ str(self.balance))

    def cashwithdrawal(self,amount):
        self.balance=self.balance-int(amount)
        print("you have withdrawn amount"+str(amount)+".your remaining balance is"+str(self.balance))
    
def main():
    card_number=input("enter card number:-")
    pin_number=input("enter pin number:-")

    atmcard =  Atm(card_number ,pin_number)
    
    activity=input("choose activity(W- withdrawal or B-balanceEnquiry)")
    if (activity == "B"):
        atmcard.balanceEnquiry()

    elif (activity == "W"):
        withdrawlamount = input ("enter withdrawal amount")
        atmcard.cashwithdrawal(withdrawlamount)
        print ("your current balance is"+ str(atmcard.balance))
    
    else:
        print("enter a valid input")

main()