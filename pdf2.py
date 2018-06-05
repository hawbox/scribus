#!/usr/bin/env python3
import glob
import re
import os
import sys
if os.name == "nt":
	addMe = os.environ["MYPYTHONPATH"]
	sys.path.append(addMe)
import pyManga.constants2 as constants
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", help="the directory the file is in")
parser.add_argument("-p", help="the page range to process as x,y,a-b,e...")

args, unknown = parser.parse_known_args()

os.chdir(args.d)
print("5555555555555555555555555555")
print(os.getcwd())
print(glob.glob("*.sla"))
for slaFileName in glob.glob("*.sla"):
    scribus.openDoc(slaFileName)    
	if not args.p:
		if os.path.isfile("segments.txt"):
			file = open("segments.txt", "r")
			args.p = file.readline().replace(" ", ",")
			file.close()
		else: args.p = range(1, pageCount()+1)
	elif not os.path.isfile("segments.txt"):
		file = open("segments.txt", "w")
		file.write(args.p.replace(",", " ")
		file.close()
	for scroll in args.p.split(","):
		print("scroll: " + scroll)
		pdf = scribus.PDFfile()
		pdf.file = os.path.splitext(slaFileName)[0] + "_" + scroll + ".pdf"
		pdf.binding = 1 #RIGHT TO LEFT
		pdf.compress = True
		# if args.p:
			# pdf.pages = constants.listString(scroll)
			# pdf.pages.sort()
		pdf.compressmtd = 3 #NONE
		pdf.resolution = 300
		print("############################################")
		print(scroll + " printing pages: " + str(pdf.pages))
		pdf.save()


