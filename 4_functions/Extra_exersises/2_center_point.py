from math import floor

def center_poit(X1, Y1, X2, Y2):
    dist_1 = X1 ** 2 + Y1 ** 2
    dist_2 = X2 ** 2 + Y2 ** 2

    if dist_1 <= dist_2:
        return f"({floor(X1)}, {floor(Y1)})"
    else:
        return f"({floor(X2)}, {floor(Y2)})"

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(center_poit(x1, y1, x2, y2))