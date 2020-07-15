def print_sum():
    global a,b
    a = 100
    b = 200
    result = a + b
    print('\n print_sum() 내부 : ',a, '과',b,'의 합은',result,'입니다.')


a = 10
b = 20
print_sum()
result = a + b
print('\n print_sum() 외부 : {} 과 {} 의 합은 {} 입니다.'.format(a,b,result) )