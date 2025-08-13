def multiply():
    result=1
    while True:
        user_input=input("Enter a number(or press ENTER to quit): ")
        if user_input== "":
            break
        result*= int(user_input)
        print("the product is",result)
multiply()        
