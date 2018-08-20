



def intersect(x1,y1,r1,x2,y2,r2):


    dx=x1-x2
    dy=y1-y2

    d=((dx**2)+(dy**2))**0.5


    #/* Check for solvability.
    if (d > (r1 + r2)):

        # no solution. circles do not intersect. */
        print("circle dont touch")

    elif(d < abs(r1 - r2)):

        #/* no solution. one circle is contained in the other */
        print("cirlce are contoant")

    else:
        print("can find points")
        print("d",d)
        print("r1",r1)
        print("r2",r2)

        a = (((r1**2) - (r2**2) + (d**2)) / (2 * d))

        print("a ",a)
        x3 = x1 + (dx * a/d)
        y3 = y1 + (dy * a/d)

        h=((r1*r1)-(a*a))**0.5

        rx = -dy * (h/d)
        ry = dx * (h/d)


        xi = x2 + rx
        xi_prime = x2 - rx
        yi = y2 + ry
        yi_prime = y2 - ry


        print(xi,yi,"\n",xi_prime,yi_prime)


intersect(0,0,50,50,0,55)

#intersect(-1.0, -1.0, 1.5, 1.0, 1.0, 2.0)
#intersect(1.0, -1.0, 1.5, -1.0, 1.0, 2.0)
#intersect(-1.0, 1.0, 1.5, 1.0, -1.0, 2.0)
#intersect(1.0, 1.0, 1.5, -1.0, -1.0, 2.0)
