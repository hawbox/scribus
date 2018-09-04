import scribus
import os
import glob
pageNum = scribus.pageCount()
print(pageNum)

result = ""

os.chdir(os.path.dirname(scribus.getDocName())+"/../png")
listeImages = sorted(glob.glob("*"))

itemNum = 0
for i in range(1,pageNum+1):

	scribus.gotoPage(i)
	for o in scribus.getAllObjects():
		if(scribus.getObjectType(o) == "ImageFrame"):
			if(scribus.getSize(o)[0] >= scribus.getPageSize()[0] * 0.99):
				#result = result + "item:" + str(itemNum) + " page:" + str(i) + " name: " + o + "\n" + " imageFile:" + scribus.getImageFile(o)
				scribus.loadImage(listeImages[itemNum], o)
				itemNum = itemNum + 1

#scribus.messageBox("caption", result)
#scribus.messageBox("listeImages", "\n".join(listeImages))
