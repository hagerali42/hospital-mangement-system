
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pip
pip.main(['install','mysql-connector-python-rf'])

import mysql.connector
import time
import datetime
import random




class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets= StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.Dailydose = StringVar()
        self.SideEfect = StringVar()
        self.FurtherInformation = StringVar()
        # self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()
        self.Blod = StringVar()


        self.root.title('Hospital  management system')
        title = Label(self.root, text='Hospital Management System', bd=20, relief=RIDGE, bg='white',fg='#66CDAA',font=("times new roman", 50, "bold"),).pack(side=TOP, fill=X)

        #=======data frame====#

        Dataframe=Frame(self.root,bd=15,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        Dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE, bg='#F8F6F0',padx=10,font=("times new roman", 12, "bold"),text="Patient Information",fg='#3CB371')
        Dataframeleft.place(x=0, y=2, width=980, height=370)

        Dataframeright = LabelFrame(Dataframe, bd=10, relief=RIDGE, bg='#F8F6F0', padx=10,font=("times new roman", 12, "bold"), text="Prescription", fg='#3CB371')
        Dataframeright.place(x=990, y=2, width=500, height=370)

        #=========buttomfram========
        Buttonframe=Frame(self.root,bd=10,relief=RIDGE,bg='#F8F6F0')
        Buttonframe.place(x=120,y=540,width=1240,height=60)

        # =========drtailsfram========
        Detailsframe=Frame(self.root,bd=10,relief=RIDGE)
        Detailsframe.place(x=0,y=610,width=1530,height=170)

        # =========datafrram= left=======
        lbl_nameTablet = Label(Dataframeleft, text='Name of Tablets', fg="#2E8B57", padx=2,pady=6, font=("arial", 12, "bold"))
        lbl_nameTablet.grid(row=0,column=0,sticky=W)

        combo_nameTablet = ttk.Combobox(Dataframeleft,textvariable=self.Nameoftablets, font=("arial", 12, "bold",), state='readonly')
        combo_nameTablet['values'] = ("Nice", 'Corona Vacacine','Acetaminophen','Adderall','Amlodipine','Ativan')
        combo_nameTablet.current(0)
        combo_nameTablet.grid(row=0,column=1)

        lblref = Label(Dataframeleft, text='Refence No', fg="#2E8B57", padx=2, font=("arial", 12, "bold"))
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(Dataframeleft,textvariable=self.ref, font=("arial", 13, "bold"), bd=4, width=35)
        txtref.grid(row=1,column=1,)

        lblDose = Label(Dataframeleft, text='Dose ', fg="#2E8B57", padx=2, font=("arial", 12, "bold"))
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(Dataframeleft,textvariable=self.Dose, font=("arial", 13, "bold"), bd=4, width=35)
        txtDose.grid(row=2, column=1, )

        lblNoOftablets = Label(Dataframeleft, text='No of Tablets ', fg="#2E8B57", padx=2,pady=6, font=("arial", 12, "bold"))
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(Dataframeleft,textvariable=self.NumberofTablets, font=("arial", 13, "bold"), bd=4, width=35)
        txtNoOftablets.grid(row=3, column=1, )

        lblLot = Label(Dataframeleft, text='Lot ', fg="#2E8B57", padx=2, pady=6,font=("arial", 12, "bold"))
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(Dataframeleft,textvariable=self.Lot, font=("arial", 13, "bold"), bd=4, width=35)
        txtLot.grid(row=4, column=1, )

        lblissueDate = Label(Dataframeleft, text='Issue Date ', fg="#2E8B57", padx=2, pady=6,font=("arial", 12, "bold"))
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(Dataframeleft,textvariable=self.Issuedate, font=("arial", 13, "bold"), bd=4, width=35)
        txtissueDate.grid(row=5, column=1, )

        lblExpDate= Label(Dataframeleft, text='Exp Date ', fg="#2E8B57", padx=2, pady=6,font=("arial", 12, "bold"))
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(Dataframeleft,textvariable=self.ExpDate, font=("arial", 13, "bold"), bd=4, width=35)
        txtExpDate.grid(row=6, column=1, )

        lblDaliyDose= Label(Dataframeleft,  text='Daily Dose ', fg="#2E8B57", padx=2, pady=4, font=("arial", 12, "bold"))
        lblDaliyDose.grid(row=7, column=0, sticky=W)
        txtDaliyDose = Entry(Dataframeleft,textvariable=self.Dailydose, font=("arial", 13, "bold"), bd=4, width=35)
        txtDaliyDose.grid(row=7, column=1, )

        lblSideEffect = Label(Dataframeleft, text='Side Effect ', fg="#2E8B57", padx=2, pady=6, font=("arial", 12, "bold"))
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(Dataframeleft,textvariable=self.SideEfect, font=("arial", 13, "bold"), bd=4, width=35)
        txtSideEffect.grid(row=8, column=1, )

        lblFurtherinfo = Label(Dataframeleft, text='Further Information ', fg="#2E8B57", padx=2, font=("arial", 12, "bold"))
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(Dataframeleft,textvariable=self.FurtherInformation, font=("arial", 13, "bold"), bd=4, width=35)
        txtFurtherinfo.grid(row=0, column=3, )

        lblBloodPressure = Label(Dataframeleft, text='Blood Pressure', fg="#2E8B57", padx=2, pady=6, font=("arial", 12, "bold"))
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(Dataframeleft,textvariable=self.Blod, font=("arial", 13, "bold"), bd=4, width=35)
        txtBloodPressure.grid(row=1, column=3, )

        lblMedicine = Label(Dataframeleft, text='Medication', fg="#2E8B57", padx=2, pady=6, font=("arial", 12, "bold"))
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(Dataframeleft,textvariable=self.DrivingUsingMachine, font=("arial", 13, "bold"), bd=4, width=35)
        txtMedicine.grid(row=3, column=3,sticky=W )

        lblPatientId= Label(Dataframeleft, text='Patient Id', fg="#2E8B57", padx=2, pady=6,font=("arial", 12, "bold"))
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(Dataframeleft,textvariable=self.PatientId, font=("arial", 13, "bold"), bd=4, width=35)
        txtPatientId.grid(row=4, column=3, )

        lblNhsNumber= Label(Dataframeleft, text='NHS Number', fg="#2E8B57", padx=2, pady=6,font=("arial", 12, "bold"))
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(Dataframeleft,textvariable=self.nhsNumber, font=("arial", 13, "bold"), bd=4, width=35)
        txtNhsNumber.grid(row=5, column=3, )

        lblPatientName = Label(Dataframeleft, text='PatientName', fg="#2E8B57", padx=2, pady=6, font=("arial", 12, "bold"))
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(Dataframeleft,textvariable=self.PatientName, font=("arial", 13, "bold"), bd=4, width=35)
        txtPatientName.grid(row=6, column=3, )

        lblDateOfBirth = Label(Dataframeleft, text='Date Of Birth', fg="#2E8B57", padx=2, pady=6,font=("arial", 12, "bold"))
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(Dataframeleft,textvariable=self.DateOfBirth, font=("arial", 13, "bold"), bd=4, width=35)
        txtDateOfBirth.grid(row=7, column=3, )

        lblPatientAddress = Label(Dataframeleft, text='Patient Address', fg="#2E8B57", padx=2, pady=6,font=("arial", 12, "bold"))
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress= Entry(Dataframeleft,textvariable=self.PatientAddress, font=("arial", 13, "bold"), bd=4, width=35)
        txtPatientAddress.grid(row=8, column=3, )

  #===============================dataframe right==========

        self.txtPrescription=Text(Dataframeright,font=("arial", 12, "bold"),padx=2, pady=6,width=50,height=16)
        self.txtPrescription.grid(row=0,column=0)

        # ===============================button==========
        bntPrescription=Button(Buttonframe,text="Prescription",bg="#2E8B57",fg='white',font=("arial", 12, "bold"),width=23,command=self.iPrectioption)
        bntPrescription.grid(row=0,column=0,padx=1, pady=6)

        bntPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="#2E8B57", fg='white',font=("arial", 12, "bold"),width=23,command=self.iPrescriptionData)
        bntPrescriptionData.grid(row=0, column=1, padx=1, pady=6)


        bntDelete = Button(Buttonframe, text="Delete", bg="#2E8B57", fg='white',font=("arial", 12, "bold"), width=23,command=self.idelete )
        bntDelete .grid(row=0, column=3, padx=1, pady=6)

        bntClear = Button(Buttonframe, text="Clear", bg="#2E8B57", fg='white',font=("arial", 12, "bold"), width=23, command=self.clear)
        bntClear.grid(row=0, column=4, padx=1, pady=6)

        bntExit = Button(Buttonframe, text="Exit", bg="#2E8B57", fg='white',font=("arial", 12, "bold"), width=23,command=self.iExit)
        bntExit.grid(row=0, column=6, padx=1, pady=6)

    # ===============================table==========
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=('Nameoftablets','ref','Dose','NumberofTablets','Lot','Issuedate','ExpDate','Dailydose','nhsNumber','PatientName','DateOfBirth','PatientAddress'),)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading('Nameoftablets', text="Name of Table")
        self.hospital_table.heading('ref', text="Reference No.")
        self.hospital_table.heading('Dose', text="Dose")
        self.hospital_table.heading('NumberofTablets', text="No OF Tablets")
        self.hospital_table.heading('Lot', text="Lot", )
        self.hospital_table.heading('Issuedate', text="Issues Data", )
        self.hospital_table.heading('ExpDate', text="Exp Date", )
        self.hospital_table.heading('Dailydose', text="Daily Date", )

        self.hospital_table.heading('nhsNumber', text="NHS Number", )
        self.hospital_table.heading('PatientName', text="Patient Name", )
        self.hospital_table.heading('DateOfBirth', text="DOB", )
        self.hospital_table.heading('PatientAddress', text="Address", )

        self.hospital_table['show'] = 'headings'

        self.hospital_table.column('Nameoftablets', width=100)
        self.hospital_table.column('ref', width=100)
        self.hospital_table.column('Dose', width=100)
        self.hospital_table.column('NumberofTablets', width=100)
        self.hospital_table.column('Lot', width=100)
        self.hospital_table.column('Issuedate', width=100)
        self.hospital_table.column('ExpDate', width=100)
        self.hospital_table.column('Dailydose', width=100)

        self.hospital_table.column('nhsNumber', width=100)
        self.hospital_table.column('PatientName', width=100)
        self.hospital_table.column('DateOfBirth', width=100)
        self.hospital_table.column('PatientAddress', width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)

        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

        #===================function declration==========#
    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="123456789",port='3306',database='sys')
            my_cursor = conn.cursor()
            print("connect")

            my_cursor.execute("insert into hospital values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                   self.Nameoftablets.get(),
                                                                                                   self.ref.get(),
                                                                                                   self.Dose.get(),
                                                                                                   self.NumberofTablets.get(),
                                                                                                   self.Lot.get(),
                                                                                                   self.Issuedate.get(),
                                                                                                   self.ExpDate.get(),
                                                                                                   self.Dailydose.get(),
                                                                                                   self.nhsNumber.get(),
                                                                                                   self.PatientName.get(),
                                                                                                   self.DateOfBirth.get()
                                                                                                   ))
            messagebox.showinfo("success","Record has been inserted")
            conn.commit()
            self.fetch_data()
            conn.close()


    # def update_data(self):
    #     conn = mysql.connector.connect(host="localhost", user="root", password="123456789", port='3306', database='sys')
    #     my_cursor = conn.cursor()
    #     my_cursor.execute("update hospital set  Nameoftablets=%s,Dose=%s,NumberofTablets=%s,Lot=%s,Issuedate=%s,ExpDate=%s,Dailydose=%s,nhsNumber=%s,PatientName=%s,DateOfBirth=%s where ref=%s",(
    #                                                                                                                                                         self.Nameoftablets.get(),
    #                                                                                                                                                         self.ref.get(),
    #                                                                                                                                                         self.Dose.get(),
    #                                                                                                                                                         self.NumberofTablets.get(),
    #                                                                                                                                                         self.Lot.get(),
    #                                                                                                                                                         self.Issuedate.get(),
    #                                                                                                                                                         self.ExpDate.get(),
    #                                                                                                                                                         self.Dailydose.get(),
    #                                                                                                                                                         self.nhsNumber.get(),
    #                                                                                                                                                         self.PatientName.get(),
    #                                                                                                                                                         self.DateOfBirth.get()
    #
    #                                                                                                                                               ))
    #
    #     conn.commit()
    #     self.fetch_data()
    #     conn.close()
    #     messagebox.showinfo("success", "Record has been updated")


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="123456789",port='3306',database='sys')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!= 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.Dailydose.set(row[7])
        # self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[8])
        self.PatientName.set(row[9])
        self.DateOfBirth.set(row[10])


    def iPrectioption(self):
        self.txtPrescription.insert(END,"Nameoftablets:\t\t\t"+self.Nameoftablets.get()+ "\n")
        self.txtPrescription.insert(END, "ref:\t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "NumberofTablets:\t\t\t" + self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issues Data:\t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END, "ExpDate:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "Dailydose :\t\t\t" + self.Dailydose.get() + "\n")
        self.txtPrescription.insert(END, "SideEfect :\t\t\t" + self.SideEfect.get() + "\n")
        self.txtPrescription.insert(END, "FurtherInformation  :\t\t\t" + self.FurtherInformation.get() + "\n")
        # self.txtPrescription.insert(END, "StorageAdvice :\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END, "DrivingUsingMachine :\t\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(END, "PatientId :\t\t\t" + self.PatientId.get() + "\n")
        self.txtPrescription.insert(END, "DateOfBirth  :\t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "PatientAddress:\t\t\t" + self.PatientAddress.get() + "\n")

    def idelete(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="123456789", port='3306', database='sys')
        my_cursor = conn.cursor()
        query = "delete from hospital where ref=%s"
        value = (self.ref.get(),)
        my_cursor.execute(query, value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("success", "Record has been deleted")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.Dailydose.set("")
        self.SideEfect.set("")
        self.FurtherInformation.set("")
        self.DrivingUsingMachine.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)


    def iExit(self):
        if messagebox.askokcancel('Quit', 'Are you sure you want to exit?'):
            self.root.destroy()
            return


















class Hospital:
    pass
    root = Tk()
    obj = Hospital(root)
    root.mainloop()