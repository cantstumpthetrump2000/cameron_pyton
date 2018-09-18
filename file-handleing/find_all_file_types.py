import os




file_in_dir=os.listdir()

vidio_files=[]
for q in file_in_dir:

    if len(q.split("."))>1:

        if (q.split(".")[len(q.split("."))-1])=="mp4":
            print(q)
            print ("vido ","\n")
            vidio_files.append(q)
            os.rename(q,"E:/New folder/teast/"+q)



print ("done")
