
import time


def print_lento(texto, delay=0.05):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


day1 = input()  
start = input()  
day2 = input()  
end = input()  


day1_f = int(day1.split()[1])
day2_f = int(day2.split()[1])


start = start.replace(":", "")
end = end.replace(":", "")


start_h = int(start[0:2]) 
start_m = int(start[2:4])  
start_s = int(start[4:6])  

end_h = int(end[0:2])  
end_m = int(end[2:4])  
end_s = int(end[4:6])  


seconds_start = (day1_f - 1) * 86400 + start_h * 3600 + start_m * 60 + start_s
seconds_final = (day2_f - 1) * 86400 + end_h * 3600 + end_m * 60 + end_s


duration_seconds = seconds_final - seconds_start


days = duration_seconds // 86400 
rest_hours = duration_seconds % 86400  
hours = rest_hours // 3600  
rest_minutes = rest_hours % 3600  
minutes = rest_minutes // 60  
seconds = rest_minutes % 60  


print_lento(f'{days} dia(s)')
print_lento(f'{hours} hora(s)')
print_lento(f'{minutes} minuto(s)')
print_lento(f'{seconds} segundo(s)')

