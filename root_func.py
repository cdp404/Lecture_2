def get_root(a,b,c):
    r1 = (-b + (b**2-4*a*c)**0.5) / (2*a)
    r2 = (-b - (b**2-4*a*c)**0.5) / (2*a)
    return r1 , r2

root = get_root(1,5,6)
print(root)

#각각을 따로 따로 반환 받는법
root1, root2 = get_root(1,5,6)
print('r1값은',root1)
print('r2값은',root2)

root_1 = get_root(1,c=6,b=5)
print(root_1)