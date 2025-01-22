import tkinter as tk
laud = tk.Tk()
laud.title("Malelaud")

board_size = 400
canvas = tk.Canvas(laud, width=board_size, height=board_size, bg="white")
canvas.pack()
tile_size = board_size // 8
colors = ["#f0d9b5", "#b58863"]
for row in range(8):
    for col in range(8):
        color = colors[(row + col) % 2]
        x1 = col * tile_size
        y1 = row * tile_size
        x2 = x1 + tile_size
        y2 = y1 + tile_size
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
laud.mainloop()