#Main Page Function 
from tkinter import *
#Modules to open the img links in SQL table:
from PIL import Image, ImageTk
from urllib.request import urlopen
import mysql.connector
import webbrowser

store=[]
index=0
carts=[] #user's cart

'''All the photographs used in this program do not belong to us
and are only being used for educational purposes. All credit
for the photos goes to their respective owners.'''

#-------------------------Pages--------------------------
'''
mainpg: the main home page which allows user to shop,
        contact support and go to cart
contactpg: page where user can go to for getting support
shoppg: page where user makes their choices
clothespg: page which shows the user the clothes available
checkoutpg: page which shows user the final billings
typage: final screen where user exits program
'''
#---------------------------------------------------------


def mainf():
    mainpg = Tk()
    mainpg.geometry("965x675")
    mainpg.resizable(False, False)
    mainpg.title('EasyShop Home')
    mainpg['background'] = '#33f5eb'

        #functions for the three buttons
    def contactbuttonpressed():
        mainpg.destroy()
        contactf()
    def shopbuttonpressed():
        mainpg.destroy()
        shopf()
    def cartbuttonpressed():
        if carts != []:
            #if carts isnt an empty list, user has made a choice.
            #program will proceed
            mainpg.destroy()
            checkoutf()
        else:
            #else will tell user to make a choice 
            choosetext['text'] = 'Please shop first.'

   

        
    #Row wise widgets
    success = Label(mainpg, text = 'Welcome to EasyShop!', font = ('Century Gothic',18), background = '#33f5eb')

    imgad = PhotoImage(file = "homead.png")
    canvasad = Label(mainpg, image = imgad)
    
    cartimg = PhotoImage(file = "cartimg.png")
    cartb = Button(mainpg, image = cartimg, height = 75, width = 75, command = cartbuttonpressed)
    shopimg = PhotoImage(file = "shopimg.png")
    shopb = Button(mainpg, image = shopimg, height = 75, width = 75, command = shopbuttonpressed)
    contactimg = PhotoImage(file = "contactimg.png")
    contactb = Button(mainpg, image = contactimg, height = 75, width = 75, command = contactbuttonpressed)

    carttext = Label(mainpg, text = 'Continue \n to Cart', background = '#33f5eb')
    shoptext = Label(mainpg, text = 'Continue \n Shopping', background = '#33f5eb')
    contacttext = Label(mainpg, text = 'Contact \nSupport', background = '#33f5eb')

    choosetext = Label(mainpg, background = '#33f5eb', font = ('Century Gothic',10))

    success.grid(row = 0, column = 1, pady = 10)

    canvasad.grid(row = 2, column = 1, pady = 10)
    
    cartb.place(x=775, y= 530)
    shopb.grid(row = 3, column = 1)
    contactb.place(x=110, y= 530)

    carttext.place(x=785, y= 620)
    shoptext.grid(row = 4, column = 1)
    contacttext.place(x=120, y= 620)
    
    choosetext.grid(row = 5, column = 1, pady = 5)
    
    mainpg.mainloop()

#--------------------------------CONTACT PAGE------------------------------
def contactf():
    contactpg = Tk()
    
    contactpg.resizable(False, False)
    contactpg.title('EasyShop Support')
    contactpg['background'] = '#33f5eb'

    def backf():
        contactpg.destroy()
        mainf()

    def whatsapprun():
        webbrowser.open("https://web.whatsapp.com/",new=1)

    def gmailrun():
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox",new=1)

    img = PhotoImage(file = "logo.png")
    canvas = Label(contactpg, image = img)
    supporttext1= Label(contactpg, text = 'Creators:', font = ('Century Gothic',15), background = '#33f5eb')
    supporttext2 = Label(contactpg, text = 'dhruv.rawal2005@gmail.com \n 9810172925 \n adit.sinha05@gmail.com \n 8800983347 \n\n\n\n', background = '#33f5eb')
    backb = Button(contactpg, text = 'Back', width = 10, command = backf)

    phoneimg = PhotoImage(file = "whatsapp.png")
    phoneb = Button(contactpg, image = phoneimg, height = 50, width = 50, command = whatsapprun)
    mailimg = PhotoImage(file = "gmail.png")
    mailb = Button(contactpg, image = mailimg, height = 50, width = 50, command = gmailrun)
                         
    canvas.pack(padx = 10, pady = 10)
    supporttext1.pack()
    supporttext2.pack()
    backb.pack(pady = 5)
    phoneb.place(x=20, y = 160)
    mailb.place(x=155, y = 160)
    mainloop()
