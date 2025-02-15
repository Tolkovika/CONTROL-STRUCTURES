x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

if x == 0 and y == 0:
    print(f"Point P({x},{y}) is at the origin of the coordinate system.")
elif x == 0:
    print(f"Point P({x},{y}) lies on the Y-axis.")
elif y == 0:
    print(f"Point P({x},{y}) lies on the X-axis.")
elif x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system.")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system.")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system.")
else:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system.")