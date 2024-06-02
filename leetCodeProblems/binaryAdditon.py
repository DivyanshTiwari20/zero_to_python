def addBinary(a: str, b: str) -> str:
    result = ""
    i, j = len(a) - 1, len(b) - 1
    carry = 0

    while i >= 0 or j >= 0 or carry:
        digitA = int(a[i]) if i >= 0 else 0
        digitB = int(b[j]) if j >= 0 else 0

        total = digitA + digitB + carry
        result = str(total % 2) + result
        carry = total // 2

        i -= 1
        j -= 1

    return result

a = "11"
b = "1"

print(addBinary(a, b)) 
