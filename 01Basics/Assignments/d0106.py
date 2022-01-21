# Programming Series - Python3.0
# Day01: 006

# Properties of the circle
print("Properties of the circle")
PI = 3.14
R = float(input("Enter Radius (cm) : "))
dia = 2 * R
peri = 2 * PI * R
area = PI * R * R
print("Radius : {:.2f} cm Diameter : {:.2f} cm, Perimeter : {:.2f} cm, \
    Area : {} sq.cm".format(R,dia,peri,area))
