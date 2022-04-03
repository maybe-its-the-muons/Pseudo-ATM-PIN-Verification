#Sample coursework from graduate program. 

#Function to assess whether account balance is greater than 0 by random
def account_balance():
    #Generating random account balance between 0 and 100
    import random
    account_balance = random.randrange(0, 2)
    
    if account_balance != 0:
        print("Your PIN has been rejected.  Please contact customer service.")
    else:
        print("Your PIN has been rejected and your account has been closed with a $0.00 balance.\nFor further assistance please contact customer service.")
                                       

    
#Function to assess whether PIN is accepted or denied by random
def pin_validation():
    #Generating random PIN validation where choice = accepted or denied
    from random import choice
    pin_accepted = choice(['accepted', 'denied'])
    
    #If accepted, reach main screeen
    if pin_accepted == 'accepted':
        print("Your PIN was accepted. Welcome to the main screen.")
    #Else follow denied steps
    else:
        denied_pin()

def denied_pin():
    count = 0
    
    while count <= 2:
        count = count + 1
        pin_retry = input("Your PIN was denied.  Please retry by entering your PIN: ")
        from random import choice
        pin_redo = choice(['accepted', 'denied'])
        
        if pin_redo == 'accepted':
            print("Your PIN was accepted. Welcome to the main screen.")
            break
            
    if count > 2 and pin_redo == 'denied':
        account_balance()


#Main function to start receiving input and flow to other dependent functions 
def main():
    pin = input("Thank you for choosing our ATM service\nPlease insert your card and enter your PIN to get started: ")
    pin_validation()
        
