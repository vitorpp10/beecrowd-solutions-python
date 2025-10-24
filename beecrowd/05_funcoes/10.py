def menor_divi(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i
       
n = int(input())
print(menor_divi(n))