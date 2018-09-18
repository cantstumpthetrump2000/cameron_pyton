import os
def get_size(start_path = './'):
    total_size = 0
    files_to_deleat=[]
    for dirpath, dirnames, filenames in os.walk(start_path):
        print("folder",dirpath)
        #print("folder2",dirnames)
        total_size = 0
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        print(dirpath)
        print(total_size)
        if total_size<100:
            files_to_deleat.append(dirpath)

    return(files_to_deleat)


files_to_remove=get_size("./")


for q in files_to_remove:
    try:
        os.remove(q)
    except Exception as e:
        print("error",e)
