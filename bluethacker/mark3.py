


import subprocess



x=subprocess.check_output(["dir"], shell=True)
x=x.decode()
print("xpppp",x)