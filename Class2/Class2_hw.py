
def is_prime(n):
    if n ==1:
        return False 

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  

    return True  

user_input = int(input("Enter a number: "))
result = is_prime(user_input)

if result:
    print(f"{user_input} 是否為質數: True")
else:
    print(f"{user_input} 是否為質數: False")

print("O(n)")