def print_star(n=1):
    for _ in range(n):
        print('********************************')


print_star()
print("\n다음은 인자값으로 위치 인자로 3을 넣어 줬을 때\n")
print_star(3)
print("\n다음은 인자값으로 키워드 인자로 3을 넣어 줬을 때\n")
print_star(n = 4)