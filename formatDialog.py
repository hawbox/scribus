n = scribus.selectionCount()
list = []
for i in range(0,n):
	list.append(getSelectedObject(i))

print(list)

#deselectAll()
for selected in list:
	size = len(getAllText(selected))
	selectText(0, size , selected)
	setStyle("WASTE dialog", selected)
