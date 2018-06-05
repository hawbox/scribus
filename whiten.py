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
	scribus.setFillColor(fillColor, selected)
	scribus.setLineShade(lineWidth, selected)
	scribus.setLineWidth(lineWidth, selected)
	scribus.setLineTransparency(lineWidth, selected)
	#scribus.setLineStyle(lineStyle, rectangle)
	#scribus.setStrokeColor(strokeColor, rectangle)
