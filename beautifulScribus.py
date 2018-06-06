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
parser.add_argument("-d", required=True, help="the directory the file is in")
parser.add_argument("-b", required=True, help="The before glob of files")
parser.add_argument("-a", required=True, help="The after glob of files")
args, unknown = parser.parse_known_args()

os.chdir(args.d)
print(os.getcwd())
print(glob.glob("*.sla"))
for slaFileName in glob.glob("*.sla"):
	scribus.openDoc(slaFileName)	
	


