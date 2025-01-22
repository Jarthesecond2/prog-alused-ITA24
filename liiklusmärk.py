import tkinter as tk

märk = tk.Tk()
märk.title("Liiklusmärk ")

canvas = tk.Canvas(märk, width=400, height=400, bg="white")
canvas.pack()

canvas.create_polygon(75, 300, 325, 300, 200, 75, outline="red", width= 20, fill="white")
canvas.create_rectangle(120, 280, 280, 275, fill="black")
canvas.create_rectangle(160, 275, 240, 266, fill="black")

märk.mainloop()