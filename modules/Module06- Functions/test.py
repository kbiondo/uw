x = None
y = None
z = None
x1 = None
y1 = None
z1 = None
x2 = None
y2 = None
z2 = None


def addValues(val1 = 5, val2 = 10):
    sumVal = val1 + val2
    minVal = val1 - val2
    prodVal = val2 * val1
    quoVal = val1 / val2
    return val1,val2,sumVal,minVal,prodVal,quoVal

x = float(input("get me fuck"))
y = float(input("get me fuck"))
x1, y1, z1, x2, y2, z2 = addValues(x,y)

print("The Sum of %.2f and %.2f is %.2f" % (x, y, z1))
print("The min of %.2f and %.2f is %.2f" % (x, y, x2))
print("The prod of %.2f and %.2f is %.2f" % (x, y, y2))
print("The quo of %.2f and %.2f is %.2f" % (x, y, z2))
