def CountSize(path = str(input())):
    import os
    return os.path.getsize(path)
print(CountSize())
