import os

file_types=".yuv,.wmv,.webm,.vob,.svi,.roq,.rmvb,.rm,.ogv,.ogg,.nsv,.mxf,.mpg,.mpeg,.m2v,.mpg,.mp2,.mpeg,.mpe,.mpv,.mp4,.m4p,.m4v,.mov,.qt,.mng,.mkv,.m4v.gifv,.flv,.f4v,.f4p,.f4a,.f4b,.flv,.drc,.avi,.asf,.amv,.3gp,.3g2"
file_types=file_types.split(",")

vido_file_found=[]


for root, dirs, files in os.walk("./"):
    for file in files:
        for types in file_types:
            if file.endswith(types):
                 vido_file_found.append(os.path.join(root, file))



for q in vido_file_found:
    print(q)
