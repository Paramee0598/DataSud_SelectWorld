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

def worldSearch(inpFileName):
    csvFiles = []
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
                #await obj.put(temp[pos])
                await obj.put(ConvertString(showStr(temp[pos])))
                del temp[pos]
    else:
        print("Not found")
        return -1


async def getWorld(obj):
    obj.shuffle()
    #print(obj.__str__())
    while not obj.empty():
        tempGet = await  obj.get()
        Label(text=tempGet).pack()
        return tempGet




#----------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
d = MyQueue()
def Input(group):
    fileName = group
    asyncio.run(worldSelect(d, worldSearch(fileName)))
#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------

from tkinter import  *
root = Tk() #หน้าจอ
root.title("World")

myMenu = Menu()
root.config(menu =myMenu)

#ใส่ข้อความ
mylabel = Label(root,text = "เลือกหมวดดิอิสัส",fg = "red"  , font = 20 , bg = 'yellow'  ).pack()

def showWorld():
    print(f'Get world = {asyncio.run(getWorld(d))}')

#ปุ่ม
bth1 = Button(root,text="กด",fg ="white",bg = 'blue' ,command = showWorld).pack()




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
        Input('Animal')
    ch3 = CarBrandName.get()
    if ch3 == 1:
        Label(text="select CarBrandName").pack()
        print('run file CarBrandName')
        Input('CarBrandName')
    ch4 = CarID_Model.get()
    if ch4 == 1:
        Label(text="select CarID_Model").pack()
        print('run file CarID_Model')
        Input('CarID_Model')
    ch5 = CarModel.get()
    if ch5 == 1:
        Label(text="select CarModel").pack()
        print('run file CarModel')
        Input('CarModel')
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
    ch8 = Laptop.get()
    if ch8 == 1:
        Label(text="select Laptop").pack()
        print('run file Laptop')
        Input('Laptop')

# 0 ไม่เลือก 1 = เลือก
Adjective = IntVar()
Checkbutton(text = "Adjective",variable = Adjective).pack(anchor =W)

Animal = IntVar()
Checkbutton(text = "Animal",variable = Animal).pack(anchor =W)

CarBrandName = IntVar()
Checkbutton(text = "CarBrandName", variable = CarBrandName).pack(anchor =W)

CarID_Model = IntVar()
Checkbutton(text = "CarID_Model",variable = CarID_Model).pack(anchor =W)

CarModel = IntVar()
Checkbutton(text = "CarModel",variable = CarModel).pack(anchor =W)

Country = IntVar()
Checkbutton(text = "Country",variable = Country).pack(anchor =W)

Fruits = IntVar()
Checkbutton(text = "Fruits",variable = Fruits).pack(anchor =W)

Laptop = IntVar()
Checkbutton(text = "Laptop",variable = Laptop).pack(anchor =W)


Button(text="เลือกไรมา" , command = Check).pack(anchor = W)
#กำหนดหน้าต่างหน้าจอ "500x500+x+y"
#menusmall = Menu(menusmall,tearoff=0);
#กล่องข้อความ
root.geometry("500x500+0+0")
root.mainloop()










