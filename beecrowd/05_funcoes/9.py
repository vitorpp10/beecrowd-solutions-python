def media_pond(notes, kg):
    sum_kg = sum(kg)  
    mult_notes = sum(n * k for n, k in zip(notes, kg))  
    return mult_notes / sum_kg  


notes = list(map(float, input().split()))  
kg = list(map(float, input().split()))  
print(f'{media_pond(notes, kg):.1f}')  