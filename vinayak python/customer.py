
import tkinter as tk  
import csv 



def Send_data():
    
    cust=entry1.get()
    mobile=entry2.get()
    adres=entry3.get()
    purchased=entry4.get()
    data=["Customer name","Mobile","Adress","Purchased Cost"]

    file_name= "emp.csv"
    with open(file_name,"a", newline="") as employee_data:
        file=csv.writer(employee_data)
        # file.writerow(data)
        file.writerow([cust,mobile,adres,purchased])


    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    print(file_name)

main=tk.Tk()
main.title("Customer Details")
main.geometry("600x600")
#creating a text  for customer name,mobile number,Adress,Purchased cost
label1=tk.Label(main,text="Customer name ",).grid(row=1,column=1)
            
label2=tk.Label(main,text="Mobile number").grid(row=2,column=1)
    
label3=tk.Label(main,text="Adress").grid(row=3,column=1)
label4=tk.Label(main,text="Purchased cost").grid(row=4,column=1)

label5=tk.Button(main,text="Send",command=Send_data).grid(row=5,column=2)#creating for button

    
entry1=tk.Entry(main)
entry1.grid(row=1,column=2)#creating a text field for customer name 
entry2=tk.Entry(main)
entry2.grid(row=2,column=2)#creating a text field for mobile number  
entry3=tk.Entry(main)
entry3.grid(row=3,column=2)#creating a text field for Adress 
entry4=tk.Entry(main)
entry4.grid(row=4,column=2)#creating a text field for purchased cost 

        # entry5=tk.Entry(main).grid(row=4,column=2)
main.mainloop()#used for continous  running code 
 
