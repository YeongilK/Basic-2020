# 국어, 영어 , 수학, 과학 점수 입력
korean , english, math, science = map(int, input('국, 영, 수, 과 4과목의 점수 입력(공백을 기준으로 분리) : ').split())

print('국어:%d / 영어:%d / 수학:%d / 과학:%d' % (korean, english, math, science))
print(korean >= 90 and english > 80 and math > 85 and science >= 80, '[True:합격 / False:불합격]')
