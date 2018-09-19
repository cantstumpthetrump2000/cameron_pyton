nums=[2,7,11,15]



target=9


count1=-1
count2=-1

for loop1 in nums:
    count2=-1
    count1=count1+1
    for loop2 in nums:
        count2=count2+1
        if loop1+loop2==target:
            print((count1,count2))
