import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import json
import ttkbootstrap as tb

DATA_FILE = "chess_stats.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "elo": 0,
            "games_played": 0,
            "games_goal": 50,
            "victories": 0,
            "defeats": 0,
            "draws": 0
        }

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

def add_game(result):
    global data
    if data["games_played"] < data["games_goal"]:
        try:
            if result == "victory":
                elo_change = simpledialog.askinteger("Changement ELO (Victoire)", "Entrez le changement positif d'ELO :", minvalue=1)
                if elo_change is None:
                    return
                data["elo"] += elo_change
                data["victories"] += 1

            elif result == "defeat":
                elo_change = simpledialog.askinteger("Changement ELO (Défaite)", "Entrez le changement négatif d'ELO :", minvalue=-100, maxvalue=-1)
                if elo_change is None:
                    return
                data["elo"] += elo_change
                data["defeats"] += 1

            elif result == "draw":
                elo_change = simpledialog.askstring("Changement ELO (Nulle)", "Entrez '-' si vous avez perdu des points, sinon laissez vide :")
                if elo_change == "-":
                    elo_change_value = simpledialog.askinteger("Perte d'ELO (Nulle)", "Entrez le changement négatif d'ELO :", minvalue=-100, maxvalue=-1)
                    if elo_change_value is not None:
                        data["elo"] += elo_change_value
                elif elo_change == "" or elo_change is None:
                    pass
                else:
                    messagebox.showerror("Erreur", "Veuillez entrer un format valide ('-' ou rien).")
                    return
                data["draws"] += 1

            data["games_played"] += 1
            save_data(data)
            update_stats()
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'ajout de la partie : {e}")
    else:
        messagebox.showinfo("Objectif atteint", "Vous avez atteint l'objectif de parties !")

def update_stats():
    elo_label.config(text=f"ELO: {data['elo']}")
    games_label.config(text=f"Objectif : {data['games_played']} / {data['games_goal']}")
    victories_label.config(text=f"Victoires : {data['victories']}")
    defeats_label.config(text=f"Défaites : {data['defeats']}")
    draws_label.config(text=f"Nulles : {data['draws']}")

data = load_data()

root = tb.Window(themename="superhero")
root.title("Stats Chess")
root.geometry("400x300")

frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, sticky=("N", "W", "E", "S"))

elo_label = ttk.Label(frame, text=f"ELO: {data['elo']}", font=("Arial", 14))
elo_label.grid(row=0, column=0, columnspan=2, pady=5)

games_label = ttk.Label(frame, text=f"Parties jouées : {data['games_played']} / {data['games_goal']}", font=("Arial", 12))
games_label.grid(row=1, column=0, columnspan=2, pady=5)

victories_label = ttk.Label(frame, text=f"Victoires : {data['victories']}", font=("Arial", 12))
victories_label.grid(row=2, column=0, pady=5)

defeats_label = ttk.Label(frame, text=f"Défaites : {data['defeats']}", font=("Arial", 12))
defeats_label.grid(row=3, column=0, pady=5)

draws_label = ttk.Label(frame, text=f"Nulles : {data['draws']}", font=("Arial", 12))
draws_label.grid(row=4, column=0, pady=5)

btn_victory = tb.Button(frame, text="Ajouter Victoire", bootstyle="success", command=lambda: add_game("victory"))
btn_victory.grid(row=5, column=0, columnspan=2, sticky="WE", pady=2)

btn_defeat = tb.Button(frame, text="Ajouter Défaite", bootstyle="danger", command=lambda: add_game("defeat"))
btn_defeat.grid(row=6, column=0, columnspan=2, sticky="WE", pady=2)

btn_draw = tb.Button(frame, text="Ajouter Nulle", bootstyle="secondary", command=lambda: add_game("draw"))
btn_draw.grid(row=7, column=0, columnspan=2, sticky="WE", pady=2)

update_stats()
root.mainloop()