#--------------------------------------------------------------------------

#-----------------------------SHOPPING PAGE--------------------------------
def shopf():
    global store, index, carts   
    
    shoppg=Tk()
    shoppg.geometry("500x500")
    shoppg.title('Easy Shop')
    shoppg['background'] = '#33f5eb'
    
    welcometext = Label(shoppg,text="Choose To Shop",font=('Century Gothic',15), background = '#33f5eb').place(x=170,y=130)
    proceedtext = Label(shoppg,text="Please choose one out of each row.", background = '#33f5eb').place(x=155,y=170)
    
    img = PhotoImage(file="logo.png")
    canvas = Label(shoppg,image=img)
    canvas.place(x=150,y=70)

    #Chosen:
    chosenmwklabel = Label(shoppg, text = '', background = '#33f5eb')
    chosenmwklabel.place(x=200,y=250)
    chosenftblabel = Label(shoppg, text = '', background = '#33f5eb')
    chosenftblabel.place(x=200,y=350)
    chosenmoneylabel = Label(shoppg, text = '', background = '#33f5eb')
    chosenmoneylabel.place(x=200,y=450)
    
    #Global Variables
    store=['0','1','2']
    index=0
    

    #Functions
    def men():
        store[0] = 'men_'
        chosenmwklabel['text'] = 'Chosen: Men'
        
    def women():
        store[0] = 'women_'
        chosenmwklabel['text'] = 'Chosen: Women'
        
    def kids():
        store[0] = 'kids_'
        chosenmwklabel['text'] = 'Chosen: Kids'
        
    def foot():
        store[1] = 'foot'
        chosenftblabel['text'] = 'Chosen: Footwear'
        
    def top():
        store[1] = 'top'
        chosenftblabel['text'] = 'Chosen: Topwear'
    
    def bottom():
        store[1] = 'bottom'
        chosenftblabel['text'] = 'Chosen: Bottomwear'
        
    def L1000():
        store[2] = '<1000'
        chosenmoneylabel['text'] = 'Chosen: Less than 1000'
        
    def B1000():
        store[2] = '1000-2000'
        chosenmoneylabel['text'] = 'Chosen: 1000 to 2000'
        
    def M2000():
        store[2] = '>2000'
        chosenmoneylabel['text'] = 'Chosen: More than 2000'


    #Buttons to make choices
    men=Button(shoppg,text='MEN',bd='5',width=12,command=men)
    men.place(x=100,y=200)
    women=Button(shoppg,text='WOMEN',bd='5',width=12,command=women)
    women.place(x=200,y=200)
    child=Button(shoppg,text='KIDS',bd='5',width=12,command=kids)
    child.place(x=300,y=200)
    
    foot=Button(shoppg,text='FOOTWEAR',bd='5',width=12,command=foot)
    foot.place(x=100,y=300)
    top=Button(shoppg,text='TOPWEAR',bd='5',width=12,command=top)
    top.place(x=200,y=300)
    bottom=Button(shoppg,text='BOTTOMWEAR',bd='5',width=12,command=bottom)
    bottom.place(x=300,y=300)
    
    L1000=Button(shoppg,text='Less than 1000',bd='5',width=12,command=L1000)
    L1000.place(x=100,y=400)
    B1000=Button(shoppg,text='1000-2000',bd='5',width=12,command=B1000)
    B1000.place(x=200,y=400)
    M2000=Button(shoppg,text='More than 2000',bd='5',width=12,command=M2000)
    M2000.place(x=300,y=400)
    
    #--------------------------------------------DISPLAY PAGE--------------------------------------------    
    def main():
      global carts, index, store
      if store[0] != '0' and store[1] != '1' and store[2] != '2':
        shoppg.destroy()
        
        clothespg=Tk()
        clothespg.geometry("1500x2000")
        clothespg.title('Easy Shop')
        clothespg['background']='#677FA3'
        
        l1 = store
        index = 0
        

        category = l1[0] + l1[1]
        items = []
        #items list would contain pictures
        fullline = []
        #fullline would contain the entire line from the file

        itemdb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'root', db = 'dex')
        mycursor = itemdb.cursor()
        
        if l1[2]==('<1000'):
            mycursor.execute("select * from items where type = '%s' and price < 1000"%category)
            for i in mycursor:
                items.append(i[3])
                x = [i[2], i[3], i[0]]
                fullline.append(x)
                    
        elif l1[2]==('>2000'):
            mycursor.execute("select * from items where type = '%s' and price > 2000"%category)
            for i in mycursor:
                items.append(i[3])
                x = [i[2], i[3], i[0]]
                fullline.append(x)
            
        elif l1[2]==('1000-2000'):
            mycursor.execute("select * from items where type = '%s' and price between 1000 and 2000"%category)
            for i in mycursor:
                items.append(i[3])
                x = [i[2], i[3], i[0]]
                fullline.append(x)

        
        def link_img():
            global index

            if index < len(items)-1 and index >=0:
                index+=1
                URL = items[index]
                u = urlopen(URL)
                raw_data = u.read()
                u.close()
                photoprice = fullline[index][0]
                phtitle=fullline[index][2].replace('-',' ')
                
                addcart['text'] = 'Add to Cart'

                photopricetext['text'] = 'Price: ' + str(photoprice)
                photoname['text']=phtitle
                #Changes the image by changing raw_data
                photonew = ImageTk.PhotoImage(data=raw_data)
                photoshow.configure(image=photonew)
                photoshow.image = photonew
            else:
                photopricetext['text'] = 'You have reached the end, please use the left arrow.'
                
        def link_img2():
            global index
      
            if index <= len(items) and index > 0:
                index-=1
                URL = items[index]
                u = urlopen(URL)
                raw_data = u.read()
                u.close()
                photoprice = fullline[index][0]
                phtitle=fullline[index][2].replace('-',' ')
                
                addcart['text'] = 'Add to Cart'
                
                photopricetext['text'] = 'Price: ' + str(photoprice)
                photoname['text']=phtitle
                #Changes the image by changing raw_data
                photonew = ImageTk.PhotoImage(data=raw_data)
                photoshow.configure(image=photonew)
                photoshow.image = photonew
            else:
                photopricetext['text'] = 'You have reached the end, please use the right arrow.'
                
        def cart():
            global carts
            #adds entire line of choice made to list to be protrayed later in listbox
            title = fullline[index][2]+ ' ' + str(fullline[index][0]) 
            mycursor.execute("insert into cart values('" +  fullline[index][2] + "', " + str(fullline[index][0]) + ')')
            itemdb.commit()
            carts.append(title)
            addcart['text'] = f'Added ({carts.count(title)}) times'
            
            
        def checkoutbuttonpressed():
            if carts != []:
                clothespg.destroy()
                checkoutf()
            else:
                photopricetext['text'] = 'Please make a choice.'
                
        def homebuttonpressed():
            clothespg.destroy()
            mainf()

            
        URL=items[0]
        u = urlopen(URL)
        raw_data = u.read()
        u.close()
        #used to take image from url

        photoprice = fullline[0][0]
        photopricetext = Label(clothespg, text = ('Price: ' + str(photoprice)), font=('Century Gothic',15))
        phtitle=fullline[0][2].replace('-',' ')
        photoname=Label(clothespg,text=phtitle,font=('Century Gothic',25), background='#677FA3')
        
        photo = ImageTk.PhotoImage(data=raw_data)
        photoshow = Label(clothespg,image=photo, height = 650, width = 900)

        nextimg = PhotoImage(file = 'rightarrow.png')
        backimg = PhotoImage(file = 'leftarrow.png')
        nextb= Button(clothespg,image = nextimg, height = 70, width=30,command=link_img)
        backb= Button(clothespg,image = backimg, height = 70, width=30,command=link_img2)
        
        addcart=Button(clothespg,text='Add To Cart',width=20,command=cart)

        
        photoname.pack()
        photoshow.pack(pady = 10)
        photopricetext.pack()
        
        cartimg=PhotoImage(file="cartimg.png")
        cartbtn=Button(clothespg,image=cartimg,height=75,width=75, command=checkoutbuttonpressed)
        proceed2=Label(clothespg,text="Proceed to Cart")

        homeimg = PhotoImage(file = 'home.png')
        homebtn = Button(clothespg, image = homeimg, height = 75, width=75, command = homebuttonpressed)
        homebtntext = Label(clothespg, text = 'Return to home')

        #Geometry Managers
        proceed2.place(relx=.9 ,rely = .9)
        cartbtn.place(relx=.905 ,rely = .80)
        homebtn.place(rely=.80,relx=.01)
        homebtntext.place(relx=.01,rely=.9)
        nextb.place(relx=.98,rely = .5, anchor = 'center')
        backb.place(relx= .02, rely = .5, anchor = 'center')
        addcart.place(relx = .5, rely = .92, anchor = 'center')
        mainloop()
        
      else:
          next2['text'] = 'Please make all choices.'

    #----------------------------------------------------------------------------------------------


          
    next1=Button(shoppg,text='Continue->',bd='5',width=12,command=main)
    next1.place(x=400,y=470)
    next2=Label(shoppg, background = '#33f5eb')
    next2.place(x=185,y=470)
    mainloop()
