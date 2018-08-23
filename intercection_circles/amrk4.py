









from math import cos,sin,tan,radians,sqrt
def meeting_point(circle1,circle2):
    x0,y0,r0=circle1
    x1,y1,r1=circle2

    d= ((x0-x1)**2+(y0-y1)**2)**0.5
    y_d=0.5*(r0+r1-d)

    x_d=(r1**2)-(y_d**5)
    x_d=x_d**0.5
    return(y_d,x_d)



def circle_intersection(circle1, circle2):
    x1,y1,r1 = circle1
    x2,y2,r2 = circle2
    # http://stackoverflow.com/a/3349134/798588
    dx,dy = x2-x1,y2-y1
    d = sqrt(dx*dx+dy*dy)
    if d > r1+r2:
        #print ("#1")
        return False # no solutions, the circles are separate
    if d < abs(r1-r2):
        #print ("#2")
        return False # no solutions because one circle is contained within the other
    if d == 0 and r1 == r2:
        #print ("#3")
        return False # circles are coincident and there are an infinite number of solutions

    a = (r1*r1-r2*r2+d*d)/(2*d)
    h = sqrt(r1*r1-a*a)
    xm = x1 + a*dx/d
    ym = y1 + a*dy/d
    xs1 = xm + h*dy/d
    xs2 = xm - h*dy/d
    ys1 = ym - h*dx/d
    ys2 = ym + h*dx/d

    xs1=round(xs1)
    ys1=round(ys1)

    xs2=round(xs2)
    ys2=round(ys2)
    return (xs1,ys1),(xs2,ys2)


def point_make(lenth):
    simple_angle=radians(30)
    point1_x=0.5*lenth*-1
    point1_y=-0.5*lenth*tan(simple_angle)
    #print("point1",point1_x,point1_y)

    point2_x=0.5*lenth
    point2_y=-0.5*lenth*tan(simple_angle)
    #print("point2",point2_x,point2_y)

    point3_x=0
    point3_y=point2_y**2+(0.5*lenth)**2
    point3_y=point3_y**0.5
    #print("point3",point3_x,point3_y)

    return((point1_x,point1_y),(point2_x,point2_y),(point3_x,point3_y))



def translat(angle,displament):

    angle=radians(angle)
    x,y=displament
    x1=x*cos(angle)-y*sin(angle)
    y1=y*cos(angle)+x*sin(angle)

    return(x1,y1)


#point1,point2,point3=(point_make(8))

#print(translat(270,(5,5)))


A=0,-17.321,15
B=10,0,34.329
C=-10,0,33.201

count=0

point_match=[]

#print("test start")
#print(circle_intersection(point2,point3))
#print("etast end")

inersection_point=[]




inersection_point.append(circle_intersection(A,B))
inersection_point.append(circle_intersection(A,C))
inersection_point.append(circle_intersection(B,C))


for q in inersection_point:
    for w in q:
        marker=True
        for t in inersection_point:

            if not (w in t):
                print("W no in t ")
                marker=False
            if q==t:
                print("comparing same point")
                #marker=False
            print("q",q)
            print("w",w)
            print("T",t)
            print("")
        if marker==True:
            print("point found",w)
            exit()


print("ggg")
#print(circle_intersection((0,-17.321,15),(10,0,34.329)))
