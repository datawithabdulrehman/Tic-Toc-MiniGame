# 🎮 Tic-Tac-Toe Mini Game

A simple **Tic-Tac-Toe Mini Game built with Python**. This project recreates the classic two-player game in a beginner-friendly way while practicing fundamental Python programming concepts.

## 📌 Project Overview

Tic-Tac-Toe is a classic two-player game played on a **3×3 grid**.

Players take turns placing their symbols — **X** and **O** — on the board. The first player to get three of their symbols in a row, column, or diagonal wins the game.

This project is designed to practice basic programming logic and game development concepts using Python.

## ✨ Features

* 🎮 Two-player gameplay
* ❌ Player X
* ⭕ Player O
* 🏆 Automatic win detection
* 🤝 Draw/tie detection
* 🔄 Turn-based gameplay
* 🖥️ Console-based interface
* 🐍 Beginner-friendly Python project

## 🛠️ Technologies Used

* **Python 3**
* Python Standard Library
* Command Line / Terminal

## 📂 Project Structure

```text
Tic-Toc-MiniGame/
│
├── Tic_Toc.py        # Main game program
└── README.md         # Project documentation
```

## 🎯 How the Game Works

The game uses a **3×3 board**:

```text
     |     |
  1  |  2  |  3
-----+-----+-----
  4  |  5  |  6
-----+-----+-----
  7  |  8  |  9
     |     |
```

Players select an available position on the board to place their symbol.

A player wins when they successfully create one of these combinations:

```text
1 2 3    4 5 6    7 8 9
1 4 7    2 5 8    3 6 9
1 5 9    3 5 7
```

## 🔄 Game Flow

```text
Start
  │
  ▼
Display Board
  │
  ▼
Player X Makes a Move
  │
  ▼
Check Winner
  │
  ├── Winner → Game Over
  │
  └── No Winner
          │
          ▼
    Player O Makes a Move
          │
          ▼
       Check Winner
          │
          └──────► Repeat
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/datawithabdulrehman/Tic-Toc-MiniGame.git
```

### 2. Navigate to the Project

```bash
cd Tic-Toc-MiniGame
```

### 3. Run the Game

```bash
python Tic_Toc.py
```

If your system uses `python3`:

```bash
python3 Tic_Toc.py
```

## 💻 Example

```text
==============================
      TIC-TAC-TOE GAME
==============================

Player X's Turn

Enter your position:
```

The board updates after every move until one player wins or the game ends in a draw.

## 🎯 Concepts Practiced

This project helps demonstrate important Python fundamentals:

* Variables
* Lists
* Functions
* Loops
* Conditional statements
* User input
* Boolean logic
* Game-state management
* Win-condition checking
* Turn-based programming

## 🔮 Future Improvements

Possible improvements include:

* [ ] Add Player vs Computer mode
* [ ] Add AI opponent
* [ ] Implement Minimax algorithm
* [ ] Add difficulty levels
* [ ] Add score tracking
* [ ] Add replay functionality
* [ ] Add a graphical user interface
* [ ] Improve input validation
* [ ] Add sound effects and animations

## 👨‍💻 Author

**Abdul Rehman**

Data Science Student | Python & Machine Learning Enthusiast

🔗 **GitHub:** https://github.com/datawithabdulrehman

## ⭐ Support

If you enjoyed this project, consider giving the repository a ⭐ on GitHub!

---

### 🐍 Built with Python | 🎮 Made for Fun & Learning
