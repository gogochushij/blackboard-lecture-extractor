from PIL import Image
import shutil
import os

folder = "C:/users/heythere/Desktop/Physical/"
lec = "Lec" + input("номер лекции:")
n = int(input("число страниц:"))

for i in range(1, n+1):
    fr = folder + lec + "/source/"
    to = folder + lec + "/"
    num = str(i).zfill(4)
    if os.path.exists(fr + num + "_c.png"):
        bg = Image.open(fr + num + ".jpg").convert("RGBA") 
        w, h = bg.size
        fg = Image.open(fr + num + "_c.png").convert("RGBA").resize((w,h))
        bg.paste(fg, (0,0), fg)
        bg.convert("RGB").save(to + num + ".jpg", "JPEG")
        print("edited and copied", to + num + ".jpg")
    else:
        shutil.copyfile(fr + num + ".jpg", to + num + ".jpg")
        print("copied", to + num + ".jpg")

