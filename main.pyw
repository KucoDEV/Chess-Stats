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
                elo_change = simpledialog.askinteger("ELO Change (Victory)", "Enter positive ELO change:", minvalue=1)
                if elo_change is None:
                    return
                data["elo"] += elo_change
                data["victories"] += 1

            elif result == "defeat":
                elo_change = simpledialog.askinteger("ELO Change (Defeat)", "Enter negative ELO change:", minvalue=-100, maxvalue=-1)
                if elo_change is None:
                    return
                data["elo"] += elo_change
                data["defeats"] += 1

            elif result == "draw":
                elo_change = simpledialog.askstring("ELO Change (Nil)", "Enter '-' if you have lost points, otherwise leave blank:")
                if elo_change == "-":
                    elo_change_value = simpledialog.askinteger("ELO Loss", "Enter negative ELO change:", minvalue=-100, maxvalue=-1)
                    if elo_change_value is not None:
                        data["elo"] += elo_change_value
                elif elo_change == "" or elo_change is None:
                    pass
                else:
                    messagebox.showerror("Error", "Please enter a valid format ('-' or nothing).")
                    return
                data["draws"] += 1

            data["games_played"] += 1
            save_data(data)
            update_stats()
        except Exception as e:
            messagebox.showerror("Error", f"Error while adding the game: {e}")
    else:
        messagebox.showinfo("Objective achieved", "You have reached the game objective!")

def update_stats():
    elo_label.config(text=f"ELO: {data['elo']}")
    games_label.config(text=f"Goal : {data['games_played']} / {data['games_goal']}")
    victories_label.config(text=f"Victories : {data['victories']}")
    defeats_label.config(text=f"Defeats : {data['defeats']}")
    draws_label.config(text=f"Draws : {data['draws']}")

data = load_data()

root = tb.Window(themename="superhero")
root.title("Stats Chess")
root.geometry("400x300")

frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, sticky=("N", "W", "E", "S"))

elo_label = ttk.Label(frame, text=f"ELO: {data['elo']}", font=("Arial", 14))
elo_label.grid(row=0, column=0, columnspan=2, pady=5)

games_label = ttk.Label(frame, text=f"Games played : {data['games_played']} / {data['games_goal']}", font=("Arial", 12))
games_label.grid(row=1, column=0, columnspan=2, pady=5)

victories_label = ttk.Label(frame, text=f"Victories : {data['victories']}", font=("Arial", 12))
victories_label.grid(row=2, column=0, pady=5)

defeats_label = ttk.Label(frame, text=f"Defeats : {data['defeats']}", font=("Arial", 12))
defeats_label.grid(row=3, column=0, pady=5)

draws_label = ttk.Label(frame, text=f"Draws : {data['draws']}", font=("Arial", 12))
draws_label.grid(row=4, column=0, pady=5)

btn_victory = tb.Button(frame, text="Add Victory", bootstyle="success", command=lambda: add_game("victory"))
btn_victory.grid(row=5, column=0, columnspan=2, sticky="WE", pady=2)

btn_defeat = tb.Button(frame, text="Add Defeat", bootstyle="danger", command=lambda: add_game("defeat"))
btn_defeat.grid(row=6, column=0, columnspan=2, sticky="WE", pady=2)

btn_draw = tb.Button(frame, text="Add Draw", bootstyle="secondary", command=lambda: add_game("draw"))
btn_draw.grid(row=7, column=0, columnspan=2, sticky="WE", pady=2)

update_stats()
root.mainloop()
