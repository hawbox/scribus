import scribus
n = scribus.selectionCount()
list = []
for i in range(0,n):
	list.append(scribus.getSelectedObject(i))

margin = 2
fillColor = "White"
lineStyle = "noLine"
lineWidth = 0

#deselectAll()
for selected in list:
	x, y = scribus.getPosition(selected)
	width, height = scribus.getSize(selected)
	rectangle = scribus.createRect(x-margin, y-margin, width+margin*2, height+margin*2)
	scribus.setFillColor(fillColor, rectangle)
	scribus.setLineShade(lineWidth, rectangle)
	#scribus.setLineStyle(lineStyle, rectangle)
	#scribus.setStrokeColor(strokeColor, rectangle)
