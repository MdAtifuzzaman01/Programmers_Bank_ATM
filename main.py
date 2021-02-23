print("Welcome to the Bank of Programmers")
restart = "Y"
chances = 3
balance = 1000.67
while chances >= 0 :
    pin = int(input("Enter your pin"))
    if pin ==(1234):
        print("You entered your pin correctly\n")
        while restart not in ('n' , "N", "No", "NO"):
            print("Please press 1 for your balance \n")
            print("Please press 2 to make a withdraw\n")
            print("Please press 3 to pay in \n")
            print("Please press 4 to return card \n")
            option = int(input("What would you like to choose?"))
            if option == 1:
                print("Your balance is A$  " , balance , '\n')
                restart = input("Would you like to go back?")
                if restart in ('n' , 'No' , 'N' , "NO"):
                    print("Thank you")
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input("How much would you like to withdraw ? \n A$10, A$20 ,  A$30"))
                if withdrawl in  [10,20,30,40,50,60,80,100]:
                    balance = balance - withdrawl
                    print("\nYour balance is  now  A$" , balance)
                    restart - input("Woulf you  like to go back?")
                    if restart in ('n' , 'No' , 'N' , "NO"):
                        print("Thank you")
                        break
                elif withdrawl != [10,20,30,40,50,60,70,80,100]:
                    print('invalid Amount , Please re-try in \n')

                    restart = ('y')
                elif withdrawl  == 1:
                    withdrawl = float(input("Please enter your desired your amount : "))
            elif option == 3:
                Pay_in = float(input('How much would you like to pay in \n'))
                balance = balance + Pay_in
                print("\nYour balance is  now  A$" , balance)
                restart = input("Would you like to go back?")
                if restart in ('n' , 'No' , 'N' , "NO"):
                    break
            elif option == 4:
                print("Please wait whilst your card is returned...")
                print('Thanks for your service')
            else:
                print("Enter a correct number . \n")
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chanced = chances - 1
        if chances == 0:
            print('\n No more tries')
            break


                    
