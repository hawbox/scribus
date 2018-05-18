n = scribus.selectionCount()
list = []
for i in range(0,n):
	list.append(getSelectedObject(i))

margin = 2
fillColor = "White"
lineStyle = "noLine"

#deselectAll()
for selected in list:
	x, y = getPosition(selected)
	width, height = getSize(selected)
	rectangle = createRect(x-margin, y-margin, width+margin*2, height+margin*2)
	setFillColor(fillColor, rectangle)
	#setLineStyle(lineStyle, rectangle)
	#setStrokeColor(strokeColor, rectangle)
