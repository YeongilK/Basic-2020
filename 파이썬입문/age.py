import datetime

now_year = datetime.datetime.now().year
now_month = datetime.datetime.now().month
now_day = datetime.datetime.now().day

birth_year, birth_month, birth_day = map(int, input('출생날짜 입력(ex. 2020.8.28) : ').split('.'))

if now_month > birth_month:                     # 현재월 > 생월(생일 지남)
    age = now_year - birth_year    
elif now_month < birth_month:                   # 현재월 < 생월(생일 안지남)
    age = now_year - birth_year - 1
else:                                           # 현재월 = 생월
    if now_day < birth_day:                       # 현재일 < 생일(생일 안지남)
        age = now_year - birth_year - 1   
    else:                                         # 현재일 >= 생일(생일 지남)
        age = now_year - birth_year
    
print('현재날짜 : %d-%d-%d' % (now_year, now_month, now_day))
print('출생날짜 : %d-%d-%d' % (birth_year, birth_month, birth_day))
    
print('사용자의 나이 : 만 %d세' % age)