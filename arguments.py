def fractorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fractorial(x-1)
print("the fractorial of 0:",fractorial(0))
print("the fractorial of 1:",fractorial(1))
print("the fractorial of 2:",fractorial(4))
print("the fractorial of 5:",fractorial(5))
print("the fractorial of 10:",fractorial(10))