import sys

ellipse_file=sys.argv[1]
points_file=sys.argv[2]

def points_placement(ellipse, points):
    ellipse_data=[]
    points_data=[]
    with open(ellipse, 'r', encoding='utf-8') as file:
        for line in file:
            ellipse_data.append([int(x) for x in line.strip().split()])

    with open(points, 'r', encoding='utf-8') as file:
        for line in file:
            points_data.append([int(x) for x in line.strip().split()])

    x0=ellipse_data[0][0]
    y0=ellipse_data[0][1]
    a=ellipse_data[1][0]
    b=ellipse_data[1][1]

    for point in points_data:
        e=((point[0] - x0)**2)/(a**2) + (( point[1] - y0)**2)/(b**2)
        if e < 1:
            print(1)
        elif e == 1:
            print(0)
        elif e > 1:
            print(2)
    return

points_placement(ellipse_file, points_file)