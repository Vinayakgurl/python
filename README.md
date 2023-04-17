import tkinter as Tk
def calculate():
    principal = int(principal.get())
    rate=str(rate.get())
    month=str(month.get())
    EMI=prin*rate*(pow((1+rate),month)/(pow((1+rate),month)-1))
    total_payment=EMI*month
    total_interest_value=total_payment-prin

    
main_window = Tk.Tk()
main_window.title("EMI Calculator")
main_window.geometry("")
Tk.Label(main_window,text="Mobile Name")
Tk.Label(main_window,text="Amount",padx=10,pady=10).grid(row=0)
Tk.Label(main_window,text="Interest",padx=10,pady=10).grid(row=1)
Tk.Label(main_window,text="Duration",padx=10,pady=10).grid(row=2)
Tk.Button(main_window,text="Calculate",command=calculate,padx=10,pady=10).grid(row=3,columnspan=2)

principal = Tk.IntVar(main_window)
rate = Tk.StringVar(main_window)
month=Tk.StringVar(main_window)
emi=Tk.StringVar(main_window)
Tottal_Interest= Tk.StringVar(main_window)
Tottal_payment=Tk.StringVar(main_window)
principal.set(0)
month.set(0)
emi.set(0)

Tk.Entry(main_window,text= principal, padx=10,pady=10).grid(row=0,colum=1)
Tk.Entry(main_window,text= rate, padx=10,pady=10).grid(row=1,colum=1)
Tk.Entry(main_window,text= month, padx=10,pady=10).grid(row=2,colum=1)
Tk.Label(main_window,text="EMI",padx=10,pady=10).grid(row=4,columnspan=2)
Tk.Label(main_window,text="emi", font=("Arial",16),padx=10,pady=10).grid(row=4,columnspan=2)
Tk.Label(main_window,text="total_Interest",padx=10,pady=10).grid(row=5,columnspan=2)
Tk.Label(main_window,text="total_interest",font=("Arial",16),padx=10,pady=10).grid(row=5,columnspan=2)
Tk.Label(main_window,text="total_Payment",padx=10,pady=10).grid(row=6,columnspan=2)
Tk.Label(main_window,text="total payment",font=("Arial",16),padx=10,pady=10).grid(row=5,columnspan=2)
main_window.mainloop()
