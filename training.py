'''
1015 beecrowd

import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
distance_final = math.sqrt(distance)

print(f'{distance_final:.4f}')
'''

'''
1016 beecrowd

distance = int(input())

temp_min = distance * 2

print(f'{temp_min} minutos')
'''

'''
1017 beecrowd

temp_work = int(input())
velocity_media = int(input())

distance = temp_work * velocity_media
necessary_L = distance / 12

print(f'{necessary_L:.3f}')
'''

'''
1018 beecrowd

value = int(input())

quanty1 = value // 100
rest1 = value % 100

quanty2 = rest1 // 50
rest2 = rest1 % 50

quanty3 = rest2 // 20
rest3 = rest2 % 20

quanty4 = rest3 // 10
rest4 = rest3 % 10

quanty5 = rest4 // 5
rest5 = rest4 % 5

quanty6 = rest5 // 2
rest6 = rest5 % 2

quanty7 = rest6 // 1
rest7 = rest6 % 1

print(f'{value}')
print(f'{quanty1} nota(s) de R$ 100,00')
print(f'{quanty2} nota(s) de R$ 50,00')
print(f'{quanty3} nota(s) de R$ 20,00')
print(f'{quanty4} nota(s) de R$ 10,00')
print(f'{quanty5} nota(s) de R$ 5,00')
print(f'{quanty6} nota(s) de R$ 2,00')
print(f'{quanty7} nota(s) de R$ 1,00')
'''

'''
1019 beecrowd

value = int(input())

hours = value // 3600
rest_before_hours = value % 3600
minutes = rest_before_hours // 60
seconds = rest_before_hours % 60

print(f'{hours}:{minutes}:{seconds}')
'''

'''
1020 beecrowd

value = int(input())

year = value // 365
rest_of_year = value % 365
month = rest_of_year // 30
days = rest_of_year % 30

print(f'{year} ano(s)')
print(f'{month} mes(es)')
print(f'{days} dia(s)')
'''

'''
1021 beecrowd

value = float(input())
value_in_cents = int(value * 100)

# notas:

quanty1 = value_in_cents // 10000
rest1 = value_in_cents % 10000

quanty2 = rest1 // 5000
rest2 = rest1 % 5000

quanty3 = rest2 // 2000
rest3 = rest2 % 2000

quanty4 = rest3 // 1000
rest4 = rest3 % 1000

quanty5 = rest4 // 500
rest5 = rest4 % 500

quanty6 = rest5 // 200
rest6 = rest5 % 200

# moedas:

quanty7 = rest6 // 100
rest7 = rest6 % 100

quanty8 = rest7 // 50
rest8 = rest7 % 50

quanty9 = rest8 // 25
rest9 = rest8 % 25

quanty10 = rest9 // 10
rest10 = rest9 % 10

quanty11 = rest10 // 5
rest11 = rest10 % 5

quanty12 = rest11 // 1
rest12 = rest11 % 1

print('NOTAS:')
print(f'{quanty1:.0f} nota(s) de R$ 100.00')
print(f'{quanty2:.0f} nota(s) de R$ 50.00')
print(f'{quanty3:.0f} nota(s) de R$ 20.00')
print(f'{quanty4:.0f} nota(s) de R$ 10.00')
print(f'{quanty5:.0f} nota(s) de R$ 5.00')
print(f'{quanty6:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{quanty7:.0f} moeda(s) de R$ 1.00')
print(f'{quanty8:.0f} moeda(s) de R$ 0.50')
print(f'{quanty9:.0f} moeda(s) de R$ 0.25')
print(f'{quanty10:.0f} moeda(s) de R$ 0.10')
print(f'{quanty11:.0f} moeda(s) de R$ 0.05')
print(f'{quanty12:.0f} moeda(s) de R$ 0.01')
'''