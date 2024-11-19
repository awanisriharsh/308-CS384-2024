def unitary_sum_of_digits(n):
    while n >= 10:  
        sum_of_digits = 0
        temp = n
        while temp > 0:  
            digit = temp % 10
            sum_of_digits += digit
            temp //= 10
        n = sum_of_digits 
    return n


num = int(input("Enter an integer: "))
result = unitary_sum_of_digits(num)
print(f"The Unitary Sum of Digits of {num} is: {result}")
