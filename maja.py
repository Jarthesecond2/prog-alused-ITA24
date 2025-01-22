from tkinter import *

raam = Tk()
raam.title("Maja")

maja = Canvas(height=500, width=500, bg="white")
maja.pack()

maja.create_rectangle(100, 500, 200, 400, fill="orange", outline="orange")
maja.create_polygon(90, 400, 210, 400, 150, 350, fill="red", outline="orange")

maja.create_rectangle(120, 470, 150, 440, fill="aqua")
maja.create_line(135, 470, 135, 440)
maja.create_line(120, 455, 150, 455)

maja.create_rectangle(160, 500, 190, 430, fill="brown", outline="chocolate")
maja.create_polygon(170, 367, 170, 340, 190, 340, 190, 384, outline="#CB4132", fill="#CB4154")
raam.mainloop()