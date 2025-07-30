def swap(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    x, y = y, x
    print("Swapped values:", x, y)

print(swap("Apple", 10))
swap(9, 17)