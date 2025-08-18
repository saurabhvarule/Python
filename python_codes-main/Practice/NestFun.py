
def funChoice(num):

    def isPrime():

        count = 0
        i = 1

        while(i <= num//2):
            if(num % i == 0):
                count += 1
            i += 1
        if(count == 1):
            print(num, " is prime number.")
        else:
            print(num, " is not a prime number.")

    
    def isPalindrom():

        rev = revNum()

        if(num == rev):
                print(num, " is palindrom number.")
        else:
                print(num, " is not  palindrom number.")

    def isArmstrong():

        temp = num
        i = 0
        val = 0

        while(temp > 0):
            
            val = val + (temp % 10) ** len(str(num))
            temp = temp // 10

        if(val == num):
                print(num, " is Armstrong number.")
        else:
                print(num, " is not  Armstrong number.")
    
    
    def revNum():

        temp = num
        rev = 0
        
        while(temp > 0):

            rev = rev * 10 + (temp % 10)
            temp = temp // 10

        return rev

    return isPrime, isPalindrom, isArmstrong, revNum


num = int(input("Please Enter a Number : "))
check = 1

while(check == 1):

    print("\nEnter your choice : \n")

    print("1. Check Number is Prime.")
    print("2. Check Number is Palindrom.")
    print("3. Check Number is Armstrong.")
    print("4. Reverse The Given Number.")
    print("0. Exit\n")

    choice = int(input("Enter your choice : "))
    print()

    ch = funChoice(num)

    if(choice == 0):
        check = 0

    elif(choice == 1):
        ch[choice - 1]()

    elif(choice == 2):
        ch[choice - 1]()

    elif(choice == 3):
        ch[choice - 1]()

    elif(choice == 4):
        print(ch[choice - 1]())

    else:
        print("Please enter the valid choice..!")


