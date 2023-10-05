from tkinter import *
from tkinter import ttk
import sqlite3

conn=sqlite3.connect('financial_management.db')
c=conn.cursor()

conn.commit()
conn.close()


root=Tk()
root.title('Codemy.com-TreeBase')
w = 1370
h = 800

root.minsize(width=w, height=h)
root.maxsize(width=w, height=h)
#root.resizable(width=FALSE, height=FALSE)
root.geometry('%dx%d' % (w, h))


def open():
  num2=S1.get()
  M=float(num2)
  num1=S2.get()
  S=float(num1)
  conn=sqlite3.connect('financial_management.db')
  c=conn.cursor()
  L1=[1201,1202,45446,53124]
  L2=[1203,1204,23123,99978]
  L3=[1205,1206,67564,11123]
  L4=[1207,1208,90786,56473]
  

  if(S and M in L1):###############    STOCKS
    Top=Toplevel()
    Top.title("Stocks")
    def select():
     E1.delete(0, END)
     E2.delete(0, END)
     E3.delete(0, END)
     E4.delete(0, END)
     E5.delete(0, END)
     E6.delete(0, END)
     E7.delete(0, END)
     E8.delete(0, END)

     selected = my_tree.focus()
     values = my_tree.item(selected,'values')


     E1.insert(0,values[0])
     E2.insert(0,values[1])
     E3.insert(0,values[2])
     E4.insert(0,values[3])
     E5.insert(0,values[4])
     E6.insert(0,values[5])
     E7.insert(0,values[6])
     E8.insert(0,values[7])



    def clear():
     E1.delete(0, END)
     E2.delete(0, END)
     E3.delete(0, END)
     E4.delete(0, END)
     E5.delete(0, END)
     E6.delete(0, END)
     E7.delete(0, END)
     E8.delete(0, END)
     return

    def remove_s():
     x=my_tree.selection()[0]
     my_tree.delete(x)
     return

    def update():
     selected = my_tree.focus()
     my_tree.item(selected,text="",values=(E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),E7.get(),E8.get(),))
     conn=sqlite3.connect('financial_management.db')
     c=conn.cursor()
  
     
    
     c.execute(""" UPDATE stocks SET
              stk_name= :name,
              stk_type= :type,
              stk_quantity= :quantity,
              stk_desc= :desc,
              price_per_unit= :price,
              total_amount= :amount,
              manager_userid= :manager

              WHERE stk_id= :id  """,
              {
                    'id':E1.get(),
                    'name':E2.get(),
                    'type':E3.get(),
                    'quantity':E4.get(),
                    'desc':E5.get(),
                    'price':E6.get(),
                    'amount':E7.get(),
                    'manager':E8.get(),
              }

        )

     
    
     conn.commit()
     conn.close()
     E1.delete(0, END)
     E2.delete(0, END)
     E3.delete(0, END)
     E4.delete(0, END)
     E5.delete(0, END)
     E6.delete(0, END)
     E7.delete(0, END)
     E8.delete(0, END)
     
     
    

    def query_database():
     conn=sqlite3.connect('financial_management.db')
     c=conn.cursor()

     c.execute("SELECT * FROM stocks")
     records=c.fetchall()

     global count
     count=0

     for record in records:
      if count %2 ==0:
        my_tree.insert(parent='',index='end',iid=count,text='',values=( record[0], record[1],record[2],record[3],record[4],record[5],record[6],record[7]),tags=('evenrow',))
      else:
        my_tree.insert(parent='',index='end',iid=count,text='',values=(  record[0], record[1],record[2],record[3],record[4],record[5],record[6],record[7]),tags=('oddrow',))
      count+=1
     conn.commit()
     conn.close()



    def submit():
     conn=sqlite3.connect('financial_management.db')
     cursor = conn.cursor()
     cursor.execute("INSERT INTO stocks VALUES(,:stk_name,:stk_type,:stk_quantity,:stk_desc,:price_per_unit,:total_amount,:manager_userid)",
          {
            'stk_id': E1.get(),
            'stk_name': E2.get(),
            'stk_type': E3.get(),
            'stk_quantity': E4.get(),
            'stk_desc': E5.get(),
            'price_per_unit': E6.get(),
            'total_amount': E7.get(),
            'manager_userid': E8.get(),
          }
    
    
          )
     conn.commit()
     conn.close()
     E1.delete(0, END)
     E2.delete(0, END)
     E3.delete(0, END)
     E4.delete(0, END)
     E5.delete(0, END)
     E6.delete(0, END)
     E7.delete(0, END)
     E8.delete(0, END)
     
     my_tree.delete(*my_tree.get_children())
     query_database()
    


    style=ttk.Style()
    style.theme_use('default')
    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map("Treeview",
    background=[('selected',"#347083")])

    tree_frame=Frame(Top)
    tree_frame.pack(pady=10)

    tree_scroll=Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT,fill=Y)

    my_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="extended")
    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)


    my_tree['columns']=("Stock ID","Stock Name","Stock Type","Stock Quantity","Stock Description","Price per unit","Total Amount","Manager ID")
    my_tree.column("#0",width=0,stretch=NO)
    my_tree.column("Stock ID",anchor=W,width=140)
    my_tree.column("Stock Name",anchor=W,width=140)
    my_tree.column("Stock Type",anchor=CENTER,width=140)
    my_tree.column("Stock Quantity",anchor=CENTER,width=140)
    my_tree.column("Stock Description",anchor=CENTER,width=140)
    my_tree.column("Price per unit",anchor=CENTER,width=140)
    my_tree.column("Total Amount",anchor=CENTER,width=140)
    my_tree.column("Manager ID",anchor=CENTER,width=140)

    my_tree.heading("#0", text="",anchor=W)
    my_tree.heading("Stock ID", text="Stock ID",anchor=W)
    my_tree.heading("Stock Name", text="Stock Name",anchor=CENTER)
    my_tree.heading("Stock Type", text="Stock Type",anchor=CENTER)
    my_tree.heading("Stock Quantity", text="Stock Quantity",anchor=CENTER)
    my_tree.heading("Stock Description", text="Stock Description",anchor=CENTER)
    my_tree.heading("Price per unit", text="Price per unit",anchor=CENTER)
    my_tree.heading("Total Amount", text="Total Amount",anchor=CENTER)
    my_tree.heading("Manager ID", text="Manager ID",anchor=CENTER)



    my_tree.tag_configure('oddrow',background="white")
    my_tree.tag_configure('evenrow',background="lightblue")






    data_frame =LabelFrame(Top, text="Record")
    data_frame.pack(fill="x",expand="yes",padx=20)

    L1=Label(data_frame,text="Stock ID",font=("Rockwell Extra Black",16))
    L1.grid(row=0,column=0,padx=10,pady=10)
    L2=Label(data_frame,text="Stock Name",font=("Rockwell Extra Black",16))
    L2.grid(row=0,column=2,padx=10,pady=10)
    L3=Label(data_frame,text="Stock Type",font=("Rockwell Extra Black",16))
    L3.grid(row=0,column=4,padx=10,pady=10)
    L4=Label(data_frame,text="Stock Quantity",font=("Rockwell Extra Black",16))
    L4.grid(row=0,column=6,padx=10,pady=10)
    L5=Label(data_frame,text="Stock Desc",font=("Rockwell Extra Black",16))
    L5.grid(row=1,column=0,padx=10,pady=10)
    L6=Label(data_frame,text="Price Per Unit",font=("Rockwell Extra Black",16))
    L6.grid(row=1,column=2,padx=10,pady=10)
    L7=Label(data_frame,text="Total Amount",font=("Rockwell Extra Black",16))
    L7.grid(row=1,column=4,padx=10,pady=10) 
    L8=Label(data_frame,text="Manager ID",font=("Rockwell Extra Black",16))
    L8.grid(row=1,column=6,padx=10,pady=10) 


    E1=Entry(data_frame)
    E1.grid(row=0,column=1,padx=10,pady=10)
    E2=Entry(data_frame)
    E2.grid(row=0,column=3,padx=10,pady=10)
    E3=Entry(data_frame)
    E3.grid(row=0,column=5,padx=10,pady=10)
    E4=Entry(data_frame)
    E4.grid(row=0,column=7,padx=10,pady=10) 
    E5=Entry(data_frame)
    E5.grid(row=1,column=1,padx=10,pady=10)
    E6=Entry(data_frame)
    E6.grid(row=1,column=3,padx=10,pady=10)
    E7=Entry(data_frame)
    E7.grid(row=1,column=5,padx=10,pady=10)
    E8=Entry(data_frame)
    E8.grid(row=1,column=7,padx=10,pady=10)

    button_frame = LabelFrame(Top, text="Commands")
    button_frame.pack(fill="x",expand="yes",padx=20)

    B1=Button(button_frame,text="Update Record",command=update)
    B1.grid(row=0,column=2,padx=20,pady=20)

    B3=Button(button_frame,text="Select Record",command=select)
    B3.grid(row=0,column=3,padx=20,pady=20)
    B4=Button(button_frame,text="Add Record",command=submit)
    B4.grid(row=0,column=4,padx=20,pady=20)
    B5=Button(button_frame,text="Remove Selected",command=remove_s)
    B5.grid(row=0,column=5,padx=20,pady=20)
    B5=Button(button_frame,text="Clear",command=clear)
    B5.grid(row=0,column=6,padx=20,pady=20)
    query_database()

