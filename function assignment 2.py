def even_odd():
    user_input=int (input("Enter a number: "))
    if user_input % 2==0:
        print(f"{user_input} IS EVEN")
    elif user_input % 2!=0:
        print(f"{user_input} IS ODD")
even_odd()
