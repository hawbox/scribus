#!/usr/bin/env python3
import glob
import re
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", help="the directory the file is in")
parser.add_argument("-p", help="the page range to process as x,y,a-b,e...")
parser.add_argument("-s", help="scribus pdf scrolls to process as x,y,a-b,e...")

args, unknown = parser.parse_known_args()

print("############################################")
print(args)
print("############################################")

"""
print("step: " + args.s)
print("directory: " + args.d)
print("file: " + args.file)
print("pages: " + args.p)
"""
os.chdir(args.d)
  
for scroll in args.s.split(","):
    scribus.openDoc(scroll)
    pdf = scribus.PDFfile()
    pdf.file = os.path.splitext(scroll)[0] + ".pdf"
    pdf.binding = 1 #RIGHT TO LEFT
    pdf.compress = True
    pdf.compressmtd = 3 #NONE
    if args.p:
        pdf.pages = constants.listString(args.p)
    pdf.pages.sort()
    pdf.resolution = 300
    print("############################################")
    print(scroll + " printing pages: " + str(pdf.pages))
    pdf.save()


