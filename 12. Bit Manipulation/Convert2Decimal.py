def convert2Decimal(num : str) -> int:
    decimal_number = 0
    power = 0
    index = len(num) - 1
    while index >= 0:
        digit = int(num[index]) * (2**power)
        decimal_number += digit
        index -=1
        power += 1
    return decimal_number
num = "1101"
print(convert2Decimal(num))