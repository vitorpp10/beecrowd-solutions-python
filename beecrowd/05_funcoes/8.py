def vogal(n):
    vogal = {'a', 'e', 'i', 'o', 'u'}
    count = sum(1 for char in n if char in vogal)
    return count
       
n = str(input())
print(vogal(n))