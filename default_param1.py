def div(a,b = 2):
    return a/b



print('div(4) = ', div(4))
#위치인자로 넣은 결과
print('div(200,5) =',div(200,5))

#위치인자와 키워드인자를 혼용
print('div(200,b=5) =',div(200,b=5))
print('div(a=200,b=5) =',div(a=200,b=5))
print('div(b=5,a=200) =',div(b=5,a=200))