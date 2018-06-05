#!/usr/bin/env python3
import glob
import re
import os
import sys
import argparse
import pyManga.constants2 as constants

parser = argparse.ArgumentParser()
parser.add_argument("-d", help="the directory the file is in")
parser.add_argument("-p", help="the page range to process as x,y,a-b,e...")


args, unknown = parser.parse_known_args()

os.chdir(args.d)
  
for slaFileName in glob.glob("*.sla"):
    scribus.openDoc(slaFileName)    
    if args.p:
        for scroll in args.p.split(","):
            print("scroll: " + scroll)
            pdf = scribus.PDFfile()
            pdf.file = os.path.splitext(slaFileName)[0] + "_" + scroll + ".pdf"
            pdf.binding = 1 #RIGHT TO LEFT
            pdf.compress = True
            if args.p:
                pdf.pages = constants.listString(scroll)
                pdf.pages.sort()
            pdf.compressmtd = 3 #NONE
            pdf.resolution = 300
            print("############################################")
            print(scroll + " printing pages: " + str(pdf.pages))
            pdf.save()


