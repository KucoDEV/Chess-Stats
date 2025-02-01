# Chess Stats - Amélioration de l'interface

## 📌 Description

Chess Stats est une application en **Python** avec **Tkinter** et **ttkbootstrap** qui permet de suivre vos statistiques de parties d'échecs. Cette version améliorée propose une interface plus moderne et ergonomique tout en conservant les fonctionnalités d'origine.

---

## 🛠️ Fonctionnalités

- 🎨 **Interface modernisée** avec **ttkbootstrap** et un thème amélioré
- 📈 Suivi en temps réel de votre **ELO**
- 🎯 Définition d'un objectif de parties à jouer
- ✅ Ajout rapide des résultats :
  - **Victoire** ➝ Augmente l'ELO
  - **Défaite** ➝ Diminue l'ELO
  - **Nulle** ➝ Option pour modifier l'ELO
- 🗂️ Sauvegarde automatique des données dans un fichier `chess_stats.json`

---

## 📸 Aperçu de l'interface

L'interface propose une présentation plus claire des statistiques avec des boutons colorés et stylisés.

---

## 🚀 Installation et utilisation

### 📥 Prérequis

- **Python 3.x** installé
- Bibliothèques nécessaires : `tkinter`, `json`, `ttkbootstrap`

### 🏗️ Installation

1. **Clonez ce dépôt** :
   ```sh
   git clone https://github.com/KucoDEV/chess-stats
   cd chess-stats
   ```

2. **Installez les dépendances** :
   ```sh
   pip install ttkbootstrap
   ```

3. **Lancez l'application** :
   ```sh
   python main.py
   ```

---

## 📂 Structure du projet

```
chess-stats/
│── main.py                   # Code principal avec interface améliorée avec console
│── main.pyw                  # Code principal avec interface améliorée sans console
│── chess_stats.json          # Fichier de stockage des statistiques
│── README.md                 # Documentation du projet
```

---

## 🤖 Fonctionnement du code

### 🏆 Gestion des parties

L'application charge les statistiques depuis `chess_stats.json`. Vous pouvez ajouter une **victoire, une défaite ou une nulle** via les boutons interactifs.

L'évolution de l'ELO est demandée dynamiquement via des boîtes de dialogue `tkinter`.

### 🔄 Sauvegarde automatique

À chaque mise à jour des statistiques, le fichier `chess_stats.json` est mis à jour.

---

## 📜 Licence

Ce projet est sous licence **MIT**. Vous êtes libre de le modifier et de le redistribuer.