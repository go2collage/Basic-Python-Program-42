# Python function

# check number is prime or not

def prime_or_not(num):
    for i in range(2, num):
        if num % i == 0:
            return (f"{num} is not Prime number.")
    
    return (f"{num} is Prime number.")
    


num = int(input("Enter a Integer number: "))

print("The given number is: ", num)

print(prime_or_not(num))            # call by value 

# Thanks for Watching
