import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import smtplib

class FirstPage(tk.Frame):
  
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        load = Image.open("wallpaper.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image = photo)
        label.image=photo
        label.place(x=0,y=0)

        border=tk.LabelFrame(self,text="Login",bg="ivory", bd=10, font=("Arial",20))
        border.pack(fill="both",expand="yes",padx=150,pady=150)
        
        
        L4=tk.Label(border,text="ID",bg="ivory",font=("Arial Bold",15))
        L4.place(x=50,y=20)
        T4= tk.Entry(border,width=30,bd=5)
        T4.place(x=180, y=20)
       
        
        
        L1=tk.Label(border,text="Username",bg="ivory",font=("Arial Bold",15))
        L1.place(x=50,y=50)
        T1= tk.Entry(border,width=30,bd=5)
        T1.place(x=180, y=50)
        global uname
        uname = T1.get()
        
        
        L1 = tk.Label(border, text="Password",bg="ivory", font=("Arial Bold", 15))
        L1.place(x=50, y=80)
        T2 = tk.Entry(border, width=30,show='*', bd=5)
        T2.place(x=180, y=80)

        def verify():
            global uname
            uname =  T1.get()
            try:
                with open(uname+".txt", "r") as f:
                    info = f.readlines()
                    i = 0
                    for e in info:
                        d, u, p, x = e.split("$")
                        if d.strip() == T4.get() and u.strip() == T1.get() and p.strip() == T2.get(): # .strip will remove the space provided before and after the username and passwword
                            controller.show_frame(HomePage)
                            i = 1
                            break
                    if i == 0:
                        messagebox.showerror("Error", "Please provide correct username and password!")
            except:
                messagebox.showerror("Error", "Please provide correct username and password!")

        B1=tk.Button(border, text="Login", bg="Coral" , fg="black",borderwidth=4, font=("Arial", 15), command=verify)#.place(x=320, y=115)
        B1.place(x=320, y=115)
     
        def register():
            window=tk.Tk()
            window.resizable(0,0)    # to remove maximizze button
            window.configure(bg="mistyrose")  #background color of the window
            window.title("Register to BookEasy")
        
           # p2 = tk.PhotoImage(file='vase.png')
           # window.iconphoto(False, p2)
            tk.Label(window, text="Fill details for registration", bg="mistyrose", fg="black", font=90).place(x=100,y=6)
            
            l5 = tk.Label(window, text="ID:", font=("Arial", 15), bg="mistyrose")
            l5.place(x=10, y=50)
            t5 = tk.Entry(window,width=30,bd=5)
            t5.place(x=200,y=50)
            
            L1 = tk.Label(window, text="Username:", font=("Arial", 15), bg="mistyrose")
            L1.place(x=10, y=100)
            T1 = tk.Entry(window,width=30,bd=5)
            T1.place(x=200,y=100)

            l2 = tk.Label(window, text="Password:", font=("Arial", 15),bg="mistyrose")
            l2.place(x=10, y=150)
            t2 = tk.Entry(window, width=30, show="*",bd=5)
            t2.place(x=200, y=150)

            l3 = tk.Label(window, text="Confirm Password:", font=("Arial", 15), bg="mistyrose")
            l3.place(x=10,y=200)
            t3 = tk.Entry(window, width=30,show="*", bd=5)
            t3.place(x=200, y=200)
            
            l4 = tk.Label(window, text="e-mail:", font=("Arial", 15), bg="mistyrose")
            l4.place(x=10,y=250)
            t4 = tk.Entry(window, width=30, bd=5)
            t4.place(x=200, y=250)
            print(t4)
            def check():
                 global uname
                 uname = T1.get()
                 if T1.get()!="" or t2.get()!="" or t3.get()!="" or t5.get()!="":
                     if t2.get()== t3.get():
                         with open(uname+".txt","w") as f:
                             f.write(t5.get()+"$"+T1.get()+"$"+t2.get()+"$"+t4.get()+"\n")
                         
                             messagebox.showinfo("Welcome","You have registered successfully!")
                     else:
                         messagebox.showerror("Error","Your password didnt match")
                 else:
                     messagebox.showerror("Error","Please fill the complete field")
            b1=tk.Button(window, text="Register",bg="dark orange", font=("Arial" , 15), command=check)
            b1.place(x=280,y=300)
            window.geometry("500x400")   #for entry to execute
            window.mainloop()

        B2 = tk.Button(self, text="Register",bg="dark orange", font=("Arial", 15),command=register)
        B2.place(x=670, y=10)
        lb1 = tk.Label(self, text="Welcome to AtoZ Ceramics", bg="light yellow", fg="black", font=("Arial", 20),
                    height=2, width=30)
        lb1.place(x=155,y=40)

class HomePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        load = Image.open("wallpaper.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        tk.Label(self, text="Welcome to AtoZ Ceramics", fg="black", font=("Arial", 20), width=30, bg="bisque", height=2, relief="raised").place(x=185, y=60)
        tk.Button(self, text="About us",  fg="black", font=("Arial", 15), width=15, bg="mistyrose",borderwidth=6, height=2, command=lambda: controller.show_frame(AboutUsPage)).place(x=70,y=180)
        tk.Button(self, text="Profile",  fg="black", font=("Arial", 15), width=15, bg="mistyrose",borderwidth=6, height=2,command=lambda: controller.show_frame(BookAllPage)).place(x=330,y=180)
        tk.Button(self, text="Categories", fg="black", font=("Arial", 15), width=15, bg="mistyrose",borderwidth=6, height=2, command=lambda: controller.show_frame(CategoryPage)).place(x=580, y=180)
        tk.Button(self, text="My Cart", fg="black", font=("Arial", 15), width=15, bg="mistyrose",borderwidth=6, height=2, command=lambda: controller.show_frame(cart)).place(x=330, y=280)



        Button = tk.Button(self, text="Back", font=("Arial", 15),fg="black",  width=7, bg="coral", borderwidth=4, command=lambda: controller.show_frame(FirstPage))
        Button.place(x=18, y=450)
        
class bookBathroomHandpaintedCeramic(tk.Frame):


        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.configure(bg="mistyrose")
            load = Image.open("category.png")
            photo = ImageTk.PhotoImage(load)
            label = tk.Label(self, image=photo)
            label.image = photo
            label.place(x=0, y=0)
            load = Image.open("bathroomCeramicBasin1.jpg")
            photo = ImageTk.PhotoImage(load)
            label = tk.Label(self, image=photo)
            label.image = photo
            label.place(x=50, y=70)
            def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write(prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                                cart()
            prodlabel = tk.Label(self, text="Handpainted Ceramic Accessory", fg="black", font=("Arial", 15), height=1)
            prodlabel.place(x=80, y=22)
            tk.Label(self, text="Price:	₹ 1,399.00", fg="black", font=("Arial", 15), height=1).place(x=110, y=415)


            bt4 = tk.Button(self, text="Add to cart", fg="black", font=("Arial", 15), width=15, bg="mistyrose", height=1,
                             command=cartProd)  # , command=bookBathroomCeramicTiles)
            bt4.place(x=415, y=415)
            Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
            Button.place(x=600, y=20)
            lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
            lb2.place(x=450, y=60)

            lb3 = tk.Label(self, text="Material:\t\tCeramic ", fg="black", font=("Arial", 11), height=1)
            lb3.place(x=420, y=100)
            tk.Label(self, text="Usage/Application: \tHome And Hotel", fg="black",
                     font=("Arial", 11), height=1).place(x=420, y=120)
            tk.Label(self, text="Brand:\t\tPriyasha Handicrafts", fg="black",
                     font=("Arial", 11), height=1).place(x=420, y=140)
            tk.Label(self, text="Set Contains:\tSoap Dispenser, Toothbrush Holder  ", fg="black", font=("Arial", 11),
                     height=1).place(x=420, y=160)
            tk.Label(self, text="\t\tAnd Soap Case ", fg="black", font=("Arial", 11), height=1).place(
                x=420, y=180)
            tk.Label(self, text="Country of Origin:\tMade in India", fg="black", font=("Arial", 11),
                     height=1).place(
                x=420, y=200)
            tk.Label(self, text="Features: \tHand Printed", fg="black", font=("Arial", 11), height=1).place(x=420,y=220)


            Button = tk.Button(self, text="Home", bg="mistyrose", font=("Arial", 15),
                               command=lambda: controller.show_frame(HomePage))
            Button.place(x=700, y=20)

            bt7 = tk.Button(self, text="<", fg="black", bg="mistyrose", font=("Arial", 15), width=3, height=1,
                            command=lambda: controller.show_frame(secondPageBathroomCeramics))
            bt7.place(x=20, y=450)
            bt7 = tk.Button(self, text=">", fg="black", bg="mistyrose", font=("Arial", 15), width=3, height=1,
                            command=lambda: controller.show_frame(ceramicPlate))
            bt7.place(x=750, y=450)
class bookBathroomCeramicBasin(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("CeramicWashbasin1.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=50, y=68)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write(prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                                cart()
        prodlabel = tk.Label(self, text="Designer Ceramic Wash Basin", fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=80, y=22)
        tk.Label(self, text="Price:	₹ 2,800.00", fg="black", font=("Arial", 15), height=1).place(x=110, y=415)



        bt4 = tk.Button(self, text="Add to cart", fg="black", font=("Arial", 15), width=15, bg="mistyrose", height=1,
                        command=cartProd)  # , command=bookBathroomCeramicTiles)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
        lb2.place(x=450, y=60)

        lb3 = tk.Label(self, text=" Product Type:\t Art Basin ", fg="black", font=("Arial", 11), height=1)
        lb3.place(x=420, y=100)
        tk.Label(self, text="Material:\t\t Ceramic", fg="black",
                 font=("Arial", 11), height=1).place(x=420, y=120)
        tk.Label(self, text="Usage/Application: \t Home And Hotel", fg="black",
                 font=("Arial", 11), height=1).place(x=420, y=140)
        tk.Label(self, text="Brand:\t\t TOYO", fg="black",
                 font=("Arial", 11), height=1).place(x=420, y=160)
        tk.Label(self, text="ModelNumber:\t 517", fg="black", font=("Arial", 11),
                 height=1).place(x=420, y=180)
        tk.Label(self, text="Mount Type: \t Table Top", fg="black", font=("Arial", 11), height=1).place(
            x=420, y=200)
        tk.Label(self, text="Basin Shape:\t Round", fg="black", font=("Arial", 11),
                 height=1).place( x=420, y=220)

        tk.Label(self, text="Size/Dimension:\t 60x40x16 cm", fg="black", font=("Arial", 11), height=1).place(x=420, y=240)

        Button = tk.Button(self, text="Home", bg="mistyrose", font=("Arial", 15),
                           command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)

        bt7 = tk.Button(self, text="<", fg="black", bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(secondPageBathroomCeramics))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">", fg="black", bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(bookBathroomCeramicBasin))
        bt7.place(x=750, y=450)

        
class mailAll(tk.Frame):
     def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        load = Image.open("wallpaper.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        lb1=tk.Label(self, text="Check your mail for further details!", bg="light yellow", fg="black", font=("Arial",15), height=2)
        lb1.place(x=265, y=30)
        bt1=tk.Button(self, text="OK", fg="black", font=("Arial", 15), height=1, width=30, command=lambda: controller.show_frame(HomePage))
        bt1.place(x=250, y=90)
        
class bookAll(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        load = Image.open("wallpaper.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        lb1=tk.Label(self, text="Do you want to Book the all latest designer ceramics?", bg="light yellow", fg="black", font=("Arial",20), height=2)
        lb1.place(x=100, y=22)
        bt1=tk.Button(self, text="Yes", fg="black", font=("Arial", 15), height=1, command=lambda: controller.show_frame(mailAll))
        bt1.place(x=200, y=90)
        bt2=tk.Button(self, text="No", fg="black", font=("Arial", 15), height=1, command=lambda: controller.show_frame(HomePage))
        bt2.place(x=100, y=90)  
        

class showyes(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)

        load = Image.open("wallpaper.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        bt1=tk.Button(self, text="Home", bg = "mistyrose" , fg="black", font=("Arial", 15), height=1, command=lambda: controller.show_frame(HomePage))
        bt1.place(x=25, y=450)
        label1= tk.Label(self, text="Enter your email for confirmation of booking", bg="light yellow", fg="black", font=("Arial",20), height=2)
        label1.place(x=150,y=100)
        def ok_command():
            recmail=maile.get()
            server = smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login("informationatoz.ceramic@gmail.com","Booksbooks123@")
            server.sendmail("informationatoz.ceramic@gmail.com",
                recmail,
                "Thanks for Booking From AtoZ\n\
                 Visit our nearby store within 10 days for collecting your item.\n\
                 Regards,\n\
                  \t  Team AtoZ")
            server.quit()
            print(recmail)
            return None
        maile = tk.Entry(self, width=50)
        maile.place(x=250,y=200)
        bt1=tk.Button(self, text="OK", bg = "mistyrose" , fg="black", font=("Arial", 15), height=1, command=ok_command)
        bt1.place(x=730, y=450)
        
        
class bookBathroomVinylTiles(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("washbasin-500x500.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=50, y=65)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write(prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                                cart()
        prodlabel= tk.Label(self, text="Designer Wash Basin", fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=110, y=22)
        tk.Label(self, text="Price:	₹ 2,800.00", fg="black", font=("Arial", 15), height=1).place(x=110, y=415)


        bt4 = tk.Button(self, text="Add to cart", fg="black", font=("Arial", 15), width=15, bg="mistyrose", height=1,
                        command=cartProd)  # , command=bookBathroomCeramicTiles)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
        lb2.place(x=450, y=60)

        lb3 = tk.Label(self, text="Material:\t\tCeramic   ", fg="black", font=("Arial", 11), height=1)
        lb3.place(x=420, y=100)
        tk.Label(self, text="Usage/Application:   Bathroom ", fg="black",
                 font=("Arial", 11), height=1).place(x=420, y=120)
        tk.Label(self, text="Mount Type:\t Pedestal ", fg="black",
                 font=("Arial", 11), height=1).place(x=420, y=140)
        tk.Label(self, text="Basin Shape:\t Oval", fg="black",
                 font=("Arial", 11), height=1).place(x=420, y=160)
        tk.Label(self, text="Thickness:\t 20mm ", fg="black", font=("Arial", 11),
                 height=1).place(x=420, y=180)
        tk.Label(self, text="Capacity:\t\t 12L", fg="black", font=("Arial", 11), height=1).place(
            x=420, y=200)
        tk.Label(self, text="Country of Origin:\t Made in India", fg="black", font=("Arial", 11),
                 height=1).place(
            x=420, y=220)
        tk.Label(self, text="Surface Finishing Glossy ", fg="black", font=("Arial", 11), height=1).place(x=420, y=240)

        Button = tk.Button(self, text="Home", bg="mistyrose", font=("Arial", 15),
                           command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)

        bt7 = tk.Button(self, text="<", fg="black", bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(contentBathroomCeramic))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">", fg="black", bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(ceramicPlate))
        bt7.place(x=750, y=450)
        
        
class cart(tk.Frame):
    def __init__(self, parent=None, controller=None):
        global proLabel, res1
        tk.Frame.__init__(self, parent)
        self.configure(bg="mistyrose")
        load = Image.open("wallpaper.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        global products
        def search():
            f = open(uname+".txt", "r")
            word = f.readlines()
            print(word)
            '''
            text1 = {}
            text1 = word[0::]
            print(text1)
            for i in text1:
                x = text1.split("$")
            print(x)       
            '''  
            if searchentry.get() in res1:
                messagebox.showinfo("info", "product exists in cart!")
            else:
                messagebox.showinfo("info", "product does not exists in cart!")
        '''
        def search1():
                       string1 = e1.get()
                       file1 = open(uname+".txt", "r")
  

                       readfile = file1.readlines()
                       
                       readfiles = " "
                       readfiles = readfile[1::]
                       print(readfiles)
                       for i in readfiles:
                           x = readfiles.split("$")
                       print(x)  

                       if string1 == x: 
                           messagebox.showinfo("info","product in cart!")
                       else: 
                           messagebox.showinfo("info","product not in cart")

                       file1.close()
        '''   
        def open_text():
            text_file = open(uname+".txt", "r")
            global res1
        
            prodText = text_file.readlines()
            prodText
           
            print(prodText)
            prods = prodText[1::]
            strList = []
            print(prods)
            for ele in prods:
                strList.append(ele.strip('$'))
            res = list(map(lambda i: i[ : -2], strList))
            res1 = "\n".join(res)
            print(res)
            print(res1)
   
            
            def clear():
               global e1
               res = tk.messagebox.askquestion("important", "Are you sure?")
               if res =='yes':
                   proLabel.destroy()
                   lines = []

                   with open(uname+'.txt', 'r') as f:
                           lines = f.readlines()

                   with open(uname+'.txt', 'w') as f:
                           f.writelines(lines[:1] + lines[100:])
               else:
                   cart()
                           

                
                
            proLabel =  tk.Label(self, text=res1, fg="black",   font=("Arial",18))
            proLabel.place(x=250, y=140)
            butonc = tk.Button(self, text="Clear cart", bg="RosyBrown1",width=9, font=("Arial ",15), command=clear)
            butonc.place(x=680, y=400)
           # print(prodText)
            
            text_file.close()
        lbb = tk.Label(self, text="cart products", fg="black", bg="RosyBrown2", relief="ridge", font=("Arial",15),width=15, height=2)
        lbb.place(x=300, y=80)
        bt4 = tk.Button(self, text="Book", fg="black", font=("Arial", 15), width=9, bg="salmon", height=1,
                        command=lambda: controller.show_frame(showyes)) 
        bt4.place(x=680, y=450)
      
        Button = tk.Button(self, text="Home", bg="lavender blush", font=("Arial", 15),
                           command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)
        #e1 = tk.Entry(self, width=15)
        #e1.place(x=400, y=20)
        #searchbut =tk.Button(self, text="search", bg="RosyBrown3", font=("Arial ",15), command=search1)
        #scsearchbut.place(x=100, y=20) 
        buttono =  tk.Button(self, text="Update Cart", bg="RosyBrown3", font=("Arial ",15), command=open_text)
        buttono.place(x=550, y=20)
        searchentry = tk.Entry(self, width=45)
        searchentry.place(x=110, y = 30)
        searchbtn = tk.Button(self, text="Search", bg="RosyBrown3", font=("Arial", 15), height=1, command=search)
        searchbtn.place(x=390, y = 23)
        
class okButton(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        lb3 = tk.Label(self, text="  Your item is been added\n  do you wanna continue shopping or go home? ", fg="black", font=("Arial", 11), height=2)
        lb3.place(x=100, y=100)
        bt4 = tk.Button(self, text="Home", fg="black", font=("Arial", 15), width=15,bg="mistyrose", height=1,command=lambda: controller.show_frame(HomePage)) #, command=bookBathroomCeramicTiles)
        bt4.place(x=415, y=415)    
        bt4 = tk.Button(self, text="Continue shopping ", fg="black", font=("Arial", 15), width=15,bg="mistyrose", height=1,command=lambda: controller.show_frame(CategoryPage)) #, command=bookBathroomCeramicTiles)
        bt4.place(x=100, y=415)  
class bookBathroomStoneTiles(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("bathroomset.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=50, y=65)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.writelines("\n"+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                               pass
        prodlabel = tk.Label(self, text="Bathroom Accessory set", fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=110, y=22)
        tk.Label(self, text="Price:	₹ 2,800.00", fg="black", font=("Arial", 15), height=1).place(x=110, y=415)


        bt4 = tk.Button(self, text="Add to cart", fg="black", font=("Arial", 15), width=15, bg="mistyrose", height=1,
                        command= cartProd)  # , command=bookBathroomCeramicTiles)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
        lb2.place(x=450, y=60)

        lb3 = tk.Label(self, text="Material:\t\tCeramic   ", fg="black", font=("Arial", 11), height=1)
        lb3.place(x=420, y=100)
        tk.Label(self, text=" Brand:\t\tJagdamba Ceramic Handicraft", fg="black",
                 font=("Arial", 11), height=1).place(x=420, y=120)
        tk.Label(self, text=" Design:\t\tCustomize Shape and Design", fg="black",
                 font=("Arial", 11), height=1).place(x=420, y=140)
        tk.Label(self, text="Thickness:\t7mm ", fg="black", font=("Arial", 11),
                 height=1).place(x=420, y=160)
        tk.Label(self, text="Capacity:\t\t500mL", fg="black", font=("Arial", 11), height=1).place(
            x=420, y=180)
        tk.Label(self, text="Country of Origin:\tMade in India", fg="black", font=("Arial", 11),
                 height=1).place( x=420, y=200)

        tk.Label(self, text="Surface Finishing Glossy ", fg="black", font=("Arial", 11), height=1).place(x=420, y=220)

        Button = tk.Button(self, text="Home", bg="mistyrose", font=("Arial", 15),
                           command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)

        bt7 = tk.Button(self, text="<", fg="black", bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(contentBathroomCeramic))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">", fg="black", bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(ceramicPlate))
        bt7.place(x=750, y=450)
             
          
class contentBathroomCeramic(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        load = Image.open("bathroomset1.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=70, y=70)

        load = Image.open("washbasin.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=450, y=82)

        Button(self, text="       Bathroom Accessory Set             \nPrice:	₹ 1,199.00", fg="black", font=("Arial", 13),
               borderwidth=6, bg="papaya whip", height=2, command=lambda: controller.show_frame(bookBathroomStoneTiles)).place(x=70,y=375)
        Button(self, text="          Designer Wash Basin              \nPrice:	₹ 2,800.00", fg="black",font=("Arial", 13), borderwidth=6, bg="papaya whip", height=2, command=lambda: controller.show_frame(bookBathroomVinylTiles)).place(x=451, y=375)



        bt7 = tk.Button(self, text=">", bg="mistyrose", fg="black", font=("Arial", 15), width=3, height=1, command=lambda: controller.show_frame(secondPageBathroomCeramics))
        bt7.place(x=750, y=450)
        
        bt3 = tk.Button(self, text="Back", bg="coral", fg="black", font=("Arial", 15), height=1, command=lambda: controller.show_frame(CategoryPage))
        bt3.place(x=20, y=450)


class secondPageBathroomCeramics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        load = Image.open("bathroomhandwash.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=70, y=60)

        load = Image.open("CeramicWashbasin.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=450, y=69)
        # bt4 = tk.Button(self, text="\n Price  ₹2300", borderwidth=6, bg="papaya whip",
        #                 fg="black", font=("Arial", 15), width=29, height=2,
        #                 command=lambda: controller.show_frame())
        # bt4.place(x=35, y=350)
        # bt6 = tk.Button(self, text="Designer Ceramic Basin \n Price ₹5800 ", borderwidth=6, bg="papaya whip",
        #                 fg="black", font=("Arial", 15), width=20, height=2,
        #                 command=lambda: controller.show_frame())
        # bt6.place(x=450, y=350)

        Button(self, text="  Handpainted Ceramic Accessory      \nPrice:	₹ 1,399.00", fg="black",
               font=("Arial", 13),
               borderwidth=6, bg="papaya whip", height=2,
               command=lambda: controller.show_frame(bookBathroomHandpaintedCeramic)).place(x=70, y=375)
        Button(self, text="      Designer Ceramic Wash Basin     \nPrice:	₹ 2,800.00", fg="black",
               font=("Arial", 13), borderwidth=6, bg="papaya whip", height=2,
               command=lambda: controller.show_frame(bookBathroomCeramicBasin)).place(x=451, y=375)
        # def bookBathroomHandpaintedCeramic():
        #   r1 = messagebox.askyesno("BookEasy" , "Do you want to Book Handpainted Ceramic Accessory?")
        #  if r1 == 1:
        #     messagebox.showinfo("Booked successfully!", "Check your mail for further details!")

        #  def bookBathroomCeramicBasin():
        # r1 = messagebox.askyesno("BookEasy" , "Do you want to Book Designer Ceramic Basin?")
        # if r1 == 1:
        #    messagebox.showinfo("Booked successfully!", "Check your mail for further details!")

        bt3 = tk.Button(self, text="<", bg="mistyrose", fg="black", font=("Arial", 15), height=1, width=3,
                        command=lambda: controller.show_frame(contentBathroomCeramic))
        bt3.place(x=20, y=450)
        bt6 = tk.Button(self, text="Done", bg="coral", fg="black", font=("Arial", 15), height=1, width=5,
                        command=lambda: controller.show_frame(CategoryPage))
        bt6.place(x=720, y=450)

class CategoryPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="beige")

        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        lb1 = tk.Label(self, text="Categories", fg="black", font=("Arial", 30), height=2)
        lb1.place(x=270, y=2)

        load = Image.open("bathroomCeramics2.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=70, y=80)
        bathButton = tk.Button(self, text="Bathroom ceramics",bg="mistyrose", font=("Arial",10),width=30, height=1, command=lambda: controller.show_frame(contentBathroomCeramic))
        bathButton.place(x=70, y=240)
        HomeButton = tk.Button(self, text="Home",bg="mistyrose", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        HomeButton.place(x=70, y=10)

        load = Image.open("home_decor.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=400, y=85)
        homeDecorButton = tk.Button(self, text="Home decor",bg="mistyrose", width=28,font=("Arial",10), height=1,command=lambda: controller.show_frame(HomeDecorPage))
        homeDecorButton.place(x=480, y=240)

        load = Image.open("kitchen11.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=290, y=290)
        tk.Button(self, text="Kitchen ceramics",bg="mistyrose", font=("Arial",10),width=28, height=1,command=lambda: controller.show_frame(KitchenCeramicsPage)).place(x=275, y=450)

class HomeDecorPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        HomeButton = tk.Button(self, text="Back",  bg="coral", fg="black", font=("Arial", 15),command=lambda: controller.show_frame(CategoryPage))
        HomeButton.place(x=20, y=450)       
        load = Image.open("ceramicMatkaDecorationLamp1.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=70, y=70)
        
        Button(self, text="      Ceramic Matka Decoration Lamp\t\nPrice:	₹ 2,199.00", borderwidth=6, bg="papaya whip" ,font=("Arial", 14), width=28, height=2,command=lambda: controller.show_frame(ceramicMatkaDecorationLamp)).place(x=60,y=375)
        load = Image.open("plate2.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=440, y=70)
        Button(self, text="      Multi-color Ceramic Wall Plate\t \nPrice:	₹ 1,499",borderwidth=6, bg="papaya whip" ,font=("Arial", 15), width=26, height=2,
              command=lambda: controller.show_frame(ceramicPlate)).place(x=440, y=375)
        bt7 = tk.Button(self, text=">",bg="mistyrose", fg="black", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(HomeDecorPage2))
        bt7.place(x=750, y=450)
class HomeDecorPage2(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        
        load = Image.open("goldenGreenDesign1.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=70, y=70)
        Button(self, text="Gold green design ceramic home decor\t\nPrice:	₹ 1,199.00", fg="black",borderwidth=6, bg="papaya whip", font=("Arial", 12), height=2,command=lambda: controller.show_frame(goldenGreenDesign)
               ).place(x=70, y=375)
        load = Image.open("AmbriosaCollectionOfHandpaintedCeramicVase.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=460, y=70)
        Button(self, text="  Hand painted Ceramic Vase\n	Price:	₹ 2,199.00     ", fg="black", font=("Arial", 12),borderwidth=6, bg="papaya whip", height=2,command=lambda: controller.show_frame(AmbriosaCollectionOfHandpaintedCeramicVase)).place(x=462, y=375)
        bt7 = tk.Button(self, text="<", fg="black",bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(HomeDecorPage))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">", fg="black", bg="mistyrose",font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(HomeDecorPage3))
        bt7.place(x=750, y=450)
class HomeDecorPage3(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
      
        load = Image.open("Lazy French Bulldog Planter  Cute Frenchie Pot for Plants  _ Etsy1.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=85, y=70)
        Button(self, text="Leaf shaped wall hanging\n	Price:	₹ 950.00 ", fg="black", font=("Arial", 12),
              borderwidth=6, bg="papaya whip", height=2,command=lambda: controller.show_frame(wallHanging)).place(x=72, y=375)
        load = Image.open("Avon Christmas Ceramic Bell 1985 _ Etsy.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=482, y=50)
        Button(self, text="Avon Christmas Ceramic Bell\nPrice:	₹ 1,399.00", fg="black", font=("Arial", 12),borderwidth=6, bg="papaya whip", height=2,command=lambda: controller.show_frame(ChristmasBell)).place(x=480, y=385)
        bt7 = tk.Button(self, text="<", fg="black",bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(HomeDecorPage2))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">", fg="black",  bg="mistyrose",font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(HomeDecorPage4))
        bt7.place(x=750, y=450)
class HomeDecorPage4(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
    
        load = Image.open("1blue-white-ceramic-planter-medium-c.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=250, y=70)
        Button(self, text="\tBlue-white Ceramic Pot\t\nPrice:	₹ 550.00\t", fg="black", font=("Arial", 12),
               borderwidth=6, bg="papaya whip", height=2,command=lambda: controller.show_frame(HandpaintedCeramicPot)).place(x=250, y=375)
        bt7 = tk.Button(self, text="<", bg="mistyrose", fg="black", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(HomeDecorPage3))
        bt7.place(x=20, y=450)
        bt6 = tk.Button(self, text="Done",bg="coral", fg="black", font=("Arial", 15), height=1, width=5,
                        command=lambda: controller.show_frame(CategoryPage))
        bt6.place(x=720, y=450)

class ceramicMatkaDecorationLamp(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("ceramicMatkaDecorationLamp.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=50, y=70)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write('\n'+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                           pass   
                             
        prodlabel = tk.Label(self, text="Ceramic Matka Decoration Lamp", fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=80, y=22)
        tk.Label(self,text="Price:	₹ 2,199.00",fg="black", font=("Arial", 15), height=1).place(x=110,y=415)
        
        # def lamp():
        #     r1 = messagebox.askyesno("BookEasy" , "Do you want to Book Ceramic Matka Decoration Lamp? ")
        #     if r1 == 1:
        #         messagebox.showinfo("Booked successfully!", "Check your mail for further details!")
        bt4 = tk.Button(self, text="Add to cart", fg="black", font=("Arial", 15), width=15,bg="mistyrose", height=1,command=cartProd)  
        bt4.place(x=415, y=415)
        lb2 = tk.Label(self, text="Description:",fg="black", font=("Arial", 15), height=1)
        lb2.place(x=450, y=60)

        lb3=tk.Label(self,text="Colour:                  Multicolour",fg="black", font=("Arial", 11), height=1)
        lb3.place(x=420,y=100)
        tk.Label(self,text="Style:                    Unravel India Blue pottery mugal art",fg="black", font=("Arial", 11), height=1).place(x=420 ,y=120)
        tk.Label(self,text="                             ceramic matka decorative Lamp",fg="black", font=("Arial", 11), height=1).place(x=420,y=140)
        tk.Label(self,text="Brand:                  Unravel India",fg="black", font=("Arial", 11), height=1).place(x=420,y=160)
        tk.Label(self, text="Shade Material:    Ceramic, Plastic",fg="black", font=("Arial", 11), height=1).place(x=420, y=180)
        tk.Label(self, text="Shade Colour:      Black",fg="black", font=("Arial", 11), height=1).place(x=420, y=200)
        tk.Label(self, text="Specification:", fg="black", font=("Arial", 15), height=1).place(x=450,y=240)
        tk.Label(self, text="Dimensions:     lamp(H * Dia) = (11.5 * 3) Inch,",fg="black", font=("Arial", 11), height=1).place(x=420, y=280)
        tk.Label(self,text="                         shade (H * Dia) = ( 5.5 * 8) Inch,",fg="black", font=("Arial", 11), height=1).place(x=420,y=300)
        tk.Label(self, text="                         total (H * Dia) = ( 15.5 * 8)Inch", fg="black",font=("Arial", 11), height=1).place(x=420, y=320)
        tk.Label(self, text="Material :           Base: Ceramic, Shade: Plastic",fg="black", font=("Arial", 11), height=1).place(x=420, y=340)
        tk.Label(self, text="Color :               Multicolor",fg="black", font=("Arial", 11), height=1).place(x=420, y=360)
        tk.Label(self,text="About the Art :   Blue pottery from Jaipur, Rajasthan",fg="black", font=("Arial", 11), height=1).place(x=420, y=380)
        Button = tk.Button(self, text="Home",bg="mistyrose", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)


        bt7 = tk.Button(self, text="<", fg="black",bg="mistyrose", font=("Arial", 15), width=3, height=1,command=lambda: controller.show_frame(HomeDecorPage))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">", fg="black", bg="mistyrose",font=("Arial", 15), width=3, height=1,command=lambda: controller.show_frame(ceramicPlate))
        bt7.place(x=750, y=450)

class ceramicPlate(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("plate1.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=50, y=70)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write('\n'+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                                pass
        prodlabel = tk.Label(self, text="Multi-color Ceramic Wall Plate", fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=80, y=22)
        tk.Label(self, text="Price:	₹ 1,499.00", fg="black", font=("Arial", 15),  height=1).place(x=110, y=415)
        lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
        lb2.place(x=450, y=60)
        Label(self,text="Material :     Ceramic",fg="black", font=("Arial", 11), height=1).place(x=420 ,y=100)
        Label(self, text="Brand :       Kolorobia", fg="black", font=("Arial", 11), height=1).place(x=420, y=120)
        tk.Label(self, text="Specification:", fg="black", font=("Arial", 15), height=1).place(x=450, y=180)
        Label(self, text="Dimension (inches):     10 L x 1 W x 10 H", fg="black", font=("Arial", 11), height=1).place(x=420, y=220)
        Label(self, text="Pack Content :              1 Wall Plate with Hook and Stand", fg="black", font=("Arial", 11), height=1).place(x=420, y=240)
        Label(self, text="Caring Instructions :     Professional cleaning only", fg="black", font=("Arial", 11), height=1).place(x=420, y=260)

        # def plate():
        #     r1 = messagebox.askyesno("BookEasy", "Do you want to Book Multi-color Ceramic Wall Plate? ")
        #     if r1 == 1:
        #         messagebox.showinfo("Booked successfully!", "Check your mail for further details!")

        bt4 = tk.Button(self, text="Add to cart", bg="mistyrose",fg="black", font=("Arial", 15), width=15, height=1,
                        command=cartProd)  # , command=bookBathroomCeramicTiles)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        bt7 = tk.Button(self, text="<", bg="mistyrose",fg="black", font=("Arial", 15), width=3, height=1,command=lambda: controller.show_frame(HomeDecorPage))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">", bg="mistyrose",fg="black", font=("Arial", 15), width=3, height=1,command=lambda: controller.show_frame(goldenGreenDesign))
        bt7.place(x=750, y=450)
        Button = tk.Button(self, text="Home",bg="mistyrose", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)

class goldenGreenDesign(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("goldenGreenDesign.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=50, y=70)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write('\n'+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                                pass
        prodlabel = tk.Label(self, text="Gold green design ceramic home decor", fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=75, y=22)
        tk.Label(self, text="Price:	₹ 1,199.00", fg="black", font=("Arial", 15),  height=1).place(x=110, y=415)
        lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
        lb2.place(x=450, y=60)
        Label(self,text="Material:                Ceramic", fg="black", font=("Arial", 11), height=1).place(x=420 ,y=100)
        Label(self, text="Color:                    Green/Gold", fg="black", font=("Arial", 11), height=1).place(x=420, y=120)
        Label(self, text="Usage:                  Home Decorations.Gifts", fg="black", font=("Arial", 11), height=1).place(x=420, y=140)
        Label(self, text="Design Style:        Art Decor, Modern, Morden Luxury", fg="black", font=("Arial", 11), height=1).place(x=420, y=160)
        Label(self, text="Size:                     17.5*30 c", fg="black", font=("Arial", 11), height=1).place(x=420, y=180)
        tk.Label(self, text="Specification:", fg="black", font=("Arial", 15), height=1).place(x=450, y=220)
        Label(self, text="Selling Units:                   Single item", fg="black", font=("Arial", 11), height=1).place(x=420, y=260)
        Label(self, text="Single package size:      37X25X17 cm", fg="black", font=("Arial", 11), height=1).place(x=420, y=280)
        Label(self, text="Single gross weight:      0.960 kg", fg="black", font=("Arial", 11), height=1).place(x=420, y=300)
        # def plate():
        #     r1 = messagebox.askyesno("BookEasy", "Do you want to Book Gold green design ceramic home decor ")
        #     if r1 == 1:
        #         messagebox.showinfo("Booked successfully!", "Check your mail for further details!")

        bt4 = tk.Button(self, text="Add to cart",bg="mistyrose",fg="black", font=("Arial", 15), width=15, height=1,
                        command=cartProd)  # , command=bookBathroomCeramicTiles)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)

        bt7 = tk.Button(self, text="<",bg="mistyrose",fg="black", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(HomeDecorPage2))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">",bg="mistyrose", fg="black", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(AmbriosaCollectionOfHandpaintedCeramicVase))
        bt7.place(x=750, y=450)
        Button = tk.Button(self, text="Home",bg="mistyrose", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)

class AmbriosaCollectionOfHandpaintedCeramicVase(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("AmbriosaCollectionOfHandpaintedCeramicVase.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=80, y=70)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write('\n'+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                                pass
        prodlabel = tk.Label(self, text="Hand painted Ceramic Vase", fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=75, y=22)
        tk.Label(self, text="Price:	₹ 2,199.00", fg="black", font=("Arial", 15),  height=1).place(x=110,
                                                                                                                y=417)
        lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
        lb2.place(x=380, y=60)
        Label(self, text="Material:                     Ceramic", fg="black", font=("Arial", 11), height=1).place(x=380, y=100)
        Label(self, text="Color:                         Multi-color", fg="black", font=("Arial", 11), height=1).place(x=380, y=120)
        Label(self, text="Material and care:      Wipe with a clean,", fg="black", font=("Arial", 11), height=1).place(x=380, y=140)
        Label(self, text="                                   dry cloth when needed", fg="black", font=("Arial", 11), height=1).place(x=380, y=160)
        tk.Label(self, text="Specification:", fg="black", font=("Arial", 15), height=1).place(x=380, y=220)
        Label(self, text="Dimensions:            9.5cm x 9.5cm x 12cm", fg="black", font=("Arial", 11), height=1).place(x=380, y=260)
        Label(self, text="Family Name:          Ambriosa", fg="black", font=("Arial", 11), height=1).place(x=380, y=280)
        Label(self, text="Desigh:                    Floral patterns", fg="black", font=("Arial", 11), height=1).place(x=380, y=300)



        # def ambriosaVase():
        #     r1 = messagebox.askyesno("BookEasy", "Do you want to Book Ambriosa Collection Of Handpainted Ceramic Vase? ")
        #     if r1 == 1:
        #         messagebox.showinfo("Booked successfully!", "Check your mail for further details!")

        bt4 = tk.Button(self, text="Add to cart", fg="black",bg="mistyrose", font=("Arial", 15), width=15, height=1,command=cartProd)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        bt7 = tk.Button(self, text="<", fg="black",bg="mistyrose",font=("Arial", 15), width=3, height=1,command=lambda: controller.show_frame(HomeDecorPage2))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">", fg="black",bg="mistyrose", font=("Arial", 15), width=3, height=1,command=lambda: controller.show_frame(HandpaintedCeramicPot))
        bt7.place(x=750, y=450)
        Button = tk.Button(self, text="Home", bg="mistyrose",font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)

class HandpaintedCeramicPot(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("blue-white-ceramic-planter-medium-c.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=50, y=70)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write('\n'+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                                pass
        prodlabel = tk.Label(self, text="Blue-white Ceramic Pot", fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=75, y=22)
        tk.Label(self, text="Price:	₹ 550.00", fg="black", font=("Arial", 15),  height=1).place(x=110,y=417)

        lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
        lb2.place(x=450, y=60)
        Label(self, text="Material:                    Ceramic", fg="black", font=("Arial", 11), height=1).place(x=420, y=100)
        Label(self, text="Usage/Application:    Exterior Decor", fg="black", font=("Arial", 11), height=1).place(x=420,y=120)
        Label(self, text="Color:	                  Blue-white", fg="black", font=("Arial", 11), height=1).place(x=420, y=140)
        Label(self, text="Pattern:  	                  Designer", fg="black", font=("Arial", 11), height=1).place(x=420, y=160)
        tk.Label(self, text="Specification:", fg="black", font=("Arial", 15), height=1).place(x=450, y=200)
        Label(self, text="Dimensions:    12'' diam, 8 1/4'' high.", fg="black", font=("Arial", 11), height=1).place(x=420, y=240)
        Label(self, text="\n*This planter does not include any drainage holes", fg="black", font=("Arial", 11), height=2).place(x=420, y=260)
        Label(self, text="*Designed for indoor and outdoor use.", fg="black", font=("Arial", 11), height=1).place(x=420, y=300)


        # def ceramicPot():
        #     r1 = messagebox.askyesno("BookEasy", "Do you want to Book Hand painted Ceramic Pot?")
        #     if r1 == 1:
        #         messagebox.showinfo("Booked successfully!", "Check your mail for further details!")

        bt4 = tk.Button(self, text="Add to cart",bg="mistyrose", fg="black", font=("Arial", 15), width=15, height=1,command=cartProd)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        bt7 = tk.Button(self, text="<", bg="mistyrose",fg="black", font=("Arial", 15), width=3, height=1,command=lambda: controller.show_frame(HomeDecorPage4))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">",bg="mistyrose", fg="black", font=("Arial", 15), width=3, height=1,command=lambda: controller.show_frame(wallHanging))
        bt7.place(x=750, y=450)
        Button = tk.Button(self, text="Home",bg="mistyrose", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)

class wallHanging(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("Lazy French Bulldog Planter  Cute Frenchie Pot for Plants  _ Etsy1.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=70, y=60)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write('\n'+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                                pass
        prodlabel = tk.Label(self, text="Leaf shaped wall hanging", fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=75, y=22)
        tk.Label(self, text="Price:	₹ 950.00", fg="black", font=("Arial", 15),  height=1).place(x=95,y=417)

        lb2 = tk.Label(self, text="Description:", fg="black",font=("Arial", 15), height=1)
        lb2.place(x=380, y=60)
        Label(self, text="Material:                    Ceramic", fg="black", font=("Arial", 11), height=1).place(x=350, y=100)
        Label(self, text="Usage/Application:    Exterior Decor", fg="black", font=("Arial", 11), height=1).place(x=350,y=120)
        Label(self, text="Pattern:  	                  Designer", fg="black", font=("Arial", 11), height=1).place(x=350, y=140)

        tk.Label(self, text="Specification:", fg="black", font=("Arial", 15), height=1).place(x=350, y=180)
        Label(self, text="Dimensions :          Picture Frame : 18 cm x 1 cm x 35 cm", fg="black", font=("Arial", 11),height=1).place(x=350, y=220)
        Label(self, text="Set Size :               Single Pc.", fg="black", font=("Arial", 11), height=1).place(x=350,y=240)
        Label(self, text="Care Instructions : Wipe with damp cloth to remove stains & dirt.", fg="black", font=("Arial", 11), height=1).place(x=350, y=260)

        # def ceramicPot():
        #     r1 = messagebox.askyesno("BookEasy", "Do you want to Book Leaf shaped wall hanging?")
        #     if r1 == 1:
        #         messagebox.showinfo("Booked successfully!", "Check your mail for further details!")

        bt4 = tk.Button(self, text="Add to cart", bg="mistyrose",fg="black", font=("Arial", 15), width=15, height=1, command=cartProd)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        bt7 = tk.Button(self, text="<",bg="mistyrose", fg="black", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(HomeDecorPage3))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">",bg="mistyrose", fg="black", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(ChristmasBell))
        bt7.place(x=750, y=450)
        Button = tk.Button(self, text="Home",bg="mistyrose", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)
class ChristmasBell(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("Avon Christmas Ceramic Bell 1985 _ Etsy.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=80, y=70)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write('\n'+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                                pass
        prodlabel = tk.Label(self, text="Avon Christmas Ceramic Bell", fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=75, y=22)
        tk.Label(self, text="Price:	₹ 1399.00", fg="black", font=("Arial", 15),  height=1).place(x=95,y=417)
        lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
        lb2.place(x=380, y=60)
        Label(self, text="Material:                    Ceramic,wood", fg="black", font=("Arial", 11), height=1).place(x=380, y=100)
        Label(self, text="Set Size :                  Single Pc.", fg="black", font=("Arial", 11), height=1).place(x=380, y=120)
        Label(self, text="Material and care:     Wipe with a clean,", fg="black", font=("Arial", 11), height=1).place(x=380, y=140)
        Label(self, text="                                  dry cloth when needed", fg="black", font=("Arial", 11),height=1).place(x=380, y=160)
        tk.Label(self, text="Specification:", fg="black", font=("Arial", 15), height=1).place(x=380, y=200)
        Label(self, text="Dimensions:            9.5cm x 9.5cm x 12cm", fg="black", font=("Arial", 11), height=1).place(x=380, y=240)
        Label(self, text="Family Name:          Avon", fg="black", font=("Arial", 11), height=1).place(x=380, y=260)
        Label(self, text="Design:                   Christmas pattern ", fg="black", font=("Arial", 11), height=1).place(x=380, y=280)

        # def bell():
        #     r1 = messagebox.askyesno("BookEasy", "Do you want to Book Avon Christmas Bell?")
        #     if r1 == 1:
        #         messagebox.showinfo("Booked successfully!", "Check your mail for further details!")

        bt4 = tk.Button(self, text="Add to cart", bg="mistyrose",fg="black", font=("Arial", 15), width=15, height=1, command=cartProd)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        bt7 = tk.Button(self, text="<", fg="black",bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(HomeDecorPage3))
        bt7.place(x=20, y=450)

        Button = tk.Button(self, text="Home", bg="mistyrose",font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)
class KitchenCeramics1(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        HomeButton = tk.Button(self, text="Home", bg="mistyrose", font=("Arial", 15),command=lambda: controller.show_frame(HomePage))
        HomeButton.place(x=70, y=10)
        load = Image.open("11dinner_set.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=70, y=70)
        Button(self, text="  Blue and White Floral\n\t Ceramic Dinner Set\t\nPrice:	₹ 2,499.00", fg="black", font=("Arial", 13), borderwidth=6, bg="papaya whip" , height=3,command=lambda: controller.show_frame(DinnerSet)).place(x=70,y=375)
        load = Image.open("SaltAndPepperShakers1.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=440, y=70)
        Button(self, text="      Ceramic Salt and Pepper Shakers\t \nPrice:	₹ 799", fg="black", font=("Arial", 12),
              borderwidth=6, bg="papaya whip" , height=3,command=lambda: controller.show_frame(CeramicShakers)).place(x=440, y=375)
        bt7 = tk.Button(self, text=">", fg="black",bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(KitchenCeramicsPage2))
        bt7.place(x=750, y=450)
        bt7 = tk.Button(self, text="<", fg="black", bg="mistyrose",font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(KitchenCeramicsPage))
        bt7.place(x=20, y=450)
class KitchenCeramic2(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        HomeButton = tk.Button(self, text="Home", bg="mistyrose", font=("Arial", 15),command=lambda: controller.show_frame(HomePage))
        HomeButton.place(x=70, y=10)
        load = Image.open("ceramicTeaPot.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=210, y=70)
        Button(self, text="\t      Royal   Brown  Tea   Pot\t\t\n     Price:  	₹ 1,999.00\t", fg="black", font=("Arial", 12),
             borderwidth=6, bg="papaya whip" , height=3,command=lambda: controller.show_frame(CeramicTeapot)).place(x=210, y=355)
        bt7 = tk.Button(self, text="<", fg="black", font=("Arial", 15), bg="mistyrose",width=3, height=1,
                        command=lambda: controller.show_frame(KitchenCeramicsPage2))
        bt7.place(x=20, y=450)
        bt6 = tk.Button(self, text="Done",bg="mistyrose", fg="black", font=("Arial", 15), height=1, width=5,
                        command=lambda: controller.show_frame(CategoryPage))
        bt6.place(x=720, y=450)
class KitchenCeramicsPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        HomeButton = tk.Button(self, text="Back", bg="coral",  font=("Arial", 15),command=lambda: controller.show_frame(HomePage))
        HomeButton.place(x=30, y=440)
        load = Image.open("tea_set11.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=70, y=70)
        Button(self, text="  Red Hand Painted Ceramic Tea Set\t\nPrice:	₹ 1350.00", fg="black", font=("Arial", 13), borderwidth=6, bg="papaya whip" , height=2,command=lambda: controller.show_frame(Teapotset)).place(x=70,y=375)
        load = Image.open("1moroccan-plate-pair-ceramic-handpainted-rice-platter-cum-dinner-original-imag3yangdzgamzg.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=440, y=70)
        Button(self, text="Moroccan plate pair ceramic \n\thand painted rice platter\t \nPrice:	₹ 899.00", fg="black", font=("Arial", 12),
               borderwidth=6, bg="papaya whip" ,height=3,command=lambda: controller.show_frame(CeramicPlate)).place(x=441, y=375)
        bt7 = tk.Button(self, text=">",bg="mistyrose", fg="black", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(KitchenCeramics1))
        bt7.place(x=750, y=450)
class KitchenCeramicsPage2(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        HomeButton = tk.Button(self, text="Home", bg="mistyrose", font=("Arial", 15),command=lambda: controller.show_frame(HomePage))
        HomeButton.place(x=70, y=10)
        load = Image.open("ceramicGlasses1.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=70, y=70)
        Button(self, text="  Ceramic Chai Glasses with stand\t\nPrice:	₹ 1,999.00", fg="black", font=("Arial", 13), borderwidth=6, bg="papaya whip" , height=3,command=lambda: controller.show_frame(CeramicTeaGlasses)).place(x=70,y=375)
        load = Image.open("measuringSpoons1.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=440, y=70)
        Button(self, text="           Fancy fruit measuring spoons          \nPrice:	₹ 1,099.00", fg="black", font=("Arial", 12),
                borderwidth=6, bg="papaya whip" , height=3,command=lambda: controller.show_frame(MeasuringSpoons)).place(x=441, y=375)
        #bt7 = tk.Button(self, text=">", fg="black", font=("Arial", 15), width=3, height=1,
         #               command=lambda: controller.show_frame(HomeDecorPage2))
        #bt7.place(x=750, y=450)
        bt7 = tk.Button(self, text="<", fg="black",bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(KitchenCeramics1))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">", fg="black", bg="mistyrose",font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(KitchenCeramic2))
        bt7.place(x=750, y=450)
class Teapotset(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("tea_set1.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=50, y=70)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write('\n'+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                              pass
        prodlabel = tk.Label(self, text="Red Hand Painted Ceramic Tea Set", fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=55, y=22)
        tk.Label(self, text="Price:	₹ 1350.00", fg="black", font=("Arial", 15),  height=1).place(x=95,y=417)
        lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
        lb2.place(x=450, y=60)
        Label(self, text="Material:\t\t\tCeramic", fg="black", font=("Arial", 11), height=1).place(x=420, y=100)
        Label(self, text="Dimension of Tray:\t\t10 L x 1.5 H", fg="black", font=("Arial", 11), height=1).place(x=420,y=120)
        Label(self, text="Capacity of Kettle:\t\t 575 ml", fg="black", font=("Arial", 11), height=1).place(x=420, y=140)
        Label(self, text="Brand:\t\t\tHindustani Saudagar", fg="black", font=("Arial", 11), height=1).place(x=420, y=160)
        Label(self, text="Dimension of Kettle(inches):  4 L x 5.5 H", fg="black", font=("Arial", 11), height=1).place(x=420, y=180)
        Label(self, text="Dimension of Cups:\t2 L x 3 H", fg="black", font=("Arial", 11), height=1).place(x=420, y=200)
        Label(self, text="Capacity of Cups:\t\t120 ml", fg="black", font=("Arial", 11), height=1).place(x=420, y=220)
        Label(self, text="Pack Content:\t\t1 Kettle, 1 Tray, 4 Cups", fg="black", font=("Arial", 11), height=1).place(x=420,y=240)

        # def teapot():
        #     r1 = messagebox.askyesno("BookEasy", "Do you want to Book Red Hand Painted Ceramic Tea Set?")
        #     if r1 == 1:
        #         messagebox.showinfo("Booked successfully!", "Check your mail for further details!")

        bt4 = tk.Button(self, text="Add to cart", fg="black",bg="mistyrose", font=("Arial", 15), width=15, height=1, command=cartProd)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        bt7 = tk.Button(self, text="<", fg="black",bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(KitchenCeramicsPage))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">", fg="black",bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(CeramicPlate))
        bt7.place(x=750, y=450)
        Button = tk.Button(self, text="Home",bg="mistyrose", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)
class CeramicPlate(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("moroccan-plate-pair-ceramic-handpainted-rice-platter-cum-dinner-original-imag3yangdzgamzg.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=50, y=70)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write('\n'+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                                pass
        prodlabel = tk.Label(self, text="Moroccan plate pair ceramic hand painted rice platter", fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=55, y=22)
        tk.Label(self, text="Price:	₹ 899.00", fg="black", font=("Arial", 15),  height=1).place(x=95,y=417)
        lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
        lb2.place(x=450, y=80)
        Label(self, text="Material:\t\t Ceramic", fg="black", font=("Arial", 11), height=1).place(x=420, y=120)
        Label(self, text="Dimension(inch):\t 10.4 L x 7.2 W x 1.2 H", fg="black", font=("Arial", 11), height=1).place(x=420, y=140)
        Label(self, text="Pack Content:\t 2 Platter Plates", fg="black", font=("Arial", 11), height=1).place(x=420, y=180)
        Label(self, text="Caring Instructions:\t Professional cleaning only", fg="black", font=("Arial", 11), height=1).place(x=420, y=200)
        Label(self, text="Color:\t\t Multi-color", fg="black", font=("Arial", 11), height=1).place(x=420, y=220)
        # def Moroccan_plate():
        #     r1 = messagebox.askyesno("BookEasy", "Do you want to Book Moroccan plate pair ceramic hand painted rice platter?")
        #     if r1 == 1:
        #         messagebox.showinfo("Booked successfully!", "Check your mail for further details!")

        bt4 = tk.Button(self, text="Add to cart", fg="black",bg="mistyrose", font=("Arial", 15), width=15, height=1, command=cartProd)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        bt7 = tk.Button(self, text="<", fg="black",bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(KitchenCeramicsPage))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">",bg="mistyrose", fg="black", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(DinnerSet))
        bt7.place(x=750, y=450)
        Button = tk.Button(self, text="Home",bg="mistyrose", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)

class DinnerSet(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("dinner_set.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=40, y=70)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write('\n'+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                                pass
        prodlabel = tk.Label(self, text="Blue and White Floral Ceramic Dinner Set",fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=45, y=22)
        tk.Label(self, text="Price:	₹ 2,499.00", fg="black", font=("Arial", 15), height=1).place(x=95,y=417)
        lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
        lb2.place(x=440, y=80)
        Label(self, text="Material:\t\t        Ceramic", fg="black", font=("Arial", 11), height=1).place(x=410, y=120)
        Label(self, text="Sales Package:\t        4 full plates, 4 quarter plates & ", fg="black", font=("Arial", 11), height=1).place(x=410, y=140)
        Label(self, text="\t\t        & 4 bowls", fg="black", font=("Arial", 11),height=1).place(x=410, y=160)
        Label(self, text="Design:\t\t        Floral", fg="black", font=("Arial", 11), height=1).place(x=410, y=180)
        Label(self, text="Convenience Features:  Dishwasher Safe, ", fg="black", font=("Arial", 11), height=1).place(x=410, y=200)
        Label(self, text="\t\t        Microwave Safe", fg="black", font=("Arial", 11),height=1).place(x=410, y=220)
        Label(self, text="Width:\t\t        Plate: 10 inch,Bowl: 4 inch,", fg="black", font=("Arial", 11), height=1).place(x=410, y=240)
        Label(self, text="\t\t        Quarter Plate: 7 inch ", fg="black", font=("Arial", 11), height=1).place(x=410, y=260)
        #Label(self, text="Width:\tPlate: 10 inch,   Quarter Plate: 7 inch,", fg="black", font=("Arial", 11), height=1).place(x=410, y=240), height=1).place(x=410, y=260)
        #Label(self, text="\t\t\tBowl: 4 inch", fg="black", font=("Arial", 11), height=1).place(x=410, y=240), height=1).place(x=410, y=260)
        Label(self, text="Height:\t\t        Plate: 0.5 inch, Bowl: 2 inch ,", fg="black", font=("Arial", 11), height=1).place(x=410 ,y=280)
        Label(self, text="\t\t        Quarter Plate: 0.5 inch", fg="black", font=("Arial", 11), height=1).place(x=410, y=300)
        Label(self, text="Depth:\t\t        Bowl: 2 inch", fg="black", font=("Arial", 11), height=1).place(x=410, y=320)
        Label(self, text="Diameter:\t        Full Plate: 10 inch, ", fg="black", font=("Arial", 11), height=1).place(x=410, y=340)
        Label(self, text="Quarter Plate:\t        7 inch, Bowl: 4 inch", fg="black",
              font=("Arial", 11), height=1).place(x=410, y=360)
        # def dinnerSet():
        #     r1 = messagebox.askyesno("BookEasy", "Do you want to Book Blue and White Floral Ceramic Dinner Set?")
        #     if r1 == 1:
        #         messagebox.showinfo("Booked successfully!", "Check your mail for further details!")

        bt4 = tk.Button(self, text="Add to cart",bg="mistyrose", fg="black", font=("Arial", 15), width=15, height=1, command=cartProd)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        bt7 = tk.Button(self, text="<", bg="mistyrose",fg="black", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(KitchenCeramics1))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">",bg="mistyrose", fg="black", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(CeramicTeapot))
        bt7.place(x=750, y=450)
        Button = tk.Button(self, text="Home",bg="mistyrose", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)

class CeramicTeapot(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("ceramicTeaPot.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=30, y=90)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write('\n'+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                               pass
        prodlabel = tk.Label(self, text="Royal Brown Tea Pot", fg="black",font=("Arial", 15), height=1)
        prodlabel.place(x=105, y=42)
        tk.Label(self, text="Price:	₹ 1,999.00", fg="black", font=("Arial", 15),  height=1).place(x=95,y=380)
        lb2 = tk.Label(self, text="Description:",fg="black", font=("Arial", 15), height=1)
        lb2.place(x=440, y=80)
        Label(self, text="Material:\t\t\tCeramic", fg="black", font=("Arial", 11), height=1).place(x=420, y=120)
        Label(self, text="Dimension of Tray:\t\t10 L x 1.5 H", fg="black", font=("Arial", 11), height=1).place(x=420,y=140)
        Label(self, text="Capacity of Kettle:\t\t 575 ml", fg="black", font=("Arial", 11), height=1).place(x=420, y=160)
        Label(self, text="Brand:\t\t\tHindustani Saudagar", fg="black", font=("Arial", 11), height=1).place(x=420,y=180)
        Label(self, text="Dimension of Kettle(inches):  4 L x 5.5 H", fg="black", font=("Arial", 11), height=1).place(x=420, y=200)
        #Label(self, text="Dimension of Cups:\t2 L x 3 H", fg="black", font=("Arial", 11), height=1).place(x=420, y=200)2
        #Label(self, text="Capacity of Cups:\t\t120 ml", fg="black", font=("Arial", 11), height=1).place(x=420, y=220)
        Label(self, text="Pack Content:\t\t1 Kettle", fg="black", font=("Arial", 11), height=1).place( x=420, y=220)

        # def Ceramicteapot():
        #     r1 = messagebox.askyesno("BookEasy", "Do you want to Book Royal Brown Tea Pot?")
        #     if r1 == 1:
        #         messagebox.showinfo("Booked successfully!", "Check your mail for further details!")

        bt4 = tk.Button(self, text="Add to cart", fg="black",bg="mistyrose", font=("Arial", 15), width=15, height=1, command=cartProd)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        bt7 = tk.Button(self, text="<", fg="black",bg="mistyrose", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(KitchenCeramics1))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">", fg="black", bg="mistyrose",font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(CeramicTeaGlasses))
        bt7.place(x=750, y=450)
        Button = tk.Button(self, text="Home",bg="mistyrose", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)

class CeramicShakers(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("SaltAndPepperShakers.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=40, y=70)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write('\n'+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                                pass
        prodlabel = tk.Label(self, text="Ceramic Salt & Pepper Shakers", fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=65, y=30)
        tk.Label(self, text="Price:	₹ 799.00", fg="black", font=("Arial", 15),height=1).place(x=95,y=417)
        lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
        lb2.place(x=440, y=80)
        Label(self, text="Material:\t\t          Ceramic", fg="black", font=("Arial", 11), height=1).place(x=410, y=120)
        Label(self, text="Brand:\t\t          ExclusiveLane", fg="black", font=("Arial", 11), height=1).place(x=410, y=140)
        Label(self, text="Colour:\t\t          White and Brown", fg="black", font=("Arial", 11), height=1).place(x=410, y=160)
        Label(self, text="Dimensions(In Inches):     Length: 2.3, Height: 2.6", fg="black", font=("Arial", 11), height=1).place(x=410, y=180)
        Label(self, text="Weight: \t\t          500 Grams", fg="black", font=("Arial", 11), height=1).place(x=410, y=200)
        Label(self, text="Pack Content:\t          1 Salt & 1 Pepper Shaker", fg="black", font=("Arial", 11), height=1).place(x=410, y=220)
        #Label(self, text="Weight: 500 Grams", fg="black", font=("Arial", 11), height=1).place(x=410, y=120)
        # def shakers():
        #     r1 = messagebox.askyesno("BookEasy", "Do you want to Book Ceramic Salt & Pepper Shakers?")
        #     if r1 == 1:
        #         messagebox.showinfo("Booked successfully!", "Check your mail for further details!")

        bt4 = tk.Button(self, text="Add to cart",bg="mistyrose", fg="black", font=("Arial", 15), width=15, height=1, command=cartProd)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        bt7 = tk.Button(self, text="<",bg="mistyrose", fg="black", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(KitchenCeramics1))
        bt7.place(x=20, y=450)
        Button = tk.Button(self, text="Home",bg="mistyrose", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)
class CeramicTeaGlasses(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("ceramicGlasses.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=40, y=70)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write('\n'+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                             pass
        prodlabel = tk.Label(self, text="Ceramic Chai Glasses with stand", fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=65, y=30)
        tk.Label(self, text="Price:	₹ 1,999.00", fg="black", font=("Arial", 15),  height=1).place(x=95,y=417)
        lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
        lb2.place(x=440, y=80)
        Label(self, text="Material:\t            Ceramic", fg="black", font=("Arial", 11), height=1).place(x=410, y=120)
        Label(self, text="Dimension:          20.5x12x16.5 cm", fg="black", font=("Arial", 11), height=1).place(x=410,y=140)
        Label(self, text="No. of glasses:    6", fg="black", font=("Arial", 11), height=1).place(x=410, y=160)
        Label(self, text="Product:\t            Each glass holds 120 ml of chai, ", fg="black", font=("Arial", 11), height=1).place(x=410,y=180)
        Label(self, text="\t            ready to be served . It comes with ", fg="black", font=("Arial", 11), height=1).place(x=410, y=200)
        Label(self, text="\t            a cute stand, which adds to the beauty.", fg="black",font=("Arial", 11), height=1).place(x=410, y=220)
        Label(self, text="Weight:\t            800 gram", fg="black", font=("Arial", 11), height=1).place(x=410, y=245)
        Label(self, text="Design:\t            Replace your standard shot glasses and ", fg="black", font=("Arial", 11), height=1).place(x=410, y=270)
        Label(self, text="\t            dessert cups with these unique chai ", fg="black", font=("Arial", 11), height=1).place( x=410, y=290)
        Label(self, text="\t            glasses that will delight your guests.", fg="black", font=("Arial", 11), height=1).place(x=410, y=310)
        Label(self, text="\t            Perfect for small tastings and desserts.", fg="black", font=("Arial", 11),height=1).place(x=410, y=330)

        # def TeaGlasses():
        #     r1 = messagebox.askyesno("BookEasy", "Do you want to Book Ceramic Chai Glasses with stand?")
        #     if r1 == 1:
        #         messagebox.showinfo("Booked successfully!", "Check your mail for further details!")

        bt4 = tk.Button(self, text="Add to cart", fg="black",bg="mistyrose", font=("Arial", 15), width=15, height=1, command=cartProd)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        bt7 = tk.Button(self, text="<", fg="black", bg="mistyrose",font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(KitchenCeramicsPage2))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">", fg="black", bg="mistyrose",font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(MeasuringSpoons))
        bt7.place(x=750, y=450)
        Button = tk.Button(self, text="Home",bg="mistyrose", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)
class MeasuringSpoons(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        load = Image.open("measuringSpoons.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=40, y=70)
        def cartProd():
                    prodName = prodlabel.cget("text")
                    with open(uname+'.txt', 'a') as file:  
                            file.write('\n'+prodName+'$'+'\n')
                            print(prodName)
                            file.close()
                    if(tk.messagebox.showinfo("message","added to cart")):
                               pass
        prodlabel = tk.Label(self, text="Fancy fruit measuring spoons",fg="black", font=("Arial", 15), height=1)
        prodlabel.place(x=80, y=42)
        tk.Label(self, text="Price:	₹ 1,099.00", fg="black", font=("Arial", 15),  height=1).place(x=95,y=417)
        lb2 = tk.Label(self, text="Description:", fg="black", font=("Arial", 15), height=1)
        lb2.place(x=420, y=80)
        Label(self, text="Material:\t\t      Ceramic", fg="black", font=("Arial", 11), height=1).place(x=380, y=120)
        Label(self, text="Dimension:\t      5L inches.", fg="black", font=("Arial", 11), height=1).place(x=380, y=140)
        tk.Label(self, text="Specification:", fg="black", font=("Arial", 15), height=1).place(x=400, y=180)
        Label(self, text="Product:\t\t      Authentic Fair Trade Product.", fg="black", font=("Arial", 11), height=1).place(x=380, y=220)
        Label(self, text="\t\t      Ethically sourced and 100% handmade.", fg="black",font=("Arial", 11), height=1).place(x=380, y=240)
        Label(self, text="Care and instructions:  Dishwasher safe.", fg="black", font=("Arial", 11), height=1).place(x=380, y=260)
        Label(self, text="Pack Contains:\t      tablespoon, teaspoon, ", fg="black", font=("Arial", 11), height=1).place(x=380,y=280)

        Label(self, text="\t\t     1/2 teaspoon,1/4 teaspoon ", fg="black", font=("Arial", 11), height=1).place(x=380, y=300)
        Label(self, text="\t\t     measurements are approximate.", fg="black", font=("Arial", 11), height=1).place(x=380, y=320)
        #Label(self, text="Pack Content:\t\t1 Kettle", fg="black", font=("Arial", 11), height=1).place( x=420, y=360)

        # def MeasuringSpoons():
        #     r1 = messagebox.askyesno("BookEasy", "Do you want to Book Fancy fruit measuring spoons?")
        #     if r1 == 1:
        #         messagebox.showinfo("Booked successfully!", "Check your mail for further details!")
        bt4 = tk.Button(self, text="Add to cart", fg="black",bg="mistyrose", font=("Arial", 15), width=15, height=1, command=cartProd)
        bt4.place(x=415, y=415)
        Button = tk.Button(self, text="Book", bg="coral", font=("Arial", 15), command=lambda: controller.show_frame(showyes))
        Button.place(x=600, y=20)
        bt7 = tk.Button(self, text="<", bg="mistyrose",fg="black", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(KitchenCeramicsPage2))
        bt7.place(x=20, y=450)
        bt7 = tk.Button(self, text=">", bg="mistyrose",fg="black", font=("Arial", 15), width=3, height=1,
                        command=lambda: controller.show_frame(CeramicShakers))
        bt7.place(x=750, y=450)
        Button = tk.Button(self, text="Home",bg="mistyrose", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=20)

class AboutUsPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("wallpaper.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        l2 = tk.Label(self, text="About us", font=("Arial", 25), bg="burlywood", relief="groove")
        l2.place(x=10, y=100)
        l3 = tk.Label(self, text="Hey customer, this software is used to book the latest designer ceramics before", font=("Arial", 15), bg="mistyrose")
        l4 = tk.Label(self, text= " it is even introduced in our AtoZ store, so you wouldnt have to worry about running out", font=("Arial", 15), bg="mistyrose")
        l5 = tk.Label(self, text=   "of the latest designer ware.", font=("Arial", 15), bg="mistyrose")
        l6 = tk.Label(self, text= " Contact us : informationatoz.ceramic@gmail.com for any queiries", font=("Arial", 15), bg="seashell", relief="raised")
        l3.place(x=20, y=200)
        l4.place(x=20, y=250)
        l5.place(x=20, y=300)
        l6.place(x=20, y=350)
        Button = tk.Button(self, text="Home",fg="black",  width=7, bg="coral", borderwidth=4, font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=450)



class BookAllPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="mistyrose")
        load = Image.open("wallpaper.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        Button = tk.Button(self, text="Home",bg="mistyrose",borderwidth=4, width=7,font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=700, y=450)
        #l2 = tk.Label(self, text="Your Details", font=("Arial", 15), bg="mistyrose")
        #l2.place(x=100, y=100)
        #Lb.place(x=120,y=150)
   
        
                
        def openi():
            global idi
            global name
            global passw
            global ema
            global f
            global lines
            global text1
            global x
            global i
            global selection
            global entryvar
            f = open(uname+".txt", "r")
            lines = f.readlines()
            print(lines)       
            text1 = {}
            text1 = lines[0]
            print(text1)
            for i in text1:
                x = text1.split("$")
            print(x)           
            idi = x[0]
            name = x[1]
            passw = x[2]
            ema = x[3]
            
            global Lb
            Lb = tk.Listbox(self, selectmode="SINGLE", width=15, font=("Arial", 20), height=4, fg="coral",bd=2,relief="raised", bg="ivory")
            Lb.place(x=330, y= 200)
            Lb.insert(1, idi)
            Lb.insert(2, name)
            Lb.insert(3, passw)
            Lb.insert(4, ema)
        def updatephno():
                text_file = open(uname+".txt", "r")          
                prodText = text_file.readline()
                print(prodText)
                for i in prodText:
                    x = prodText.split("$")
                print(x)
                print(x[3])
                e8 = tk.Entry(self, bd = 1, width= 15)
                e8.place(x=330, y = 390)
                global entryvar
                entryvar = e8.get()
                print(entryvar)
                for q in Lb.curselection():
                       entr =  Lb.get(q)
                       print(entr)
                selection = Lb.curselection()
                print(selection)
                if selection == (3,):
                         print("fourthline")
                         with open(uname+'.txt', 'r') as original: data = original.read()
                         with open(uname+'.txt', 'a+') as modified: modified.write("\n"+(data.replace(ema, entryvar)))
        Button = tk.Button(self, text="Your details ", font=("Arial", 15),  bg="coral", borderwidth=6,command=openi)
        Button.place(x=350, y=20)
        l2 = tk.Label(self, text="ID   ", font=("Arial", 15),  bg="ivory", relief="groove", fg="RosyBrown3")
        l2.place(x=220, y=210)
        l3 = tk.Label(self, text="Name   ", font=("Arial", 15),  bg="ivory", relief="groove", fg="RosyBrown3")
        l3.place(x=220, y=240)
        l4 = tk.Label(self, text="Password   ", font=("Arial", 15),  bg="ivory", relief="groove", fg="RosyBrown3")
        l4.place(x=220, y=270)
        l5 = tk.Label(self, text="phno", font=("Arial", 15),  bg="ivory", relief="groove", fg="RosyBrown3")
        l5.place(x=220, y=300)
        updatebtn = tk.Button(self, text="Update my Phone Num", bg="RosyBrown3", font=("Arial", 15), height=1, command=updatephno)
        updatebtn.place(x=100, y =450)
class Application(tk.Tk):
    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        window=tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0,minsize=500)
        window.grid_columnconfigure(0,minsize=800)
        self.frames= {}
        for F in (FirstPage,HomePage,CategoryPage,cart,okButton,  AboutUsPage,KitchenCeramicsPage,CeramicShakers,bookBathroomStoneTiles, KitchenCeramic2,KitchenCeramicsPage2,KitchenCeramics1,DinnerSet,CeramicPlate,MeasuringSpoons,CeramicTeaGlasses,Teapotset,CeramicTeapot,BookAllPage,wallHanging,HomeDecorPage2,HomeDecorPage3,HomeDecorPage4, ChristmasBell,AmbriosaCollectionOfHandpaintedCeramicVase,HandpaintedCeramicPot,secondPageBathroomCeramics,ceramicPlate,goldenGreenDesign,ceramicMatkaDecorationLamp, bookBathroomCeramicBasin,contentBathroomCeramic,bookAll,mailAll,HomeDecorPage, bookBathroomVinylTiles,bookBathroomHandpaintedCeramic,showyes): #bookBathroomHandpaintedCeramic, bookBathroomVinylTiles,bookBathroomStoneTiles,bookBathroomCeramicTiles,
            frame= F(window, self)
            self.frames[F]=frame
            frame.grid(row=0,column=0, sticky="nsew")
            self.title('BookEasy',)
            p1 = tk.PhotoImage(file='vase.png')
            self.iconphoto(False, p1)

        self.show_frame(FirstPage)

    def show_frame(self,page):
            frame = self.frames[page]
            frame.tkraise()
app= Application()
app.maxsize(850,550)
app.mainloop()

