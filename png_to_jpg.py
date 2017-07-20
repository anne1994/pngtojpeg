from PIL import Image
import fnmatch
import os
from os import listdir, makedirs
from os.path import isdir, join, exists
from shutil import copyfile
import scipy
from scipy.misc import imread
import cv2
import matplotlib as plt

print("ho")
curate_dir = "C:/Users/annea/tf_files/homework_agilent"
print("hi")
img_path = join("C:/Users/annea/tf_files/prescan_images")

min_class_size = 60

if not exists(img_path):
    print('creating %s' % img_path)
    makedirs(img_path)

labels = [f for f in listdir(curate_dir) if isdir(join(curate_dir, f))]
print(labels)

for label in labels:
    cdir = join(curate_dir,label)
    ldir = join(img_path,label)
    #for f in listdir(cdir):
    files = fnmatch.filter(listdir(cdir),'*.png')
    #nfiles = len(files)
    for f in files:
        #pic = str(f)
        #A=cv2.imread(files)
        #im=Image.fromarray(A)
        #im.save("f.jpg")
        #scipy.misc.imsave("f.jpg")
        #files = fnmatch.filter(listdir(cdir),'*.jpg')
        #print(files)
        #file,ext = os.path.splitext(f)
        #print(file)
        pic=f
        A=cv2.imread(os.path.join(cdir,f))
        im=Image.fromarray(A)
        img_path2="C:/Users/annea/tf_files/prescan_images/"+label
        #img_path2 = os.path.join(img_path,label)
        if not exists(img_path2):
            print('creating %s' % img_path2)
            makedirs(img_path2)
        os.chdir(img_path2)
        f=f.strip('.png')
        im.save(" %s .jpg" % (f))
        
      

    print('done')




    #for label in labels:

#im=Image.open("C:/Users/annea/tf_files/homework_agilent/blotches/US22502520_254472095944_S01_t1.png")
#im.save('US22502520_254472095944_S01_t1.jpg') 
