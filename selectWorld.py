import csv
from secrets import randbelow
import asyncio
from random import shuffle
import glob
showStr = lambda L: ' '.join(map(str, L))


class MyQueue(asyncio.Queue):

    def __init__(self):
        super().__init__()

    def shuffle(self):
        if self._queue is not self.empty():
         shuffle(self._queue)
        else: return None

def ConvertString(string):
    tolist=[]
    tolist[:0]=string
    return tolist



csvFiles = []      #************ update 10/12/2564
def worldSearch(inpFileName):
    
    for file in glob.glob('DataWorld/AllWorld/*.csv'):
        directory = file.replace('DataWorld/AllWorld\\', '')
        directory =directory.replace('.csv', '')
        #directory = directory.strip('.csv')
        csvFiles.append(directory)
    print(csvFiles)
    for i in range(len(csvFiles)):
        if str(csvFiles[i]) == str(inpFileName):
            return csvFiles[i]
        else :
            if i == (len(csvFiles)-1):
                return None
            else: pass


async def worldSelect(obj,fileName) :
    print(f'Name : {fileName}')
    if fileName is not None :
        with open('DataWorld/AllWorld/'+fileName+'.csv', newline='') as f:
            reader = csv.reader(f)
            temp = list(reader)
            while len(temp) != 0:
                pos = randbelow(len(temp))
                # output type
                await obj.put(temp[pos])
                #await obj.put(ConvertString(showStr(temp[pos])))
                del temp[pos]
    else:
        print("Not found")
        return -1


async def getWorld(obj):
    obj.shuffle()
    #print(obj.__str__())
    while not obj.empty():
        tempGet = await  obj.get()
        Label(text=tempGet[0]).pack()
        return tempGet




#----------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
d = MyQueue()
def Input(group):
    fileName = group
    asyncio.run(worldSelect(d, worldSearch(fileName)))
    csvFiles.clear()   #***************************************** update 10/12/2564

#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------

from tkinter import  *
root = Tk() #??????????????????
root.title("World")

myMenu = Menu()
root.config(menu =myMenu)

#??????????????????????????????
mylabel = Label(root,text = "????????????????????????????????????????????????",fg = "red"  , font = 20 , bg = 'yellow'  ).pack()

def showWorld():
    if d.empty() is False:
     checkWorld = asyncio.run(getWorld(d))
     print(f'Get word = {checkWorld[0]}')
    else:
        print('Word is empty')
   #print(type(asyncio.run(getWorld(d))))



def clearListWord(): #************** update 10/12/2564
    while d.empty() is False:    #************** update 10/12/2564
     d.get_nowait()   #************** update 10/12/2564
#????????????
bth1 = Button(root,text="??????",fg ="white",bg = 'blue' ,command = showWorld).pack()
bth2 = Button(root,text="clear",fg ="white",bg = 'blue' ,command = clearListWord ).pack() #************** update 10/12/2564




def Check():

    #while d.empty() is False:
    #
    ch1 = Adjective.get()
    if ch1 == 1:
        Label(text="select Adjective").pack()
        print('run file Adjective')
        Input('Adjective')

    ch2 = Animal.get()
    if ch2 == 1:
        Label(text="select Animal").pack()
        print('run file Animal')
        Input('Animals')
    ch3 = BodyParts.get()
    if ch3 == 1:
        Label(text="select BodyParts").pack()
        print('run file BodyParts')
        Input('BodyParts')
    ch4 = Colors.get()
    if ch4 == 1:
        Label(text="select Colors").pack()
        print('run file Colors')
        Input('Colors')
    ch5 = Sport.get()
    if ch5 == 1:
        Label(text="select Sport").pack()
        print('run file Sport')
        Input('Sport')
    ch6 = Country.get()
    if ch6 == 1:
        Label(text="select Country").pack()
        print('run file Country')
        Input('Country')
    ch7 = Fruits.get()
    if ch7 == 1:
        Label(text="select Fruits").pack()
        print('run file Fruits')
        Input('Fruits')
    ch8 = ThaiFood.get()
    if ch8 == 1:
        Label(text="select ThaiFood").pack()
        print('run file ThaiFood')
        Input('ThaiFood')

# 0 ???????????????????????? 1 = ???????????????
Adjective = IntVar()
Checkbutton(text = "Adjective",variable = Adjective).pack(anchor =W)

Animal = IntVar()
Checkbutton(text = "Animals",variable = Animal).pack(anchor =W)

BodyParts = IntVar()
Checkbutton(text = "BodyParts", variable = BodyParts).pack(anchor =W)

Colors = IntVar()
Checkbutton(text = "Colors", variable = Colors).pack(anchor =W)

Sport = IntVar()
Checkbutton(text = "Sport", variable = Sport).pack(anchor =W)

Country = IntVar()
Checkbutton(text = "Country",variable = Country).pack(anchor =W)

Fruits = IntVar()
Checkbutton(text = "Fruits",variable = Fruits).pack(anchor =W)

ThaiFood = IntVar()
Checkbutton(text = "ThaiFood ??????????????????", variable = ThaiFood).pack(anchor =W)


Button(text="???????????????????????????" , command = Check).pack(anchor = W)
#????????????????????????????????????????????????????????? "500x500+x+y"
#menusmall = Menu(menusmall,tearoff=0);
#????????????????????????????????????
root.geometry("500x500+0+0")
root.mainloop()









