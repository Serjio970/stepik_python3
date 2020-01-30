g = str(input())
if g == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    d = (a+b+c)/2
    print((d*(d-a)*(d-b)*(d-c))**0.5)
elif g == "прямоугольник":
    a = int(input())
    b = int(input())
    print(a*b)
elif g == "круг":
    a = int(input())
    print(3.14 * (a**2))
