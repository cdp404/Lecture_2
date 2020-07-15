def factorial_recursion(n):
    if n <=1:
        return 1
    else:
        return n*factorial_recursion(n-1)

n = 4
result = factorial_recursion(n)
print('{} 팩토리얼은 {} 입니다.'.format(n,result))