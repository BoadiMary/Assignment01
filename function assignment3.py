def prime_numbers():
    def is_prime(num):
        if num<2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num % i==0:
                return False
        return True
    num_1=int(input("Enter first number "))
    num_2=int(input("Enter last number "))    
    count=0
    for num in range(num_1,num_2+1):
        if is_prime(num):
            count+=1
    print(f"There are {count} prime numbers between {num_1} and {num_2}")  
prime_numbers()  
        
            