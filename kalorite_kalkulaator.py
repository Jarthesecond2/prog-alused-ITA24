import tkinter as tk

def mees_valitud():
    sugu_var.set("Mees")
    
def naine_valitud():
    sugu_var.set("Naine")
    
def aktiivsus_valitud(aktiivsus):
    aktiivsus_var.set(aktiivsus)

def bmr_calculate():
    vanus = int(vanus_entry.get())
    pikkus = int(pikkus_entry.get())
    kaal = int(kaal_entry.get())
    
    if sugu_var.get() == "Mees":
        bmr = 88.36 + (13.4 * kaal) + (4.8 * pikkus) - (5.7 * vanus)
    else:
        bmr = 447.6 + (9.2 * kaal) + (3.1 * pikkus) - (4.3 * vanus)

    aktiivsus = aktiivsus_var.get()
    if aktiivsus == "Istuv eluviis":
        aktiivsuse_tase = 1.2
    elif aktiivsus == "Väike aktiivsus":
        aktiivsuse_tase = 1.375
    elif aktiivsus == "Mõõdukas aktiivsus":
        aktiivsuse_tase = 1.55
    elif aktiivsus == "Kõrge aktiivsus":
        aktiivsuse_tase = 1.725
    else:
        aktiivsuse_tase = 1.9

    kalorid = bmr * aktiivsuse_tase
    toitumise_tulemus.set(f"Sinu igapäevane kalorivajadus on {kalorid:.2f} kcal")

root = tk.Tk()
root.title("Kalorivajaduse Kalkulaator")

sugu_var = tk.StringVar(value="Mees")
aktiivsus_var = tk.StringVar(value="Istuv eluviis")
toitumise_tulemus = tk.StringVar()

vanus_label = tk.Label(root, text="Vanus (aastad):")
vanus_label.grid(row=0, column=0)
vanus_entry = tk.Entry(root)
vanus_entry.grid(row=0, column=1)

pikkus_label = tk.Label(root, text="Pikkus (cm):")
pikkus_label.grid(row=1, column=0)
pikkus_entry = tk.Entry(root)
pikkus_entry.grid(row=1, column=1)

kaal_label = tk.Label(root, text="Kaal (kg):")
kaal_label.grid(row=2, column=0)
kaal_entry = tk.Entry(root)
kaal_entry.grid(row=2, column=1)

sugu_label = tk.Label(root, text="Sugu:")
sugu_label.grid(row=3, column=0)

tk.Button(root, text="Mees", command=mees_valitud).grid(row=3, column=1)
tk.Button(root, text="Naine", command=naine_valitud).grid(row=3, column=2)

aktiivsus_label = tk.Label(root, text="Kehaline aktiivsus:")
aktiivsus_label.grid(row=4, column=0)

tk.Button(root, text="Istuv eluviis", command=lambda: aktiivsus_valitud("Istuv eluviis")).grid(row=4, column=1)
tk.Button(root, text="Väike aktiivsus", command=lambda: aktiivsus_valitud("Väike aktiivsus")).grid(row=4, column=2)
tk.Button(root, text="Mõõdukas aktiivsus", command=lambda: aktiivsus_valitud("Mõõdukas aktiivsus")).grid(row=4, column=3)
tk.Button(root, text="Kõrge aktiivsus", command=lambda: aktiivsus_valitud("Kõrge aktiivsus")).grid(row=4, column=4)
tk.Button(root, text="Väga kõrge aktiivsus", command=lambda: aktiivsus_valitud("Väga kõrge aktiivsus")).grid(row=4, column=5)

calculate_button = tk.Button(root, text="Arvuta kalorivajadus", command=bmr_calculate)
calculate_button.grid(row=5, column=1, columnspan=2, pady=10)

toitumise_label = tk.Label(root, textvariable=toitumise_tulemus)
toitumise_label.grid(row=6, column=0, columnspan=3)

root.mainloop()