




'''
matrix_1=[
[1,2,3],
[4,5,6],
]


matrix_2=[
[7,8],
[9,10],
[11,12],
]

'''


matrix_1=[
[3,4,2],
]


matrix_2=[
[13,9,7,15],
[8,7,4,6],
[6,4,0,3],
]











matrix_3=[
[0,0,0,0],
]



print("")
#math part



returl_array=[]



#or1

for q in range(len(matrix_1)):
    for w in range(len(matrix_2[0])):
        total=0
        for m in range(len(matrix_1[0])):
            #print(matrix_1[q][m])
            #print(matrix_2[m][w])
            total=total+(matrix_2[m][w]*matrix_1[q][m])

        matrix_3[q][w]=total



for q in matrix_3:
    print(q)