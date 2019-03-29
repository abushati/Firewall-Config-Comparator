import os


class FireWallComparer():
	def __init__(self,mainFile,secFile,saveLocation):

		mainFileDic = mainFile#"\\\dot55fs10.dot.nycnet\\UsersHomeDrive\\ABushati\\Desktop\\firewallCompare\\corepls.txt"
		secondary = secFile#"\\\dot55fs10.dot.nycnet\\UsersHomeDrive\\ABushati\\Desktop\\firewallCompare\\second.txt"
		self.saveLocation = saveLocation

		self.mainInfo= {}
		self.secondaryInfor = {}
		self.listOfMissingInfo = []
		self.listofFiles = [mainFileDic,secondary]
		self.searchingKeyWords = ["object network", "route", "access-list","object-group"]
		self.main()
	
	def main(self):
		for index,file in enumerate(self.listofFiles):
			for self.word in self.searchingKeyWords:
				print(self.word+"--------------------------------------")
				if index == 1:
					self.readFile(file,self.secondaryInfor)
				else:
					self.readFile(file, self.mainInfo)


		for self.word,stuffInWord in list(self.mainInfo.items()): 
			
			for stuff in self.mainInfo[self.word]:
				
				if type(stuff) == type({}):
					
					self.compareDicts(stuff)
					
				else:
					self.compareDicts(stuff)				
			
			print("----------------------------------------------------------------------")

		with open(self.saveLocation,'w') as missing:
			for missingInfo in self.listOfMissingInfo:

				if type(missingInfo) == type({}):
					for parent, child in  missingInfo.items():
						pass
					print(parent,child)
					missing.write("\n" + parent)
					[missing.write("\n   " + str(x) ) for x in child] 
				else:
					missing.write(str(missingInfo)+"\n")



		
			

	def compareDicts(self,info):

		for items in self.secondaryInfor[self.word]:
			if type(items) == type({}):
				name = items.keys()
				if name == info.keys():
					#print(f'{info.keys()} its a match {name}')
					return
					#print(f"{info} from the main firewall matches {items}")

					#print(f'{info} is not found in the second firewall')
			else:
				if info == items:
					return
					#print(f'this is a index in the list {info} and {items}')
				#if(info == )
		self.listOfMissingInfo.append(info)
					
		#print(dict)


	def getInfo(self,file,currentIndex):
		objectName = file[currentIndex].replace("\n","").strip()
		print(file[currentIndex])
		return file


	def getSubInfo(self,file,currentIndex):
		objectInfor = {}
		objectName = file[currentIndex].replace("\n","").strip()
		tempList=[]
		#print(objectName)
		try:
			while True:
				nextLine = file[currentIndex+1].replace("\n","")
				nextLineList = nextLine.split(" ")
				if nextLineList[0] == "":
					currentIndex += 1
					#Strip here b/c the algorthim depends on leading whitespace
					tempList.append(nextLine.strip())
				else:
					objectInfor[objectName] = tempList
					#print(objectInfor)
					return objectInfor
		except:
			return		



	def checkIfRightWord(self,line):
		wordListOfSectence = line.split(self.word)
		#print(wordListOfSectence)
		if wordListOfSectence[0] == "":
			return True
		else:
			return False


	def readFile(self,file,bucketOfInfo):
		listOfInfo = []
		with open(file,"r") as CoreFile:
			listOfLines = CoreFile.readlines()
			
			for index,line in enumerate(listOfLines):
			
				if self.word in line:
					correctLine = self.checkIfRightWord( line)
					if correctLine:

						if self.word=="object network" or self.word=="object-group":
							#print(self.word)
							objectInfo = self.getSubInfo(listOfLines,index)
							listOfInfo.append(objectInfo)
						else:
							line = line.replace(" \n","").strip()
							listOfInfo.append(line)

			#print(listOfInfo)
			bucketOfInfo[self.word] = listOfInfo				




