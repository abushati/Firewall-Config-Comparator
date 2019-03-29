from tkinter import filedialog
from tkinter import *
from CompareScript import FireWallComparer
import os



root = Tk()
#os.chdir("\\\dot55fs10.dot.nycnet\\UsersHomeDrive\\ABushati\\Desktop\\Firewall Compare")
mainVar = StringVar()
secVar = StringVar()
mainFile = Entry(root, textvariable = mainVar,text = mainVar, width = 60)
mainFile.grid(row = 2,column = 0)
secFile = Entry(root,  textvariable = secVar,text = secVar,width = 60)
secFile.grid(row = 3,column = 0)

def cleanPath(path):
	

	newPath = path.replace("//","")
	newPath = newPath.replace("/","\\")
	newPath= "\\\{}".format(newPath)

	return newPath

def send():
	mainFiles = str(mainVar.get())
	secFiles = str(secVar.get())
	mainFiles = cleanPath(mainFiles)
	secFiles = cleanPath(secFiles)


	print(secFiles)
	print (mainFiles)

	saveLocation = filedialog.asksaveasfile(filetypes = (("Text File","*.txt"),))
	savedFileLocation = str(saveLocation.name) +".txt"
	saveLocation.close()
	os.remove(saveLocation.name)

	print(savedFileLocation)
	savedFileLocation = cleanPath(savedFileLocation)
	print(savedFileLocation)
	
	FireWallComparer(mainFiles,secFiles,savedFileLocation)

def findMainFile():
	file = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text File","*.txt"),))
	return 	file
	



mains = Button(root,text = "Find Main File",command = lambda: mainVar.set(findMainFile()))
mains.grid(row = 2,column = 1)
sec = Button(root,text = "Find Secondary File",command = lambda: secVar.set(findMainFile()))
sec.grid(row = 3,column = 1)
Label(root, text="Step 1) Select the main file \n Step 2) Select the file you want to compare to the main file \n \
	Step 3) Click the compare button and SELECT LOCATION TO SAVE AND NAME FILE" ).grid(row = 0, column = 0)


Button(root,text = "Compare",command = lambda: send(), background = 'SeaGreen1' ).grid(row = 4)



mainloop()