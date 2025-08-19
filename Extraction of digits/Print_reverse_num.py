# n = 5873 print one by one (reverse)

num = 5873
while num > 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10
    
