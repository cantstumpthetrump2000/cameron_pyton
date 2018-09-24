#problem
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.


def addTwoNumbers( l1, l2):
    reslut=[]
    add_to_the_end=0
    lenth_of_l1=len(l1)
    lenth_of_l2=len(l2)

    if lenth_of_l1==lenth_of_l2:
        case=1
        how_meny_time_to_loop=lenth_of_l1

    if lenth_of_l1>lenth_of_l2:
        case=2
        how_meny_time_to_loop=lenth_of_l2

    if lenth_of_l1<lenth_of_l2:
        case=3
        how_meny_time_to_loop=lenth_of_l1


    for loop_count in range(how_meny_time_to_loop):

        total_temp=l1[loop_count]+l2[loop_count]
        if total_temp>9:
            if   ((loop_count+1)<lenth_of_l1):
                l1[loop_count+1]=l1[loop_count+1]+1

            elif  (loop_count+1<lenth_of_l2):
                l2[loop_count+1]=l2[loop_count+1]+1


            elif(loop_count+2>lenth_of_l2) and (loop_count+2>lenth_of_l1):
                add_to_the_end=1

            total_temp=total_temp-10
            reslut.append(total_temp)
        elif total_temp<10:
            reslut.append(total_temp)



    if case==1:
        pass
    if case==2:
        for q in l1[lenth_of_l2:]:
            reslut.append(q)


    if case==3:
        for q in l2[lenth_of_l1:]:
            reslut.append(q)

    if add_to_the_end!=0:
        reslut.append(add_to_the_end)

    return(reslut)


print(addTwoNumbers([9,9,9],[1,2,3]))
