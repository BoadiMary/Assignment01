def odd_nums_in_range():
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    print(f"\odd numbers between {start} and {end}:")
    for number in range(start , end + 1):
        if number % 2!= 0:
            print(number)

def prime_num_in_range():
    start = int(input("Enter a number( start of range): "))
    end = int(input("Enter a number (end of range): "))
    print(f"\nprime numbers between {start} and {end}:")
    for num in range(start, end + 1): 
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num)

def even_numbers_in_range():
    start = int(input("Enter start of range:"))
    end = int(input("Enter end of range:"))
    print(f"\neven numbers between {start} and {end}:")
    for even in range (start, end , + 1):
        if even % 2 == 0:
            print(even)

def multiply():
    result=1
    while True:
        user_input=input("Enter a number to multiply(or press ENTER to continue): ")
        if user_input== "":
            break
        result*= int(user_input)
        print("the product is",result)
       
def main():
    while True:
        print("options")
        print("1. find odd numbers in range")
        print("2. find prime numbers in range")
        print("3. find even numbers in range")
        print("4. find mulplication")
        choice=input("Enter you choice: ")
        if choice=="1":
            odd_nums_in_range()
        elif choice=="2":
            prime_num_in_range()
        elif choice=="3":
            even_numbers_in_range()
        elif choice=="4":
            multiply()
        elif choice=="5":
            break
        else:
            print("invalid choice. please enter a number between 1 and 4")
if __name__=="__main__":
    main()           
        




            
