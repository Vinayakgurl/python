import csv
import tkinter as tk

def save_data():
    filename = "data.csv"
    
    # Get the data from the entry fields
    name = name_entry.get()
    age = age_entry.get()
    profession = profession_entry.get()

    # Write data to CSV file
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, profession])
    
    # Clear the entry fields
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    profession_entry.delete(0, tk.END)
    
    print("Data has been written to", filename)

# Create a Tkinter window
window = tk.Tk()

# Create labels and entry fields
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

profession_label = tk.Label(window, text="Profession:")
profession_label.pack()
profession_entry = tk.Entry(window)
profession_entry.pack()

# Create a button to save the data
save_button = tk.Button(window, text="Save", command=save_data)
save_button.pack()

# Start the Tkinter event loop
window.mainloop()
