#!/usr/bin/python
#---------------------------------------
# ovpn-to-certificates.py
# (c) Jansen A. Simanullang
# 27.03.2016 13:26
#---------------------------------------
# usage: python ovpn-to-certificates.py
#
# example:
# python ovpn-to-certificates.py
#
# features:
# grab ovpn files and create certificates
# ca.crt, client.crt, client.key
#
# you should edit the OVPN path here:

path = 'D:\Python\Projects\ovpn-to-certificates-master\\'



import os, re


def fileFilter(path, fileExtension):

	dirContents  = os.listdir(path)
	selectedFiles = []
	
	count = 0

	for filename in dirContents:

		if fileExtension in filename:
		
			print(filename.strip())
			
			count = count + 1
			
			selectedFiles.append(path+filename)
			
	print("\nThere are ", count, fileExtension + " files\n\n")

	return selectedFiles
	

	
def grabBetweenTag(tagName, fileContents):

	betweentag = re.findall('<'+tagName+'>.*\n(^.*$.*\n[\S\n]+.*$\n)</'+tagName+'>', fileContents, re.MULTILINE)

	return betweentag[0]
	


def fileCreate(strNamaFile, strData):
	#--------------------------------
	# fileCreate(strNamaFile, strData)
	# create a text file
	#
	try:
	
		f = open(strNamaFile, "w")
		f.writelines(str(strData))
		f.close()
	
	except IOError:
	
		strNamaFile = strNamaFile.split(os.sep)[-1]
		f = open(strNamaFile, "w")
		f.writelines(str(strData))
		f.close()
		
	print("file created: " + strNamaFile + "\n")
	
	
	
def readTextFile(strNamaFile):

	f = open(strNamaFile, "r")
	
	print("file being read: " + strNamaFile + "\n")
	
	return f.read()
	


def ovpnToCertificate(strNamaFile):

	fileContents = readTextFile(strNamaFile)
	
	strData = ""
	
	tagFile = {'ca':'ca.crt', 'cert':'client.crt', 'key':'client.key'}
	
	for tag, file in tagFile.items():
	
		strData = strData + grabBetweenTag(tag, fileContents)
	
		strNamaFile = strNamaFile.replace(".ovpn","")
		
		print(tag, strNamaFile + "-" + file)
		
		fileCreate(strNamaFile + "-" + file, strData)
	
	
	
def main():

	fileExtension = '.ovpn'
	selectedFiles = fileFilter(path, fileExtension)

	for files in selectedFiles:
		
		ovpnToCertificate(files)

	
main()
