












def intersect(p1,p2,r):
    x1,y1=p1
    x2,y2=p2

    direction=[1,1]


    l3=((x1-x2)**2+(y1-y2)**2)**0.5
    l3=l3/2
    print("l3",l3)
    l4=(r**2-l3**2)**0.5
    print("l4",l4)
    x1=x1+l3*direction[0]
    y1=y1+l4*direction[1]
    print("point is ",x1,y1)

#intersect((0,0),(5,5),10)
intersect((0,0),(6,-4),10)
