# 🤖 AI-Practicals-SPPU

<div align="center">

![Python](https://img.shields.io/badge/Language-Python%203-blue?style=for-the-badge&logo=python)
![Prolog](https://img.shields.io/badge/Language-Prolog-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Comprehensive AI Algorithms & Expert Systems Collection**

A collection of practical AI implementations covering graph traversal, game theory, sorting algorithms, backtracking, chatbots, and expert systems. Perfect for learning AI fundamentals!

[View on GitHub](https://github.com/avartan007/AI-Practicals-SPPU) • [Report Issue](https://github.com/avartan007/AI-Practicals-SPPU/issues)

</div>

---

## ✨ Features

- 🔍 **Graph Traversal** - DFS & BFS implementations
- ♟️ **Game AI** - Minimax algorithm for Tic-Tac-Toe
- 📊 **Sorting Algorithms** - Greedy selection sort with visualization
- 🎯 **Backtracking** - N-Queens problem solver
- 💬 **Chatbot** - Simple conversational AI for customer interaction
- 🏥 **Expert Systems** - Disease diagnosis & employee evaluation systems
- 📚 **Prolog Implementation** - Logic programming examples

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- SWI-Prolog (for .pl files)

### Installation

```bash
# Clone the repository
git clone https://github.com/avartan007/AI-Practicals-SPPU.git
cd AI-Practicals-SPPU

# No external dependencies required for Python files
# Run any Python file directly
python 1.py
```

## 📖 Usage

### **1.py - Graph Traversal (DFS & BFS)**
```bash
python 1.py
# Enter number of vertices: 4
# Enter number of edges: 5
# Enter edges (format: u v): 0 1
# ...
# Enter starting node: 0
```

### **2.py - Tic-Tac-Toe with AI (Minimax)**
```bash
python 2.py
# Play against an unbeatable AI using minimax algorithm
# Enter moves as (row col) format
```

### **3.py - Selection Sort (Greedy)**
```bash
python 3.py
# Visualize each pass of selection sort algorithm
```

### **4.py - N-Queens Problem**
```bash
python 4.py
# Enter N: 8
# Finds and displays all possible solutions
```

### **5.py - Simple Chatbot**
```bash
python 5.py
# Interactive chatbot with pattern matching
```

### **6.pl & emp.pl - Expert Systems (Prolog)**
```bash
swipl -f 6.pl -t start
# Interactive disease diagnosis system

swipl -f emp.pl -t start
# Employee performance evaluation system
```

## 📂 Project Structure

```
AI-Practicals-SPPU/
├── 1.py                 # Graph Traversal (DFS/BFS)
├── 2.py                 # Tic-Tac-Toe AI
├── 3.py                 # Selection Sort Greedy
├── 4.py                 # N-Queens Backtracking
├── 5.py                 # Chatbot
├── 6.pl                 # Disease Diagnosis Expert System
├── emp.pl               # Employee Evaluation Expert System
├── README.md            # This file
└── .gitignore           # Git ignore rules
```

## 🎓 Algorithms Covered

| File | Algorithm | Type | Time Complexity |
|------|-----------|------|-----------------|
| 1.py | DFS/BFS | Graph Traversal | O(V + E) |
| 2.py | Minimax | Game Theory | O(b^d) |
| 3.py | Selection Sort | Greedy | O(n²) |
| 4.py | Backtracking | CSP | O(N!) |
| 5.py | Pattern Matching | NLP | O(n) |
| 6.pl | Forward Chaining | Expert System | Varies |
| emp.pl | Rule-Based | Expert System | Varies |

## 🛠️ Technologies Used

- **Python 3** - Core implementation language
- **Prolog (SWI-Prolog)** - Logic programming & expert systems
- **Collections (deque)** - Queue data structure
- **Math module** - Minimax algorithm utilities

## 📚 Learning Outcomes

After studying this repository, you'll understand:
- ✅ Graph traversal algorithms and their applications
- ✅ Game AI using minimax and alpha-beta pruning concepts
- ✅ Greedy algorithms and optimization
- ✅ Backtracking for constraint satisfaction
- ✅ Natural language processing basics
- ✅ Expert systems and knowledge representation
- ✅ Logic programming with Prolog

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**SPPU AI Practicals**
- GitHub: [@avartan007](https://github.com/avartan007)

---

<div align="center">

**⭐ Star this repo if it helped you learn AI concepts!**

Made with ❤️ for AI enthusiasts and SPPU students

</div>