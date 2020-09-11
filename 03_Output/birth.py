year = 2000
month = 10
day = 15
hour = 11
minute = 18
second = 13

print('날짜, 시간 출력')
print(year, month, day, sep='/')
print(hour, minute, second, sep=':')

# 입력 받은 출생 날짜, 시간 출력
b_year, b_month, b_day = map(int, input('출생 날짜 입력(ex. 2000 10 10) : ').split())
b_hour, b_minute, b_second = map(int, input('출생 시간 입력(ex. 16 10 25) : ').split())
print('\n\n출생 날짜 : %d/%02d/%02d' % (b_year, b_month, b_day))
print('\n출생 시간 : %02d:%02d:%02d' % (b_hour, b_minute, b_second))
