

import random


print("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))