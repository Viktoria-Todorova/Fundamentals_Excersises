from math import floor
def longer_line(X1,Y1,X2,Y2,X3,Y3,X4,Y4):
    line_1 = (X1 - X2) ** 2 + (Y1 - Y2) ** 2
    line_2 = (X3 - X4) ** 2 + (Y3 - Y4) ** 2
    if line_1 >= line_2:
        # Check which point of the first line is closer to the origin
        if (X1 ** 2 + Y1 ** 2) <= (X2 ** 2 + Y2 ** 2):
            return f"({floor(X1)}, {floor(Y1)})({floor(X2)}, {floor(Y2)})"
        else:
            return f"({floor(X2)}, {floor(Y2)})({floor(X1)}, {floor(Y1)})"
    else:
        # Check which point of the second line is closer to the origin
        if (X3 ** 2 + Y3 ** 2) <= (X4 ** 2 + Y4 ** 2):
            return f"({floor(X3)}, {floor(Y3)})({floor(X4)}, {floor(Y4)})"
        else:
            return f"({floor(X4)}, {floor(Y4)})({floor(X3)}, {floor(Y3)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
print(longer_line(x1,y1,x2,y2,x3,y3,x4,y4))
