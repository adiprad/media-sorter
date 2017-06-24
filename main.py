# !/usr/bin/python

# Make sure to install exifread and argparse using pip

import os, exifread, argparse
from shutil import copyfile

extList=['jpg','jpeg','JPG','JPEG']
parser = argparse.ArgumentParser(description='Organize media files based on EXIF data')
parser.add_argument('source_dir',type=str,help='Source Directory')
parser.add_argument('target_dir',type=str,help='Target Directory')
args=parser.parse_args()
output=args.target_dir
if os.path.isdir(output)==False:
    os.mkdir(output)
for root, dirs, files in os.walk(args.source_dir,topdown=False):
    for name in files:
        filePath=os.path.join(root,name) # full filepath
        fileExt=filePath.split('.')[-1] # file extension
        for ext in extList:
            if fileExt==ext:
                f=open(filePath,'rb')
                date=exifread.process_file(f,stop_tag='EXIF DateTimeOriginal')['EXIF DateTimeOriginal']
                print (filePath)
                date=str(date).split(" ")[0].split(":")
                year=output+'/'+date[0]
                month=year+'/'+date[1]
                day=month+'/'+date[2]
                dest=day+'/'+name
                print (dest)
                if os.path.isdir(year)==False:
                    os.mkdir(year)
                if os.path.isdir(month)==False:
                    os.mkdir(month)
                if os.path.isdir(day)==False:
                    os.mkdir(day)
                if os.path.exists(dest)==False:
                    copyfile(filePath, dest)
                else:
                    print ('ERROR: file exists')
