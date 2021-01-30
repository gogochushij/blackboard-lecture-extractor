import requests
import shutil
import os

beurl = [ [ "https://bb.spbu.ru/bbcswebdav/courses/UNIV.000999.2016.FT.TEST.1.C02.FPTB.1/L10-Комплекс ГТО/files/assets/common/page-html5-substrates/page", "_l.jpg"] ]#, ["https://bb.spbu.ru/bbcswebdav/courses/UNIV.000999.2016.FT.TEST.1.C02.FPTB.1/L09-Спортивное питание/files/assets/common/page-html5-substrates/page", ".jpg"] ]

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
    
            
        