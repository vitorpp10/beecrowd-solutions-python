def palindromo(n):
    filter_n = filter(str.isalnum, n.lower())
    caracter_n = "".join(filter_n)


    palindromo_n = caracter_n == caracter_n[::-1]


    if palindromo_n == True:
        return 'SIM'
    else:
        return 'NAO'
   
n = str(input())
print(palindromo(n))