####################################

  elif(S and M in L3):
    Top=Toplevel()
    Top.title("Inventory")
    def select():
      E1.delete(0, END)
      E2.delete(0, END)
      E3.delete(0, END)
      E4.delete(0, END)
      E5.delete(0, END)
      E6.delete(0, END)
      E7.delete(0, END)
      E8.delete(0, END)

 
      selected = my_tree.focus()
      values = my_tree.item(selected,'values')


      E1.insert(0,values[0])
      E2.insert(0,values[1])
      E3.insert(0,values[2])
      E4.insert(0,values[3])
      E5.insert(0,values[4])
      E6.insert(0,values[5])
      E7.insert(0,values[6])
      E8.insert(0,values[7])



    def clear():
      E1.delete(0, END)
      E2.delete(0, END)
      E3.delete(0, END)
      E4.delete(0, END)
      E5.delete(0, END)
      E6.delete(0, END)
      E7.delete(0, END)
      E8.delete(0, END)
      return

    def remove_s():
     x=my_tree.selection()[0]
     my_tree.delete(x)
     return

    def update():
     selected = my_tree.focus()
     my_tree.item(selected,text="",values=(E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),E7.get(),E8.get(),))
     E1.delete(0, END)
     E2.delete(0, END)
     E3.delete(0, END)
     E4.delete(0, END)
     E5.delete(0, END)
     E6.delete(0, END)
     E7.delete(0, END)
     E8.delete(0, END)
     return

    def query_database():
     conn=sqlite3.connect('financial_management.db')
     c=conn.cursor()

     c.execute("SELECT * FROM inventory")
     records=c.fetchall()

     global count
     count=0

     for record in records:
      if count %2 ==0:
        my_tree.insert(parent='',index='end',iid=count,text='',values=( record[0], record[1],record[2],record[3],record[4],record[5],record[6],record[7]),tags=('evenrow',))
      else:
        my_tree.insert(parent='',index='end',iid=count,text='',values=(  record[0], record[1],record[2],record[3],record[4],record[5],record[6],record[7]),tags=('oddrow',))
      count+=1
     conn.commit()
     conn.close()
    



    def submit():
      mydb=sqlite3.connect('financial_management.db')
      cursor = mydb.cursor()
      cursor.execute("INSERT INTO inventory VALUES(:E1,:E2,:E3,:E4,:E5,:E6,:E7,:E8)",
          {
            'E1': E1.get(),
            'E2': E2.get(),
            'E3': E3.get(),
            'E4': E4.get(),
            'E5': E5.get(),
            'E6': E6.get(),
            'E7': E7.get(),
            'E8': E8.get(),
          }
    
    
        )
      mydb.commit()
      mydb.close()
      '''E1.delete(0, END)
      E2.delete(0, END)
      E3.delete(0, END)
      E4.delete(0, END)
      E5.delete(0, END)
      E6.delete(0, END)
      E7.delete(0, END)
      E8.delete(0, END)'''
   
    


    style=ttk.Style()
    style.theme_use('default')
    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map("Treeview",
    background=[('selected',"#347083")])

    tree_frame=Frame(Top)
    tree_frame.pack(pady=10)

    tree_scroll=Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT,fill=Y)

    my_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="extended")
    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)


    my_tree['columns']=("Inventory ID","Inventory Name","Inventory Type","Inventory Quantity","Inventory Description","Price per unit","Total Amount","Manager ID")
    my_tree.column("#0",width=0,stretch=NO)
    my_tree.column("Inventory ID",anchor=W,width=140)
    my_tree.column("Inventory Name",anchor=W,width=140)
    my_tree.column("Inventory Type",anchor=CENTER,width=140)
    my_tree.column("Inventory Quantity",anchor=CENTER,width=140)
    my_tree.column("Inventory Description",anchor=CENTER,width=140)
    my_tree.column("Price per unit",anchor=CENTER,width=140)
    my_tree.column("Total Amount",anchor=CENTER,width=140)
    my_tree.column("Manager ID",anchor=CENTER,width=140)


    my_tree.heading("#0", text="",anchor=W)
    my_tree.heading("Inventory ID", text="Inventory ID",anchor=W)
    my_tree.heading("Inventory Name", text="Inventory Name",anchor=CENTER)
    my_tree.heading("Inventory Type", text="Inventory Type",anchor=CENTER)
    my_tree.heading("Inventory Quantity", text="Inventory Quantity",anchor=CENTER)
    my_tree.heading("Inventory Description", text="Inventory Description",anchor=CENTER)
    my_tree.heading("Price per unit", text="Price per unit",anchor=CENTER)
    my_tree.heading("Total Amount", text="Total Amount",anchor=CENTER)
    my_tree.heading("Manager ID", text="Manager ID",anchor=CENTER)




    my_tree.tag_configure('oddrow',background="white")
    my_tree.tag_configure('evenrow',background="lightblue")






    data_frame =LabelFrame(Top, text="Record")
    data_frame.pack(fill="x",expand="yes",padx=20)

    L1=Label(data_frame,text="Inventory ID",font=("Rockwell Extra Black",16))
    L1.grid(row=0,column=0,padx=10,pady=10)
    L2=Label(data_frame,text="Inventory Name",font=("Rockwell Extra Black",16))
    L2.grid(row=0,column=2,padx=10,pady=10)
    L3=Label(data_frame,text="Inventory Type",font=("Rockwell Extra Black",16))
    L3.grid(row=0,column=4,padx=10,pady=10)
    L4=Label(data_frame,text="Inventory Quantity",font=("Rockwell Extra Black",16))
    L4.grid(row=1,column=0,padx=10,pady=10)
    L5=Label(data_frame,text="Inventory Description",font=("Rockwell Extra Black",16))
    L5.grid(row=1,column=2,padx=10,pady=10)
    L6=Label(data_frame,text="Price per unit",font=("Rockwell Extra Black",16))
    L6.grid(row=1,column=4,padx=10,pady=10)
    L7=Label(data_frame,text="Total Amount",font=("Rockwell Extra Black",16))
    L7.grid(row=1,column=6,padx=10,pady=10) 
    L8=Label(data_frame,text="Manager ID",font=("Rockwell Extra Black",16))
    L8.grid(row=0,column=6,padx=10,pady=10) 

    E1=Entry(data_frame)
    E1.grid(row=0,column=1,padx=10,pady=10)
    E2=Entry(data_frame)
    E2.grid(row=0,column=3,padx=10,pady=10)
    E3=Entry(data_frame)
    E3.grid(row=0,column=5,padx=10,pady=10)
    E4=Entry(data_frame)
    E4.grid(row=1,column=1,padx=10,pady=10) 
    E5=Entry(data_frame)
    E5.grid(row=1,column=3,padx=10,pady=10)
    E6=Entry(data_frame)
    E6.grid(row=1,column=5,padx=10,pady=10)
    E7=Entry(data_frame)
    E7.grid(row=1,column=7,padx=10,pady=10)
    E8=Entry(data_frame)
    E8.grid(row=0,column=7,padx=10,pady=10)

    button_frame = LabelFrame(Top, text="Commands")
    button_frame.pack(fill="x",expand="yes",padx=20)

    B1=Button(button_frame,text="Update Record",command=update)
    B1.grid(row=0,column=0,padx=10,pady=10)

    B3=Button(button_frame,text="Select Record",command=select)
    B3.grid(row=0,column=2,padx=10,pady=10)
    B4=Button(button_frame,text="Add Record",command=submit)
    B4.grid(row=0,column=3,padx=10,pady=10)
    B5=Button(button_frame,text="Remove Selected",command=remove_s)
    B5.grid(row=0,column=4,padx=20,pady=10)
    B5=Button(button_frame,text="Clear",command=clear)
    B5.grid(row=0,column=5,padx=10,pady=10)
    query_database()

  elif(S and M in L2):
    Top=Toplevel()
    Top.title("Accounts")
    def select():
     E1.delete(0, END)
     E2.delete(0, END)
     E3.delete(0, END)
     E4.delete(0, END)
     E5.delete(0, END)
    

     selected = my_tree.focus()
     values = my_tree.item(selected,'values')


     E1.insert(0,values[0])
     E2.insert(0,values[1])
     E3.insert(0,values[2])
     E4.insert(0,values[3])
     E5.insert(0,values[4])
     E6.insert(0,values[5])
     
     



    def clear():
     E1.delete(0, END)
     E2.delete(0, END)
     E3.delete(0, END)
     E4.delete(0, END)
     E5.delete(0, END)
     E6.delete(0, END)
     
     return

    def remove_s():
     x=my_tree.selection()[0]
     my_tree.delete(x)
     return

    def update():
     selected = my_tree.focus()
     my_tree.item(selected,text="",values=(E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),))
     return

    def query_database():
     conn=sqlite3.connect('financial_management.db')
     c=conn.cursor()

     c.execute("SELECT * FROM accounts")
     records=c.fetchall()

     global count
     count=0

     for record in records:
      if count %2 ==0:
        my_tree.insert(parent='',index='end',iid=count,text='',values=( record[0], record[1],record[2],record[3],record[4],record[5]),tags=('evenrow',))
      else:
        my_tree.insert(parent='',index='end',iid=count,text='',values=(  record[0], record[1],record[2],record[3],record[4],record[5]),tags=('oddrow',))
      count+=1
     conn.commit()
     conn.close()



    def submit():
     conn=sqlite3.connect('financial_management.db')
     cursor = conn.cursor()
     cursor.execute("INSERT INTO accounts VALUES(:E1,:E2,:E3,:E4,:E5,:E6)",
          {
            'E1': E1.get(),
            'E2': E2.get(),
            'E3': E3.get(),
            'E4': E4.get(),
            'E5': E5.get(),
            'E6': E6.get(),
          
          }
    
    
    )
     conn.commit()
     conn.close()
     E1.delete(0, END)
     E2.delete(0, END)
     E3.delete(0, END)
     E4.delete(0, END)
     E5.delete(0, END)
     E6.delete(0, END)

   
    


    style=ttk.Style()
    style.theme_use('default')
    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map("Treeview",
    background=[('selected',"#347083")])

    tree_frame=Frame(Top)
    tree_frame.pack(pady=10)

    tree_scroll=Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT,fill=Y)

    my_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="extended")
    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)


    my_tree['columns']=("Account ID","Bank Name","Bank Account No.","Balance","Account Type","Manager ID")
    my_tree.column("#0",width=0,stretch=NO)
    my_tree.column("Account ID",anchor=W,width=140)
    my_tree.column("Bank Name",anchor=CENTER,width=140)
    my_tree.column("Bank Account No.",anchor=CENTER,width=140)
    my_tree.column("Balance",anchor=CENTER,width=140)
    my_tree.column("Account Type",anchor=CENTER,width=140)
    my_tree.column("Manager ID",anchor=CENTER,width=140)

    my_tree.heading("#0", text="",anchor=W)
    my_tree.heading("Account ID", text="Account ID",anchor=W)
    my_tree.heading("Bank Name", text="Bank Name",anchor=CENTER)
    my_tree.heading("Bank Account No.", text="Bank Account No.",anchor=CENTER)
    my_tree.heading("Balance", text="Ex-Gst Amount",anchor=CENTER)
    my_tree.heading("Account Type", text="Gst",anchor=CENTER)
    my_tree.heading("Manager ID", text="Manager ID",anchor=CENTER)




    my_tree.tag_configure('oddrow',background="white")
    my_tree.tag_configure('evenrow',background="lightblue")






    data_frame =LabelFrame(Top, text="Record")
    data_frame.pack(fill="x",expand="yes",padx=20)

    L1=Label(data_frame,text="Account ID",font=("Rockwell Extra Black",16))
    L1.grid(row=0,column=0,padx=10,pady=10)
    L3=Label(data_frame,text="Bank Name",font=("Rockwell Extra Black",16))
    L3.grid(row=0,column=2,padx=10,pady=10)
    L4=Label(data_frame,text="Bank Account No.",font=("Rockwell Extra Black",16))
    L4.grid(row=0,column=4,padx=10,pady=10)
    L5=Label(data_frame,text="Balance",font=("Rockwell Extra Black",16))
    L5.grid(row=0,column=6,padx=10,pady=10)
    L6=Label(data_frame,text="Account Type",font=("Rockwell Extra Black",16))
    L6.grid(row=1,column=0,padx=10,pady=10) 
    L7=Label(data_frame,text="Manager ID",font=("Rockwell Extra Black",16))
    L7.grid(row=1,column=2,padx=10,pady=10) 

    E1=Entry(data_frame)
    E1.grid(row=0,column=1,padx=10,pady=10)
    E2=Entry(data_frame)
    E2.grid(row=0,column=3,padx=10,pady=10)
    E3=Entry(data_frame)
    E3.grid(row=0,column=5,padx=10,pady=10)
    E4=Entry(data_frame)
    E4.grid(row=0,column=7,padx=10,pady=10) 
    E5=Entry(data_frame)
    E5.grid(row=1,column=1,padx=10,pady=10)
    E6=Entry(data_frame)
    E6.grid(row=1,column=3,padx=10,pady=10)





    button_frame = LabelFrame(Top, text="Commands")
    button_frame.pack(fill="x",expand="yes",padx=20)

    B1=Button(button_frame,text="Update Record",command=update)
    B1.grid(row=0,column=0,padx=10,pady=10)

    B3=Button(button_frame,text="Select Record",command=select)
    B3.grid(row=0,column=2,padx=10,pady=10)
    B4=Button(button_frame,text="Add Record",command=submit)
    B4.grid(row=0,column=3,padx=10,pady=10)
    B5=Button(button_frame,text="Remove Selected",command=remove_s)
    B5.grid(row=0,column=4,padx=10,pady=10)
    B5=Button(button_frame,text="Clear",command=clear)
    B5.grid(row=0,column=5,padx=10,pady=10)
    query_database()
  elif(S and M in L4):
    Top=Toplevel()
    Top.title("Activity_Logs")
    def select():
      E1.delete(0, END)
      E2.delete(0, END)
      E3.delete(0, END)
      E4.delete(0, END)
      E5.delete(0, END)
      

 
      selected = my_tree.focus()
      values = my_tree.item(selected,'values')


      E1.insert(0,values[0])
      E2.insert(0,values[1])
      E3.insert(0,values[2])
      E4.insert(0,values[3])
      E5.insert(0,values[4])
      



    def clear():
      E1.delete(0, END)
      E2.delete(0, END)
      E3.delete(0, END)
      E4.delete(0, END)
      E5.delete(0, END)
      
      return

    def remove_s():
     x=my_tree.selection()[0]
     my_tree.delete(x)
     return

    def update():
     selected = my_tree.focus()
     my_tree.item(selected,text="",values=(E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),))
     return

    def query_database():
     conn=sqlite3.connect('financial_management.db')
     c=conn.cursor()

     c.execute("SELECT * FROM log")
     records=c.fetchall()

     global count
     count=0

     for record in records:
      if count %2 ==0:
        my_tree.insert(parent='',index='end',iid=count,text='',values=( record[0], record[1],record[2],record[3],record[4]),tags=('evenrow',))
      else:
        my_tree.insert(parent='',index='end',iid=count,text='',values=(  record[0], record[1],record[2],record[3],record[4]),tags=('oddrow',))
      count+=1
     conn.commit()
     conn.close()
    



    def submit():
      mydb=sqlite3.connect('financial_management.db')
      cursor = mydb.cursor()
      cursor.execute("INSERT INTO activity_log VALUES(:E1,:E2,:E3,:E4,:E5)",
          {
            'E1': E1.get(),
            'E2': E2.get(),
            'E3': E3.get(),
            'E4': E4.get(),
            'E5': E5.get(),
       
          }
    
    
        )
      mydb.commit()
      mydb.close()
      E1.delete(0, END)
      E2.delete(0, END)
      E3.delete(0, END)
      E4.delete(0, END)
      E5.delete(0, END)
    
   
    


    style=ttk.Style()
    style.theme_use('default')
    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map("Treeview",
    background=[('selected',"#347083")])

    tree_frame=Frame(Top)
    tree_frame.pack(pady=10)

    tree_scroll=Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT,fill=Y)

    my_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="extended")
    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)


    my_tree['columns']=("Log ID","Log Type","Log Type ID","Log Date","Manager ID")
    my_tree.column("#0",width=0,stretch=NO)
    my_tree.column("Log ID",anchor=W,width=140)
    my_tree.column("Log Type",anchor=W,width=140)
    my_tree.column("Log Type ID",anchor=CENTER,width=140)
    my_tree.column("Log Date",anchor=CENTER,width=140)
    my_tree.column("Manager ID",anchor=CENTER,width=140)


    my_tree.heading("#0", text="",anchor=W)
    my_tree.heading("Log ID", text="Log ID",anchor=W)
    my_tree.heading("Log Type", text="Log Type",anchor=CENTER)
    my_tree.heading("Log Type ID", text="Log Type ID",anchor=CENTER)
    my_tree.heading("Log Date", text="Log Date",anchor=CENTER)
    my_tree.heading("Manager ID", text="Manager ID",anchor=CENTER)




    my_tree.tag_configure('oddrow',background="white")
    my_tree.tag_configure('evenrow',background="lightblue")






    data_frame =LabelFrame(Top, text="Record")
    data_frame.pack(fill="x",expand="yes",padx=20)

    L1=Label(data_frame,text="Log ID",font=("Rockwell Extra Black",16))
    L1.grid(row=0,column=0,padx=10,pady=10)
    L2=Label(data_frame,text="Log Type",font=("Rockwell Extra Black",16))
    L2.grid(row=0,column=2,padx=10,pady=10)
    L3=Label(data_frame,text="Log Type ID",font=("Rockwell Extra Black",16))
    L3.grid(row=0,column=4,padx=10,pady=10)
    L4=Label(data_frame,text="Log Date",font=("Rockwell Extra Black",16))
    L4.grid(row=1,column=0,padx=10,pady=10)
    L5=Label(data_frame,text="Manager ID",font=("Rockwell Extra Black",16))
    L5.grid(row=1,column=2,padx=10,pady=10)
    

    E1=Entry(data_frame)
    E1.grid(row=0,column=1,padx=10,pady=10)
    E2=Entry(data_frame)
    E2.grid(row=0,column=3,padx=10,pady=10)
    E3=Entry(data_frame)
    E3.grid(row=0,column=5,padx=10,pady=10)
    E4=Entry(data_frame)
    E4.grid(row=1,column=1,padx=10,pady=10) 
    E5=Entry(data_frame)
    E5.grid(row=1,column=3,padx=10,pady=10)
    

    button_frame = LabelFrame(Top, text="Commands")
    button_frame.pack(fill="x",expand="yes",padx=20)

    B1=Button(button_frame,text="Update Record",command=update)
    B1.grid(row=0,column=0,padx=10,pady=10)

    B3=Button(button_frame,text="Select Record",command=select)
    B3.grid(row=0,column=2,padx=10,pady=10)
    B4=Button(button_frame,text="Add Record",command=submit)
    B4.grid(row=0,column=3,padx=10,pady=10)
    B5=Button(button_frame,text="Remove Selected",command=remove_s)
    B5.grid(row=0,column=4,padx=20,pady=10)
    B5=Button(button_frame,text="Clear",command=clear)
    B5.grid(row=0,column=5,padx=10,pady=10)
    query_database()


  return



H1=Label(root,text="User Type",font=("Rockwell Extra Black",16)).place(x=450,y=202)
H2=Label(root,text="UserID",font=("Rockwell Extra Black",16)).place(x=450,y=233)
H3=Label(root,text="Password",font=("Rockwell Extra Black",16)).place(x=450,y=260)
S1=Entry(root,bg="Light Grey",width=30)
S1.place(x=600,y=240)
S2=Entry(root,bg="Light Grey",width=30)
S2.place(x=600,y=267)
J1=Button(root,text="Login",padx=40,pady=10,command=open)
J1.place(x=600,y=300)
clicked = StringVar()
drop = OptionMenu(root, clicked,"Account Manager","Stock Manager", " Inventory Manager", "Log Manager")
drop.place(x=597,y=199)
drop.config(width=20)
drop.config(bg='light blue')

root.mainloop()