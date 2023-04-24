

import tkinter as Tk
def calculate():
    input_principal = (principal.get())
    input_rate=float((rate.get())/12/100)
    input_month=(month.get())
    input_emi=input_principal * input_rate * (pow((1+input_rate),input_month)/(pow((1+input_rate),input_month)-1)) 
    emi.set(input_emi)
    total_payment=float(input_emi * input_month )
    Total_payment.set(format(total_payment))
    total_interest_value=total_payment-input_principal
    Total_Interest.set(format(total_interest_value))
  
main_window = Tk.Tk() 
main_window.title("EMI Calculator") 
main_window.geometry("") 
Tk.Label(main_window,text="Mobile Name") 
Tk.Label(main_window,text="Amount", padx=10,pady=10).grid(row=0)
Tk.Label(main_window,text="Interest", padx=10,pady=10).grid(row=1)
Tk.Label(main_window,text="Duration", padx=10,pady=10).grid(row=2) 
Tk.Button(main_window,text="Calculate", command=calculate,padx=10,pady=10).grid(row=3,columnspan=2)

principal = Tk.IntVar(main_window) 
rate = Tk.IntVar(main_window)
month=Tk.IntVar(main_window)
emi=Tk.IntVar(main_window) 
Total_Interest= Tk.StringVar(main_window)
Total_payment=Tk.StringVar(main_window)



Tk.Entry(main_window,textvariable= principal).grid(row=0,column=1) 
Tk.Entry(main_window,textvariable= rate).grid(row=1,column=1) 
Tk.Entry(main_window,textvariable= month).grid(row=2,column=1) 
Tk.Label(main_window,text="EMI", padx=10,pady=10).grid(row=4,columnspan=2)
Tk.Label(main_window,textvariable=emi, font=("Arial",16),padx=10,pady=10).grid(row=5,columnspan=2)
Tk.Label(main_window,text="TOTAL_INTEREST").grid(row=6,columnspan=2) 
Tk.Label(main_window,textvariable=Total_Interest,font=("Arial",16),padx=10,pady=10).grid(row=7,columnspan=2) 
Tk.Label(main_window,text="TOTAL_PAYMENT").grid(row=8,columnspan=2) 
Tk.Label(main_window,textvariable=Total_payment,font=("Arial",16,),padx=10,pady=10).grid(row=9,columnspan=2)
main_window.mainloop()