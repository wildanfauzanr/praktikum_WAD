import tkinter as tk

#preparation
root = tk.Tk()
root.title("KONVERSI SUHU (C)")
canvas1 = tk.Canvas(root, width = 400, height = 300, relief="raised")
canvas1.pack()

#label
label1 = tk.Label(root, text="KONVERSI SUHU (CELCIUS)",fg='blue')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text="Masukan suhu yang akan dikonveris :")
label2.config(font=('helvetica', 10))
canvas1.create_window(200,80,window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 100, window=entry1)


#fucntion hasil
def suhu():
    data = entry1.get()
    label3 = tk.Label(root, text="Hasil konversi "+data+" celcius :" )
    canvas1.create_window(200,200,window=label3)
    label4 = tk.Label(root, text=f"Reamur = {round(float(data)*0.8,2)}")
    canvas1.create_window(200, 230, window=label4)
    label5 = tk.Label(root, text=f"Fahrenheit = {round(float(data)*1.8+32,2)}")
    canvas1.create_window(200, 250, window=label5)
    label6 = tk.Label(root, text=f"Kelvin = {round(float(data)+273.15,2)}")
    canvas1.create_window(200, 270, window=label6)

#button
button1 = tk.Button(text="Konversi", command= suhu, bg='blue', fg='white', font=('helvetica',9,'bold'))
canvas1.create_window(200, 150, window=button1)


root.mainloop()