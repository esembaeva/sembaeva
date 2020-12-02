def f(x = input()):
    l = [str(i) for i in x]
    l.insert (l.index('6'), '9')
    l.remove ('6')
    k = "".join(l)
    return k
print(f())