#--------------------------------------------------------------------------


def checkoutf():
    global carts
    checkoutpg=Tk() 
    checkoutpg.geometry("700x520")
    checkoutpg.title('Your Cart')
    checkoutpg['background'] = '#33f5eb'

    
    img=PhotoImage(file="logo.png")
    canvas=Label(checkoutpg,image=img)
    canvas.pack(anchor='center',pady=10)
    
    
    heading=Label(checkoutpg,text="Checkout",font=('Century Gothic',25,), background = '#33f5eb').pack(anchor='center')
    order=Label(checkoutpg,text='Order Information', font=('Century Gothic',17), background = '#33f5eb').place(relx=.05,rely=.225)


    listbox=Listbox(checkoutpg,height=14,width=80) #contains items
    listbox2 = Listbox(checkoutpg, height = 14, width = 7) #contains prices
    listbox3 = Listbox(checkoutpg, height = 14, width = 10) #contains quantity
    
    rangenum = 0
    listbox.insert(0,'Item')
    listbox2.insert(0,'Price')
    listbox3.insert(0,'Quantity')
    for item in range(1, len(carts)+1):
        if carts.index(carts[item-1]) == item-1:
            #inserts items starting from line one
            listbox.insert(item,carts[item-1].split()[0])
            listbox2.insert(item,carts[item-1].split()[1])
            listbox3.insert(item,carts.count(carts[item-1]))
    
    
        
    listbox.place(relx=.048,rely=.29)
    listbox2.place(relx = .76, rely = .29)
    listbox3.place(relx = .86, rely = .29)

    amount = 0
    for i in carts:
        amount += int(i.split()[1])
    def shopmoref():
        checkoutpg.destroy()
        mainf()

    #clothes have 8% taxes
    taxes=Label(checkoutpg, background = '#33f5eb', text=('Taxes: ' + str(round(.08*amount,2))),font=('Century Gothic',14)).place(relx=.05,rely=.79)

    
            
    shopmore=Button(checkoutpg,text='Shop more',bd='5',width='8', command = shopmoref)
    shopmore.place(relx=.05,rely=.905)
    
    amount=round(1.08*amount, 2)
    tot_amount=Label(checkoutpg,text="Total Amount: "+str(amount),font=('Century Gothic',24), background = '#33f5eb').place(relx=.45,rely=.79)

    
        
    def typage():
        #final screen the user sees
        checkoutpg.destroy()
        typage=Tk()
        typage['background'] = '#33f5eb'
        typage.title('Thank you!')

        #button to exit the Tk window
        def exitbut():
            typage.destroy()
            itemdb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'root', db = 'dex')
            mycursor = itemdb.cursor()
            mycursor.execute('truncate table cart') #removing items from cart in sql
            print('aaa')
            itemdb.commit()
        logoimg = PhotoImage(file = 'thankyouend.png')

        exitbtn = Button(typage, text = 'Exit', command=exitbut)
        exitbtn.place(relx = 0.99, rely = 0.99, anchor = 'se')
        ty=Label(typage,text='Thank you for shopping with us!',font=('Century Gothic',20), background = '#33f5eb').pack(anchor='center',expand=True, pady = 10, padx = 10)
        logophoto = Label(typage, image = logoimg).pack(pady = 20, padx = 50)
        
        mainloop()
        
    ty=Button(checkoutpg,text='Proceed to pay',bd='5',command=typage,width='12')
    ty.place(relx=.76,rely=.91)
    mainloop()
    

#adding saved data from cart:
itemdb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'root', db = 'dex')
mycursor = itemdb.cursor()
mycursor.execute('select * from cart')
for i in mycursor:
    amongus = str(i[0])+ ' ' + str(i[1]) 
    carts.append(amongus)
mainf()
quit()
