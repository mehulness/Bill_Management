from tkinter import *
import math,random,os
import tkinter.messagebox

class Bill_App:

    def __init__(self,root):

        self.root = root
        self.root.iconbitmap(r'icon.ico')
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = '#212121'
        title = Label(self.root,text = "Mehul Enterprises Limited",font = ('times',30,'bold'),fg = "white",relief =GROOVE,bg = bg_color,pady = 2,bd=7).pack(fill = X)
        #=============Variables===============#
        #Cosmetics
        self.bath = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_s = IntVar()
        self.hair_g = IntVar()
        self.body_l = IntVar()
        #Grocery
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        #cold drinks
        self.maaza = IntVar()
        self.coca_cola = IntVar()
        self.frooti = IntVar()
        self.thumbs_up = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()
        #total
        self.tcp = StringVar()
        self.tgp = StringVar()
        self.tcdp = StringVar()
        self.tct = StringVar()
        self.tgt = StringVar()
        self.tcdt = StringVar()
        #customer
        self.c_name = StringVar()
        self.c_phn = StringVar()
        self.bill_no = StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        #=============Customer Frame================#
        F1 = LabelFrame(self.root,text = "Customer Details",font = ("times new roman",15,'bold'),fg = "gold",bg=bg_color,bd=6,relief=GROOVE)
        F1.place(x=0,y=73,relwidth=1)

        cname_lbl = Label(F1,text="Customer Name",font = ("times new roman",18,'bold'),fg = "white",bg=bg_color).grid(row=0,column=0,padx = 20,pady = 5)
        cname_txt = Entry(F1,textvariable=self.c_name,width=15,font=('arial',15),bd=4,relief=SUNKEN).grid(row=0,column=1,padx = 10,pady = 5)

        cphn_lbl = Label(F1, text="Phone Number", font=("times new roman", 18, 'bold'), fg="white", bg=bg_color).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1,textvariable=self.c_phn, width=15, font=('arial', 15), bd=4, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)

        c_bill_lbl = Label(F1, text="Bill Number", font=("times new roman", 18, 'bold'), fg="white", bg=bg_color).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1,textvariable=self.bill_no, width=15, font=('arial', 15), bd=4, relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)

        save_btn = Button(F1,text = 'Save',font=("times new roman", 12, 'bold'),width=7,bd=3,command=self.save_bill).grid(row=0,column=6,padx=2, pady=6)
        search_btn = Button(F1, text='Search', font=("times new roman", 12, 'bold'), width=7, bd=3,command=self.find_bill).grid(row=0, column=7, padx=7, pady=6)

        # =============Cosmetics Frame================#
        F2 = LabelFrame(self.root, text="Cosmetics Details", font=("times new roman", 15, 'bold'), fg="gold",bg=bg_color, bd=6, relief=GROOVE)
        F2.place(x=0, y=160,width=325,height=380)

        bath_lbl = Label(F2,text="Bath Soap",font=("times new roman", 16, 'bold'), fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx = 10,pady = 10,sticky='w')
        bath_txt = Entry(F2,textvariable=self.bath,width=14,font=("times new roman", 13, 'bold'),bd=3,relief=SUNKEN).grid(row=0,column=1,padx=20)

        face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, 'bold'), fg="lightgreen", bg=bg_color).grid(row=1, column=0, padx=10, pady=10, sticky='w')
        face_cream_txt = Entry(F2,textvariable=self.face_cream, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=1, column=1,padx=20)

        face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, 'bold'), fg="lightgreen", bg=bg_color).grid(row=2, column=0, padx=10, pady=10, sticky='w')
        face_w_txt = Entry(F2,textvariable=self.face_wash, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=2, column=1, padx=20)

        hair_s_lbl = Label(F2, text="Hair Soap", font=("times new roman", 16, 'bold'), fg="lightgreen",bg=bg_color).grid(row=3, column=0, padx=10, pady=10, sticky='w')
        hair_s_txt = Entry(F2,textvariable=self.hair_s, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=3,column=1,padx=20)

        hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, 'bold'), fg="lightgreen",bg=bg_color).grid(row=4, column=0, padx=10, pady=10, sticky='w')
        hair_g_txt = Entry(F2,textvariable=self.hair_g, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=4,column=1, padx=20)

        body_l_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, 'bold'), fg="lightgreen",bg=bg_color).grid(row=5, column=0, padx=10, pady=10, sticky='w')
        body_l_txt = Entry(F2,textvariable=self.body_l, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=5,column=1,padx=20)

        # =============Grocery Frame================#
        F3 = LabelFrame(self.root, text="Grocery Details", font=("times new roman", 15, 'bold'), fg="gold",bg=bg_color, bd=6, relief=GROOVE)
        F3.place(x=325, y=160, width=325, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, 'bold'), fg="lightgreen", bg=bg_color).grid(row=0, column=0, padx=10, pady=10, sticky='w')
        g1_txt = Entry(F3,textvariable=self.rice, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=0, column=1,padx=20)

        g2_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, 'bold'), fg="lightgreen",bg=bg_color).grid(row=1, column=0, padx=10, pady=10, sticky='w')
        g2_txt = Entry(F3,textvariable=self.food_oil, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=1,column=1,padx=20)

        g3_lbl = Label(F3, text="Daal", font=("times new roman", 16, 'bold'), fg="lightgreen",bg=bg_color).grid(row=2, column=0, padx=10, pady=10, sticky='w')
        g3_txt = Entry(F3,textvariable=self.daal, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=2,column=1,padx=20)

        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, 'bold'), fg="lightgreen",bg=bg_color).grid(row=3, column=0, padx=10, pady=10, sticky='w')
        g4_txt = Entry(F3,textvariable=self.wheat, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=3,column=1,padx=20)

        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 16, 'bold'), fg="lightgreen",bg=bg_color).grid(row=4, column=0, padx=10, pady=10, sticky='w')
        g5_txt = Entry(F3,textvariable=self.sugar, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=4,column=1,padx=20)

        g6_lbl = Label(F3, text="Tea", font=("times new roman", 16, 'bold'), fg="lightgreen",bg=bg_color).grid(row=5, column=0, padx=10, pady=10, sticky='w')
        g6_txt = Entry(F3,textvariable=self.tea, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=5,column=1,padx=20)

        # =============Cold Drink Frame================#
        F4 = LabelFrame(self.root, text="Cold Drink Details", font=("times new roman", 15, 'bold'), fg="gold", bg=bg_color,bd=6, relief=GROOVE)
        F4.place(x=650, y=160, width=325, height=380)

        c1_lbl = Label(F4, text="Maaza", font=("times new roman", 16, 'bold'), fg="lightgreen", bg=bg_color).grid(row=0, column=0, padx=10, pady=10, sticky='w')
        c1_txt = Entry(F4,textvariable=self.maaza, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=0, column=1,padx=20)

        c2_lbl = Label(F4, text="Coca Cola", font=("times new roman", 16, 'bold'), fg="lightgreen", bg=bg_color).grid(row=1, column=0, padx=10, pady=10, sticky='w')
        c2_txt = Entry(F4,textvariable=self.coca_cola, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=1, column=1,padx=20)

        c3_lbl = Label(F4, text="Frooti", font=("times new roman", 16, 'bold'), fg="lightgreen", bg=bg_color).grid(row=2, column=0, padx=10, pady=10, sticky='w')
        c3_txt = Entry(F4,textvariable=self.frooti, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=2, column=1,padx=20)

        c4_lbl = Label(F4, text="Thumbs Up", font=("times new roman", 16, 'bold'), fg="lightgreen", bg=bg_color).grid(row=3, column=0, padx=10, pady=10, sticky='w')
        c4_txt = Entry(F4,textvariable=self.thumbs_up, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=3, column=1,padx=20)

        c5_lbl = Label(F4, text="Limca", font=("times new roman", 16, 'bold'), fg="lightgreen", bg=bg_color).grid(row=4, column=0, padx=10, pady=10, sticky='w')
        c5_txt = Entry(F4,textvariable=self.limca, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=4, column=1,padx=20)

        c6_lbl = Label(F4, text="Sprite", font=("times new roman", 16, 'bold'), fg="lightgreen", bg=bg_color).grid(row=5, column=0, padx=10, pady=10, sticky='w')
        c6_txt = Entry(F4,textvariable=self.sprite, width=14, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=5, column=1,padx=20)

        #=================Billing Area================#
        F5 = Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=975,y=160,height=380,width=380)
        bill_text = Label(F5,text='Mehul Enterprises Limited',font=('times',18,'bold')).pack(pady=1)
        bill_text = Label(F5,text='*********** Bill Details ***********',font=('times',14)).pack()
        scroll_y = Scrollbar(F5,orient = VERTICAL)
        self.textarea = Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #===========Bill Details===========#
        F6 = LabelFrame(self.root, text="Bill Menu", font=("times new roman", 15, 'bold'), fg="gold",bg=bg_color, bd=6, relief=GROOVE)
        F6.place(x=0,y=540, relwidth=1, height=159)

        m1 = Label(F6, text="Total Cosmetic Price", font=("times new roman", 13, 'bold'), fg="lightgreen", bg=bg_color).grid(row=0,column=0,padx=10,pady=7,sticky='w')
        m1_txt = Entry(F6,textvariable=self.tcp, width=10, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=0, column=1,padx=15)

        m2 = Label(F6, text="Total Grocery Price", font=("times new roman", 13, 'bold'), fg="lightgreen",bg=bg_color).grid(row=1, column=0, padx=10, pady=10, sticky='w')
        m2_txt = Entry(F6, width=10,textvariable=self.tgp, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=1, column=1,padx=15)

        m3 = Label(F6, text="Total Soft Drink Price", font=("times new roman", 13, 'bold'), fg="lightgreen",bg=bg_color).grid(row=2,column=0, padx=10, pady=10, sticky='w')
        m3_txt = Entry(F6,textvariable=self.tcdp, width=10, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=2, column=1,padx=15)

        t1 = Label(F6, text="Total Cosmetic Tax", font=("times new roman", 13, 'bold'), fg="lightgreen",bg=bg_color).grid(row=0, column=2, padx=10, pady=7, sticky='w')
        t1_txt = Entry(F6,textvariable=self.tct, width=10, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=0, column=3,padx=15)

        t2 = Label(F6, text="Total Grocery Tax", font=("times new roman", 13, 'bold'), fg="lightgreen",bg=bg_color).grid(row=1, column=2, padx=10, pady=10, sticky='w')
        t2_txt = Entry(F6,textvariable=self.tgt, width=10, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=1, column=3,padx=15)

        t3 = Label(F6, text="Total Cold Drink Tax", font=("times new roman", 13, 'bold'), fg="lightgreen",bg=bg_color).grid(row=2, column=2, padx=10, pady=10, sticky='w')
        t3_txt = Entry(F6,textvariable=self.tcdt, width=10, font=("times new roman", 13, 'bold'), bd=3, relief=SUNKEN).grid(row=2, column=3,padx=15)

        #=================Button Frame==============#
        btn_F = Frame(F6,bd=6,relief=GROOVE)
        btn_F.place(x=638,y=5,width=676,height=114)

        total_btn = Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg='white',pady=29,bd=4,width=12,font=('times',15,'bold')).grid(row=0,column=0)
        GBill_btn = Button(btn_F, text="Generate Bill", bg="cadetblue", fg='white', pady=29, bd=4, width=12,font=('times', 15, 'bold'),padx=6,command=self.bill_area).grid(row=0, column=1)
        Clear_btn = Button(btn_F, text="Clear", bg="cadetblue", fg='white', pady=29, bd=4, width=12,font=('times', 15, 'bold'),padx=6,command=self.clear).grid(row=0, column=2)
        Exit_btn = Button(btn_F, text="Exit", bg="cadetblue", fg='white', pady=29, bd=4, width=12,font=('times', 15, 'bold'),padx=6,command=self.exit).grid(row=0, column=3)
        self.welcome_bill()
    def total(self):
        self.cbp = (self.bath.get()*40)
        self.cfcp = (self.face_cream.get() * 100)
        self.cfwp = (self.face_wash.get() * 250)
        self.chsp = (self.hair_s.get() * 100)
        self.chgp = (self.hair_g.get()*100)
        self.blp = (self.body_l.get()*200)
        self.total_cosmetic_price = float(self.cbp+self.cfcp+self.cfwp+self.chsp+self.chgp+self.blp)
        self.tcp.set('Rs'+' '+str(self.total_cosmetic_price))
        self.total_cosmetic_tax = round(self.total_cosmetic_price*0.02,2)
        self.tct.set('Rs'+' '+str(self.total_cosmetic_tax))


        self.grp = (self.rice.get() * 40)
        self.gfop = (self.food_oil.get() * 100)
        self.gdp = (self.daal.get() * 70)
        self.gwp = (self.wheat.get() * 30)
        self.gsp = (self.sugar.get() * 45)
        self.gtp = (self.tea.get()* 180)
        self.total_grocery_price = float(self.grp+self.gfop+self.gdp+self.gwp+self.gsp+self.gtp)
        self.tgp.set('Rs'+' '+str(self.total_grocery_price))
        self.total_grocery_tax = round(self.total_grocery_price * 0.02,2)
        self.tgt.set('Rs' + ' ' + str(self.total_grocery_tax))


        self.cdmp = (self.maaza.get() * 40)
        self.cdccp = (self.coca_cola.get() * 20)
        self.cdfp = (self.frooti.get() * 20)
        self.cdtup = (self.thumbs_up.get() * 20)
        self.cdlp = (self.limca.get() * 20)
        self.cdsp = (self.sprite.get() * 20)

        self.total_cold_drink_price = float(self.cdmp+self.cdccp+self.cdfp+self.cdfp+self.cdtup+self.cdlp+self.cdsp)
        self.tcdp.set('Rs'+' '+str(self.total_cold_drink_price))
        self.total_cold_drink_tax = round(self.total_cold_drink_price * 0.02,2)
        self.tcdt.set('Rs' + ' ' + str(self.total_cold_drink_tax))

        self.total_amt = self.total_cosmetic_price+self.total_grocery_price+self.total_cold_drink_price+self.total_cosmetic_tax+self.total_grocery_tax+self.total_cold_drink_tax


    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,f'\n Bill Number : {self.bill_no.get()}')
        self.textarea.insert(END,f'\n Customer Name : {self.c_name.get()}')
        self.textarea.insert(END,f'\n Phone Number : {self.c_phn.get()}')
        self.textarea.insert(END,'\n==========================================')
        self.textarea.insert(END,'\n Products\t\t Quantity\t\t Price')
        self.textarea.insert(END, '\n==========================================')

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phn.get()=="":
            tkinter.messagebox.showerror("Mehul Enterprises Limited","Please enter Customer details")
        else:
            self.welcome_bill()
            if self.bath.get()!=0:
                self.textarea.insert(END,f'\n Bath Soap\t\t   {self.bath.get()}\t\t {self.cbp}')
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f'\n Face Cream\t\t   {self.face_cream.get()}\t\t {self.cfcp}')
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f'\n Face Wash\t\t   {self.face_wash.get()}\t\t {self.cfwp}')
            if self.hair_s.get()!=0:
                self.textarea.insert(END,f'\n Hair Shampoo\t\t   {self.hair_s.get()}\t\t {self.chsp}')
            if self.hair_g.get()!=0:
                self.textarea.insert(END,f'\n Hair Gel\t\t   {self.hair_g.get()}\t\t {self.chgp}')
            if self.body_l.get()!=0:
                self.textarea.insert(END,f'\n Body Lotion\t\t   {self.body_l.get()}\t\t {self.cbp}')
            if self.rice.get()!=0:
                self.textarea.insert(END,f'\n Rice\t\t   {self.rice.get()}\t\t {self.grp}')
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f'\n Food Oil\t\t   {self.food_oil.get()}\t\t {self.gfop}')
            if self.daal.get()!=0:
                self.textarea.insert(END,f'\n Daal\t\t   {self.daal.get()}\t\t {self.gdp}')
            if self.wheat.get()!=0:
                self.textarea.insert(END,f'\n Wheat\t\t   {self.wheat.get()}\t\t {self.gwp}')
            if self.sugar.get()!=0:
                self.textarea.insert(END,f'\n Sugar\t\t   {self.sugar.get()}\t\t {self.gsp}')
            if self.tea.get()!=0:
                self.textarea.insert(END,f'\n Tea\t\t   {self.tea.get()}\t\t {self.gtp}')

            if self.maaza.get()!=0:
                self.textarea.insert(END,f'\n Maaza\t\t   {self.maaza.get()}\t\t {self.cdmp}')
            if self.coca_cola.get()!=0:
                self.textarea.insert(END,f'\n Coca Cola\t\t   {self.coca_cola.get()}\t\t {self.cdccp}')
            if self.frooti.get()!=0:
                self.textarea.insert(END,f'\n Frooti\t\t   {self.frooti.get()}\t\t {self.cdfp}')
            if self.thumbs_up.get()!=0:
                self.textarea.insert(END,f'\n Thumbs Up\t\t   {self.thumbs_up.get()}\t\t {self.cdtup}')
            if self.limca.get()!=0:
                self.textarea.insert(END,f'\n Limca\t\t   {self.limca.get()}\t\t {self.cdlp}')
            if self.sprite.get()!=0:
                self.textarea.insert(END,f'\n Sprite\t\t   {self.sprite.get()}\t\t {self.cdsp}')

            self.textarea.insert(END,f'\n------------------------------------------')
            if self.tct.get()!="Rs 0.0":
                self.textarea.insert(END,f'\nTotal Cosmetics Tax  : {self.tct.get()}')
            if self.tgt.get() != "Rs 0.0":
                self.textarea.insert(END, f'\nTotal Grocery Tax    : {self.tgt.get()}')
            if self.tcdt.get() != "Rs 0.0":
                self.textarea.insert(END, f'\nTotal Cold Drink Tax : {self.tcdt.get()}')
            self.textarea.insert(END, f'\n------------------------------------------')
            self.textarea.insert(END, f'\nTotal Amount : {self.total_amt}')
            self.textarea.insert(END, f'\n------------------------------------------')
            self.textarea.insert(END, f'\n********** Thanks for Shopping ***********')
            self.textarea.insert(END, f'\n------------------------------------------')


    def save_bill(self):
        op = tkinter.messagebox.askyesno("Save Details","Do you want to save the details?")
        if op>0:
            self.bill_data = self.textarea.get('1.0',END)
            f1 = open("bills/"+str(self.bill_no.get())+'.txt','w')
            f1.write(self.bill_data)
            f1.close()
            tkinter.messagebox.showinfo("Success","Your bill is successfully saved")
        else:
            return

    def find_bill(self):
        present = "No"
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.bill_no.get():
                f1 = open(f"bills/{i}","r")
                self.textarea.delete("1.0", END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="Yes"
        if present=="No":
            tkinter.messagebox.showerror("Error","File Not Found")

    def clear(self):
        op = tkinter.messagebox.askyesno("Mehul Enterprises Limited","Do you really want to clear data?")
        if op>0:
            # Cosmetics
            self.bath.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_s.set(0)
            self.hair_g.set(0)
            self.body_l.set(0)
            # Grocery
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            # cold drinks
            self.maaza.set(0)
            self.coca_cola.set(0)
            self.frooti.set(0)
            self.thumbs_up.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            # total
            self.tcp.set("")
            self.tgp.set("")
            self.tcdp.set("")
            self.tct.set("")
            self.tgt.set("")
            self.tcdt.set("")
            # customer
            self.c_name.set("")
            self.c_phn.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.textarea.delete('1.0',END)
            self.welcome_bill()
    def exit(self):
        op = tkinter.messagebox.askyesno("Mehul Enterprises Limited","Do you really want to exit?")
        if op>0:
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()