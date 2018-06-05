import scribus

n = scribus.selectionCount()
list = []
for i in range(0,n):
	list.append(scribus.getSelectedObject(i))

print(list)

#deselectAll()
for selected in list:
	size = len(scribus.getAllText(selected))
	scribus.selectText(0, size , selected)
	scribus.setStyle("WASTE dialog", selected)
