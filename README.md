# Chess Stats

## 📌 Description

Chess Stats is a **Python** application using **Tkinter** and **ttkbootstrap** that allows you to track your chess game statistics. This improved version offers a more modern and ergonomic interface while maintaining the original functionalities.

---

## 🛠️ Features

- 🎨 **Modernized interface** with **ttkbootstrap** and an improved theme
- 📈 Real-time tracking of your **ELO**
- 🎯 Setting a target for games to play
- ✅ Quick result entry:
  - **Win** ➝ Increases ELO
  - **Loss** ➝ Decreases ELO
  - **Draw** ➝ Option to modify ELO
- 🗂️ Automatic data saving in a `chess_stats.json` file

---

## 🚀 Installation and Usage

### 📥 Prerequisites

- **Python 3.x** installed
- Required libraries: `tkinter`, `json`, `ttkbootstrap`

### 🏗️ Installation

1. **Clone this repository**:
   ```sh
   git clone https://github.com/KucoDEV/chess-stats
   cd chess-stats
   ```

2. **Install dependencies**:
   ```sh
   pip install ttkbootstrap
   ```

3. **Run the application**:
   ```sh
   python main.py
   ```

---

## 📂 Project Structure

```
chess-stats/
│── main.py                   # Main code with enhanced interface with console
│── main.pyw                  # Main code with enhanced interface without console
│── chess_stats.json          # Statistics storage file
│── README.md                 # Project documentation
```

---

## 🤖 Code Functionality

### 🏆 Game Management

The application loads statistics from `chess_stats.json`. You can add a **win, loss, or draw** using the interactive buttons.

ELO progression is dynamically requested through `tkinter` dialog boxes.

### 🔄 Automatic Saving

Each time statistics are updated, the `chess_stats.json` file is updated accordingly.

---

## 📜 License

This project is licensed under the **MIT** license. You are free to modify and redistribute it.
