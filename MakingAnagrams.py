def number_needed(a, b):
    count = 0
    for i in range (97, 123):
        ct_a = a.count(chr(i))
        ct_b = b.count(chr(i))
        count += abs(ct_a - ct_b)
    return count
    
a = input().strip()
b = input().strip()

print(number_needed(a, b))
