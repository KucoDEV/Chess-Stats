import tkinter as tk
from tkinter import simpledialog, messagebox
import json

# Chargement ou initialisation des données
DATA_FILE = "chess_stats.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "elo": 1224,
            "games_played": 0,
            "games_goal": 50,
            "victories": 0,
            "defeats": 0,
            "draws": 0
        }

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# Ajout d'une partie
def add_game(result):
    global data
    if data["games_played"] < data["games_goal"]:
        try:
            # Différentes conditions selon le type de partie
            if result == "victory":
                elo_change = simpledialog.askinteger(
                    "Changement ELO (Victoire)",
                    "Entrez le changement positif d'ELO :",
                    minvalue=1  # Doit être un nombre positif
                )
                if elo_change is None:
                    return  # Annuler
                data["elo"] += elo_change
                data["victories"] += 1

            elif result == "defeat":
                elo_change = simpledialog.askinteger(
                    "Changement ELO (Défaite)",
                    "Entrez le changement négatif d'ELO :",
                    minvalue=-100,  # Doit être un nombre négatif
                    maxvalue=-1
                )
                if elo_change is None:
                    return  # Annuler
                data["elo"] += elo_change
                data["defeats"] += 1

            elif result == "draw":
                elo_change = simpledialog.askstring(
                    "Changement ELO (Nulle)",
                    "Entrez '-' si vous avez perdu des points, sinon laissez vide :"
                )
                if elo_change == "-":
                    elo_change_value = simpledialog.askinteger(
                        "Perte d'ELO (Nulle)",
                        "Entrez le changement négatif d'ELO :",
                        minvalue=-100,
                        maxvalue=-1
                    )
                    if elo_change_value is not None:
                        data["elo"] += elo_change_value
                elif elo_change == "" or elo_change is None:
                    pass  # Aucun changement d'ELO
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

# Mise à jour de l'affichage
def update_stats():
    elo_label.config(text=f"ELO: {data['elo']}")
    games_label.config(text=f"Parties jouées : {data['games_played']} / {data['games_goal']}")
    victories_label.config(text=f"Victoires : {data['victories']}")
    defeats_label.config(text=f"Défaites : {data['defeats']}")
    draws_label.config(text=f"Nulles : {data['draws']}")

# Chargement des données initiales
data = load_data()

# Création de l'interface
root = tk.Tk()
root.title("Stats Chess")

# Affichage des statistiques
elo_label = tk.Label(root, text=f"ELO: {data['elo']}", font=("Arial", 14))
elo_label.pack()

games_label = tk.Label(root, text=f"Parties jouées : {data['games_played']} / {data['games_goal']}", font=("Arial", 14))
games_label.pack()

victories_label = tk.Label(root, text=f"Victoires : {data['victories']}", font=("Arial", 14))
victories_label.pack()

defeats_label = tk.Label(root, text=f"Défaites : {data['defeats']}", font=("Arial", 14))
defeats_label.pack()

draws_label = tk.Label(root, text=f"Nulles : {data['draws']}", font=("Arial", 14))
draws_label.pack()

# Boutons pour ajouter un résultat
tk.Button(root, text="Ajouter Victoire", command=lambda: add_game("victory"), bg="green").pack(fill=tk.X)
tk.Button(root, text="Ajouter Défaite", command=lambda: add_game("defeat"), bg="red").pack(fill=tk.X)
tk.Button(root, text="Ajouter Nulle", command=lambda: add_game("draw"), bg="gray").pack(fill=tk.X)

# Lancement de l'application
update_stats()
root.mainloop()
