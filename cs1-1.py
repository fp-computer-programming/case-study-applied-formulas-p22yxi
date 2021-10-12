# Author Yongdong Xi (Oct 12)

x1 = float(input("what is the x coordinates of point A"))
y1 = float(input("what is the y coordinates of point A"))
x2 = float(input("what is the x coordinates of point B"))
y2 = float(input("what is the y coordinates of point B"))

anwser = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1/2)
print(anwser)
