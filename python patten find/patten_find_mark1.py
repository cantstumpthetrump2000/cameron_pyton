
import random


data=""

head="123"

tail="789"

parrton_data="456646849861"


parrton=head+parrton_data+tail

lenth_data=len(parrton)

print("looking for",parrton)


#data maker

#v1
'''
random_noise=5

parrton_reption=2

for number_of_parrton in range(parrton_reption):
    data=data+parrton
    for q in range(random_noise):
        data=data+str(random.randint(1,10))
'''

#v2


random_noise=5

parrton_reption=2

aount_of_curruptiuon=2

for number_of_parrton in range(parrton_reption):
    data=data+parrton
    for q in range(random_noise):
        data=data+str(random.randint(1,10))
#curption

for _ in range(aount_of_curruptiuon):
    palce=random.randint(0,len(data))
    print("ramdom curruption at ",palce)
    data=data[0:palce]+str(random.randint(1,10))+data[palce:]


print(data)


#data find

#print("data in ",parrton in data)

head_match=[False,False,False]

looking_for_head=True




looking_for_tail=False

tail_match=[False,False,False]


retrved_data=""

for q in data:
    #print("Q",q)
    if looking_for_head==True:
        if q==head[0] and head_match[0]==False and  head_match[1]==False and head_match[2]==False:
            head_match[0]=True
            #print("1",q)
            #print(head_match)

        elif q==head[1] and head_match[0]==True and  head_match[1]==False and head_match[2]==False:
            head_match[1]=True
            #print("2",q)
            #print(head_match)

        elif q==head[2] and head_match[0]==True and  head_match[1]==True and head_match[2]==False:
            head_match[2]=True
            #print("3",q)
            print("posible start found")
            looking_for_head=False
            looking_for_tail=True
            retrved_data=""
            #print(head_match)

        else:
            #print("reset")
            head_match=[False,False,False]
            #print(head_match)

    if looking_for_tail ==True:
        retrved_data=retrved_data+q

        if q==tail[0] and tail_match[0]==False and  tail_match[1]==False and tail_match[2]==False:
            tail_match[0]=True
            #print("1",q)
            #print(head_match)

        elif q==tail[1] and tail_match[0]==True and  tail_match[1]==False and tail_match[2]==False:
            tail_match[1]=True
            #print("2",q)
            #print(head_match)

        elif q==tail[2] and tail_match[0]==True and  tail_match[1]==True and tail_match[2]==False:
            tail_match[2]=True
            #print("3",q)
            print("end found")
            print("the data is :")
            print(retrved_data[1:-len(tail)])
            print("did the code work")
            print(parrton_data==(retrved_data[1:-len(tail)]))
            exit()
            looking_for_head=True
            looking_for_tail=False
            #print(head_match)

        else:
            #print("reset")
            tail_match=[False,False,False]
            #print(head_match)


print("code not found")
