import requests
import shutil
import os

beurl = [ [ "https://bb.spbu.ru/bbcswebdav/courses/.....", "_l.jpg"] ]

n = 87
lec = "Lec10"

folder = "C:/Users/heythere/Desktop/Physical/"
for i in range(n):
    if os.path.isdir(folder + lec) == False:
        os.mkdir(folder + lec)
        os.mkdir(folder + lec + "/source/")
    for p in beurl:
        url = p[0] + str(i+1).zfill(4) + p[1]
        path = folder + lec + "/source/" + str(i+1).zfill(4) + p[1]
        
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, "wb") as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            print("OK ", path)
        else:
            print(r.status_code, url)
    
            
        
