import os,shutil,magic

image = ['.jpeg','.png','.jpg','.gif','gif','jpg','png','jpeg']
video = ['.mp4','.avi','.mpeg','mp4','avi','mpeg']
audio = ['.mp3','.wav','mp3','wav']

folder = input("폴더명을 입력해주세요 : ")

if os.path.exists("{}/result".format(folder)) is False: os.mkdir("{}/result".format(folder))
if os.path.exists("{}/result/img".format(folder)) is False: os.mkdir("{}/result/img".format(folder))
if os.path.exists("{}/result/video".format(folder)) is False: os.mkdir("{}/result/video".format(folder))
if os.path.exists("{}/result/audio".format(folder)) is False: os.mkdir("{}/result/audio".format(folder))
if os.path.exists("{}/result/etc".format(folder)) is False: os.mkdir("{}/result/etc".format(folder))

for root,dirs,files in os.walk(folder):
    for filename in files:
        fullName = root + "/" + filename
        ext = magic.Magic(mime=True,uncompress=True,magic_file="libmagicwin64-master/magic.mgc").from_file(fullName).split("/")[1]
        print("Extension is [{}]".format(ext))
        if ext in image:
            shutil.copy(fullName,"{}/result/img/{}.{}".format(folder,filename,ext))
        elif ext in video:
            shutil.copy(fullName, "{}/result/video/{}.{}".format(folder, filename, ext))
        elif ext in audio:
            shutil.copy(fullName, "{}/result/audio/{}.{}".format(folder, filename, ext))
        else:
            if "plain" in ext:
                ext = ".txt"
            shutil.copy(fullName, "{}/result/etc/{}.{}".format(folder, filename, ext))
