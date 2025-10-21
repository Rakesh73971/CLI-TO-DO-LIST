

# 📝 To-Do List (Python CLI)

A simple **command-line To-Do List application** built using Python.
It allows users to **add, display, and remove tasks**, and stores all data in a **CSV file** so that tasks are saved even after exiting the program.

---

## 🚀 Features

* 📄 Display all saved tasks
* ➕ Add new tasks
* ❌ Remove existing tasks
* 💾 Automatically saves tasks to a CSV file
* 🔁 Loads previously saved tasks on startup

---

## 🧠 How It Works

The program maintains a task list in memory (`tasks` list) and syncs it with a CSV file (`tasks.csv`):

* When you **add** or **remove** a task, it updates the CSV file instantly.
* When the program **starts**, it loads all tasks from `tasks.csv`.

---

## 🗂 Project Structure

```
todo_list/
│
├── tasks.csv          # Stores all tasks (auto-created)
├── todo.py            # Main Python program
└── README.md          # Project documentation
```

---

## ⚙️ How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/todo-list-python.git
```

### 2️⃣ Navigate into the Project Folder

```bash
cd todo-list-python
```

### 3️⃣ Run the Program

```bash
python todo.py
```

---

## 💡 Usage Example

```bash
Todo-List
1. Display Tasks
2. Add Task
3. Remove Task
4. Exit
Enter your choice: 2
Enter your task: Finish React To-Do project
Task added successfully!
```

Next time you run the program, your task will still be there!

---

## 📁 File Example (tasks.csv)

```
Learn React
Learn Python Full Stack
Complete  project
```

---

## 🧰 Requirements

* Python 3.7 or above
* No external libraries (uses only built-in modules: `csv`, `os`)

---


---

## 🧑‍💻 Author

**Rakesh**
💻 Computer Science Engineering Student
📚 Passionate about Python & Full Stack Development


